// Main JavaScript for the Data Structures Question Generator
document.addEventListener('DOMContentLoaded', function() {
    // Initialize the app
    initApp();
});

// Global variables
let currentQuestions = [];
let currentQuestionIndex = 0;

function initApp() {
    // Set up the form submission handler
    const questionForm = document.getElementById('question-form');
    if (questionForm) {
        questionForm.addEventListener('submit', handleFormSubmit);
    }
    
    // Set up event delegation for dynamic elements
    document.addEventListener('click', function(event) {
        // Show answer button
        if (event.target.classList.contains('show-answer-btn')) {
            const questionId = event.target.getAttribute('data-question-id');
            toggleAnswer(questionId);
        }
        
        // Navigation buttons
        if (event.target.id === 'prev-question') {
            navigateQuestions('prev');
        }
        
        if (event.target.id === 'next-question') {
            navigateQuestions('next');
        }
        
        // Code submission for advanced questions
        if (event.target.classList.contains('submit-code-btn')) {
            const questionId = event.target.getAttribute('data-question-id');
            submitCode(questionId);
        }
    });
}

// Handle form submission to get questions
async function handleFormSubmit(event) {
    event.preventDefault();
    
    // Get form data
    const formData = {
        topic: document.getElementById('topic').value,
        difficulty: document.getElementById('difficulty').value,
        num_questions: document.getElementById('num_questions').value
    };
    
    // Show loading state
    const questionsContainer = document.getElementById('questions-container');
    questionsContainer.innerHTML = '<div class="loading">Loading questions...</div>';
    
    try {
        // Send request to backend
        const response = await fetch('/get_questions', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });
        
        if (!response.ok) {
            throw new Error('Failed to fetch questions');
        }
        
        // Get questions data
        currentQuestions = await response.json();
        currentQuestionIndex = 0;
        
        // Display first question
        if (currentQuestions.length > 0) {
            displayQuestions();
        } else {
            questionsContainer.innerHTML = '<div class="no-questions">No questions found for the selected criteria.</div>';
        }
    } catch (error) {
        console.error('Error fetching questions:', error);
        questionsContainer.innerHTML = '<div class="error">Error loading questions. Please try again.</div>';
    }
}

// Display questions in the container
function displayQuestions() {
    const questionsContainer = document.getElementById('questions-container');
    
    // Clear previous content
    questionsContainer.innerHTML = '';
    
    if (currentQuestions.length === 0) {
        questionsContainer.innerHTML = '<div class="no-questions">No questions available.</div>';
        return;
    }
    
    // Create progress bar
    const progressBar = document.createElement('div');
    progressBar.className = 'progress-bar';
    const progressBarInner = document.createElement('div');
    progressBarInner.className = 'progress-bar-inner';
    progressBarInner.style.width = `${((currentQuestionIndex + 1) / currentQuestions.length) * 100}%`;
    progressBar.appendChild(progressBarInner);
    questionsContainer.appendChild(progressBar);
    
    // Get current question
    const currentQuestion = currentQuestions[currentQuestionIndex];
    
    // Process the question text by replacing [VALUES] with actual values
    let questionText = currentQuestion.question;
    let answerText = currentQuestion.answer;
    let explanation = getQuestionExplanation(currentQuestion.topic, currentQuestion.difficulty);
    
    // Replace [VALUES] with the actual array
    if (currentQuestion.values) {
        const valuesStr = JSON.stringify(currentQuestion.values);
        questionText = questionText.replace(/\[VALUES\]/g, valuesStr);
        
        // Process other placeholders in the answer based on question type
        if (currentQuestion.topic === 'Array') {
            const values = currentQuestion.values;
            
            // Replace common placeholders
            answerText = answerText
                .replace(/\[LENGTH\]/g, values.length)
                .replace(/\[SUM\]/g, values.reduce((a, b) => a + b, 0))
                .replace(/\[MAX\]/g, Math.max(...values))
                .replace(/\[MIN\]/g, Math.min(...values))
                .replace(/\[AVERAGE\]/g, (values.reduce((a, b) => a + b, 0) / values.length).toFixed(2))
                .replace(/\[REVERSED\]/g, JSON.stringify([...values].reverse()))
                .replace(/\[SORTED\]/g, JSON.stringify([...values].sort((a, b) => a - b)))
                .replace(/\[DIFFERENCE\]/g, Math.max(...values) - Math.min(...values))
                .replace(/\[PRODUCT\]/g, values.reduce((a, b) => a * b, 1))
                .replace(/\[MEDIAN\]/g, getMedian(values))
                .replace(/\[SECOND_MAX\]/g, getSecondMax(values));
            
            // Replace specific index value if present
            if (questionText.includes('index 2') && values.length > 2) {
                answerText = answerText.replace(/\[VALUE\]/g, values[2]);
            }
        } else if (currentQuestion.topic.includes('Linked List')) {
            const values = currentQuestion.values;
            
            // Replace common placeholders
            answerText = answerText
                .replace(/\[HEAD\]/g, values[0])
                .replace(/\[TAIL\]/g, values[values.length - 1])
                .replace(/\[LENGTH\]/g, values.length)
                .replace(/\[SUM\]/g, values.reduce((a, b) => a + b, 0))
                .replace(/\[MAX\]/g, Math.max(...values))
                .replace(/\[MIN\]/g, Math.min(...values))
                .replace(/\[REVERSED\]/g, JSON.stringify([...values].reverse()));
            
            // If asking about the 3rd node and it exists
            if (questionText.includes('3rd node') && values.length > 2) {
                answerText = answerText.replace(/\[VALUE\]/g, values[2]);
            }
            
            // If asking about deleting the first node
            if (questionText.includes('deleted the first node')) {
                answerText = answerText.replace(/\[RESULT\]/g, JSON.stringify(values.slice(1)));
            }
        } else if (currentQuestion.topic === 'Tree') {
            const values = currentQuestion.values;
            
            // For tree questions, we'll use the first value as the root
            answerText = answerText
                .replace(/\[ROOT\]/g, values[0])
                .replace(/\[COUNT\]/g, values.length)
                .replace(/\[SUM\]/g, values.reduce((a, b) => a + b, 0))
                .replace(/\[MAX\]/g, Math.max(...values))
                .replace(/\[MIN\]/g, Math.min(...values));
            
            // If we have enough values for a basic tree
            if (values.length > 2) {
                answerText = answerText
                    .replace(/\[LEFT_CHILD\]/g, values[1])
                    .replace(/\[RIGHT_CHILD\]/g, values[2]);
            }
            
            // For leaf nodes in a simple binary tree representation
            const leaves = values.filter((_, i) => i >= Math.floor(values.length / 2));
            answerText = answerText.replace(/\[LEAVES\]/g, JSON.stringify(leaves));
            
            // For traversals (simplified)
            answerText = answerText
                .replace(/\[INORDER\]/g, JSON.stringify(values))
                .replace(/\[PREORDER\]/g, JSON.stringify(values))
                .replace(/\[POSTORDER\]/g, JSON.stringify(values));
        }
    }
    
    // Create question card
    const questionCard = document.createElement('div');
    questionCard.className = 'question-card slide-up';
    questionCard.id = `question-${currentQuestion.id}`;
    
    // Create question header
    const questionHeader = document.createElement('div');
    questionHeader.className = 'question-header';
    
    const questionTitle = document.createElement('h3');
    questionTitle.className = 'question-title';
    questionTitle.textContent = `Question ${currentQuestionIndex + 1} of ${currentQuestions.length}`;
    
    questionHeader.appendChild(questionTitle);
    questionCard.appendChild(questionHeader);
    
    // Create question meta information
    const questionMeta = document.createElement('div');
    questionMeta.className = 'question-meta';
    
    const topicTag = document.createElement('span');
    topicTag.className = 'question-tag topic';
    topicTag.textContent = currentQuestion.topic;
    
    const difficultyTag = document.createElement('span');
    difficultyTag.className = `question-tag difficulty-${currentQuestion.difficulty}`;
    difficultyTag.textContent = `Level ${currentQuestion.difficulty}`;
    
    questionMeta.appendChild(topicTag);
    questionMeta.appendChild(difficultyTag);
    questionCard.appendChild(questionMeta);
    
    // Create question content
    const questionContent = document.createElement('div');
    questionContent.className = 'question-content';
    questionContent.textContent = questionText;
    questionCard.appendChild(questionContent);
    
    // Create explanation section
    const explanationSection = document.createElement('div');
    explanationSection.className = 'explanation-section';
    explanationSection.innerHTML = explanation;
    questionCard.appendChild(explanationSection);
    
    // Create visualization container
    const visualizationContainer = document.createElement('div');
    visualizationContainer.className = 'visualization-container';
    questionCard.appendChild(visualizationContainer);
    
    // For advanced level questions, add code editor
    if (currentQuestion.difficulty === 3) {
        const codeSection = document.createElement('div');
        codeSection.className = 'code-section';
        codeSection.innerHTML = `
            <h4>Write your solution:</h4>
            <textarea id="code-editor-${currentQuestion.id}" class="code-editor" placeholder="Write your code here..."></textarea>
            <button class="btn btn-secondary submit-code-btn" data-question-id="${currentQuestion.id}">Submit Code</button>
            <div id="code-result-${currentQuestion.id}" class="code-result"></div>
        `;
        questionCard.appendChild(codeSection);
    }
    
    // Create answer container
    const answerContainer = document.createElement('div');
    answerContainer.className = 'question-answer';
    answerContainer.id = `answer-${currentQuestion.id}`;
    
    // For code answers, format them properly
    if (answerText.includes('```')) {
        answerContainer.innerHTML = formatCodeAnswer(answerText);
    } else {
        answerContainer.textContent = answerText;
    }
    
    questionCard.appendChild(answerContainer);
    
    // Create show answer button
    const showAnswerBtn = document.createElement('button');
    showAnswerBtn.className = 'btn btn-primary show-answer-btn';
    showAnswerBtn.setAttribute('data-question-id', currentQuestion.id);
    showAnswerBtn.textContent = 'Show Answer';
    questionCard.appendChild(showAnswerBtn);
    
    // Add navigation
    const questionNav = document.createElement('div');
    questionNav.className = 'question-nav';
    
    const prevButton = document.createElement('button');
    prevButton.className = 'btn btn-outline';
    prevButton.id = 'prev-question';
    prevButton.textContent = 'Previous';
    prevButton.disabled = currentQuestionIndex === 0;
    
    const nextButton = document.createElement('button');
    nextButton.className = 'btn btn-primary';
    nextButton.id = 'next-question';
    nextButton.textContent = currentQuestionIndex < currentQuestions.length - 1 ? 'Next' : 'Finish';
    
    questionNav.appendChild(prevButton);
    questionNav.appendChild(nextButton);
    questionCard.appendChild(questionNav);
    
    // Add the question card to the container
    questionsContainer.appendChild(questionCard);
    
    // Render the visualization based on the data structure type
    renderVisualization(currentQuestion.topic, currentQuestion.values, visualizationContainer);
}

// Helper functions for calculations
function getMedian(arr) {
    const sorted = [...arr].sort((a, b) => a - b);
    const mid = Math.floor(sorted.length / 2);
    return sorted.length % 2 === 0 ? 
        ((sorted[mid - 1] + sorted[mid]) / 2).toFixed(2) : 
        sorted[mid];
}

function getSecondMax(arr) {
    const unique = [...new Set(arr)].sort((a, b) => b - a);
    return unique.length > 1 ? unique[1] : unique[0];
}

// Format code answers with syntax highlighting
function formatCodeAnswer(answerText) {
    return answerText.replace(/```python\n([\s\S]*?)```/g, '<pre><code class="language-python">$1</code></pre>');
}

// Submit code for advanced questions
function submitCode(questionId) {
    const codeEditor = document.getElementById(`code-editor-${questionId}`);
    const codeResult = document.getElementById(`code-result-${questionId}`);
    const code = codeEditor.value.trim();
    
    if (!code) {
        codeResult.innerHTML = '<div class="error">Please write some code before submitting.</div>';
        return;
    }
    
    // Simple validation - check if code contains basic programming constructs
    const hasFunction = code.includes('def ') || code.includes('function');
    const hasLogic = code.includes('if ') || code.includes('for ') || code.includes('while ');
    const hasReturn = code.includes('return');
    
    if (hasFunction && (hasLogic || hasReturn)) {
        codeResult.innerHTML = '<div class="success">Code submitted successfully! Good approach to the problem.</div>';
    } else {
        codeResult.innerHTML = '<div class="warning">Code submitted. Consider adding functions, control structures, or return statements for a complete solution.</div>';
    }
}

// Get detailed explanation based on topic and difficulty
function getQuestionExplanation(topic, difficulty) {
    const explanations = {
        'Array': {
            1: `
                <h4>Arrays - Beginner Level Concepts</h4>
                <p>Arrays are fundamental data structures that store elements in contiguous memory locations. Key concepts at this level include:</p>
                <ul>
                    <li><strong>Indexing:</strong> Accessing elements by index (O(1) time complexity)</li>
                    <li><strong>Basic Operations:</strong> Insertion, deletion, and traversal</li>
                    <li><strong>Array Properties:</strong> Length, sum, min/max calculations</li>
                    <li><strong>Zero-based Indexing:</strong> Understanding that arrays start at index 0</li>
                    <li><strong>Memory Layout:</strong> Elements stored in consecutive memory locations</li>
                </ul>
            `,
            2: `
                <h4>Arrays - Intermediate Level Concepts</h4>
                <p>At this level, we explore more complex array operations and algorithms:</p>
                <ul>
                    <li><strong>Two-pointer Technique:</strong> Using two pointers to solve problems efficiently</li>
                    <li><strong>Sliding Window:</strong> Maintaining a window of elements for optimization</li>
                    <li><strong>Array Manipulation:</strong> Rotation, reversal, and transformation</li>
                    <li><strong>Subarray Problems:</strong> Finding subarrays with specific properties</li>
                    <li><strong>Searching Algorithms:</strong> Binary search and its variations</li>
                    <li><strong>Time Complexity:</strong> Understanding and optimizing algorithmic efficiency</li>
                </ul>
            `,
            3: `
                <h4>Arrays - Advanced Level Concepts</h4>
                <p>Advanced array problems involve complex algorithms and optimizations:</p>
                <ul>
                    <li><strong>Dynamic Programming:</strong> Solving complex problems using DP on arrays</li>
                    <li><strong>Kadane's Algorithm:</strong> Maximum subarray sum problem</li>
                    <li><strong>Dutch National Flag:</strong> Three-way partitioning algorithm</li>
                    <li><strong>Advanced Sorting:</strong> Merge sort, quick sort with optimizations</li>
                    <li><strong>Space-Time Tradeoffs:</strong> Balancing memory usage and execution time</li>
                    <li><strong>Mathematical Algorithms:</strong> Number theory applications in arrays</li>
                </ul>
            `
        },
        'Singly Linked List': {
            1: `
                <h4>Singly Linked Lists - Beginner Level Concepts</h4>
                <p>Singly Linked Lists are linear data structures where each node contains data and a reference to the next node:</p>
                <ul>
                    <li><strong>Node Structure:</strong> Each node has data and a next pointer</li>
                    <li><strong>Head Pointer:</strong> Points to the first node in the list</li>
                    <li><strong>Traversal:</strong> Moving through the list using next pointers</li>
                    <li><strong>Basic Operations:</strong> Insertion at head/tail, deletion, search</li>
                    <li><strong>NULL Termination:</strong> Last node's next pointer is NULL</li>
                    <li><strong>Dynamic Size:</strong> Can grow and shrink during runtime</li>
                </ul>
            `,
            2: `
                <h4>Singly Linked Lists - Intermediate Level Concepts</h4>
                <p>Intermediate concepts focus on more complex operations and algorithms:</p>
                <ul>
                    <li><strong>Two-Pointer Technique:</strong> Fast and slow pointers for cycle detection</li>
                    <li><strong>List Reversal:</strong> Iterative and recursive approaches</li>
                    <li><strong>Merging Lists:</strong> Combining sorted linked lists</li>
                    <li><strong>Finding Middle:</strong> Using Floyd's algorithm</li>
                    <li><strong>Cycle Detection:</strong> Floyd's cycle-finding algorithm</li>
                    <li><strong>Node Manipulation:</strong> Swapping, partitioning, and reordering</li>
                </ul>
            `,
            3: `
                <h4>Singly Linked Lists - Advanced Level Concepts</h4>
                <p>Advanced problems require sophisticated algorithms and optimizations:</p>
                <ul>
                    <li><strong>Complex Manipulations:</strong> Reversing in groups, reordering</li>
                    <li><strong>Intersection Problems:</strong> Finding intersection points of lists</li>
                    <li><strong>Palindrome Detection:</strong> Checking if list forms a palindrome</li>
                    <li><strong>Sorting Algorithms:</strong> Merge sort on linked lists</li>
                    <li><strong>Memory Optimization:</strong> In-place algorithms</li>
                    <li><strong>Advanced Patterns:</strong> Skip lists, self-organizing lists</li>
                </ul>
            `
        },
        'Doubly Linked List': {
            1: `
                <h4>Doubly Linked Lists - Beginner Level Concepts</h4>
                <p>Doubly Linked Lists have nodes with references to both next and previous nodes:</p>
                <ul>
                    <li><strong>Bidirectional Traversal:</strong> Can move forward and backward</li>
                    <li><strong>Node Structure:</strong> Contains data, next, and prev pointers</li>
                    <li><strong>Head and Tail:</strong> Pointers to first and last nodes</li>
                    <li><strong>Insertion/Deletion:</strong> More complex due to two pointers</li>
                    <li><strong>Memory Overhead:</strong> Extra memory for prev pointers</li>
                    <li><strong>Boundary Conditions:</strong> Handling head and tail updates</li>
                </ul>
            `
        },
        'Circular Linked List': {
            1: `
                <h4>Circular Linked Lists - Beginner Level Concepts</h4>
                <p>Circular Linked Lists have the last node pointing back to the first node:</p>
                <ul>
                    <li><strong>Circular Structure:</strong> No NULL pointers, forms a circle</li>
                    <li><strong>Traversal Termination:</strong> Stop when reaching starting node again</li>
                    <li><strong>Applications:</strong> Round-robin scheduling, circular buffers</li>
                    <li><strong>Insertion/Deletion:</strong> Maintaining circular property</li>
                    <li><strong>Detection:</strong> Identifying if a list is circular</li>
                    <li><strong>Conversion:</strong> Converting between linear and circular lists</li>
                </ul>
            `
        },
        'Tree': {
            1: `
                <h4>Trees - Beginner Level Concepts</h4>
                <p>Trees are hierarchical data structures with a root node and child nodes:</p>
                <ul>
                    <li><strong>Tree Terminology:</strong> Root, leaf, parent, child, sibling nodes</li>
                    <li><strong>Binary Trees:</strong> Each node has at most two children</li>
                    <li><strong>Tree Traversals:</strong> Inorder, preorder, postorder</li>
                    <li><strong>Height and Depth:</strong> Measuring tree dimensions</li>
                    <li><strong>Node Counting:</strong> Total nodes, leaf nodes, internal nodes</li>
                    <li><strong>Basic Properties:</strong> Understanding tree structure and relationships</li>
                </ul>
            `,
            2: `
                <h4>Trees - Intermediate Level Concepts</h4>
                <p>Intermediate tree concepts involve more complex operations and properties:</p>
                <ul>
                    <li><strong>Binary Search Trees:</strong> Ordered binary trees for efficient searching</li>
                    <li><strong>Tree Balancing:</strong> AVL trees, red-black trees concepts</li>
                    <li><strong>Level-order Traversal:</strong> Breadth-first search in trees</li>
                    <li><strong>Path Algorithms:</strong> Finding paths, lowest common ancestor</li>
                    <li><strong>Tree Construction:</strong> Building trees from traversals</li>
                    <li><strong>Tree Properties:</strong> Diameter, width, symmetry, balance</li>
                </ul>
            `,
            3: `
                <h4>Trees - Advanced Level Concepts</h4>
                <p>Advanced tree problems require deep understanding and complex algorithms:</p>
                <ul>
                    <li><strong>Self-Balancing Trees:</strong> AVL rotations, Red-Black tree operations</li>
                    <li><strong>Advanced Data Structures:</strong> Segment trees, Fenwick trees, Tries</li>
                    <li><strong>Tree Algorithms:</strong> Morris traversal, tree serialization</li>
                    <li><strong>Optimization Techniques:</strong> Space-efficient algorithms</li>
                    <li><strong>Complex Operations:</strong> Tree reconstruction, path sum problems</li>
                    <li><strong>Specialized Trees:</strong> B-trees, suffix trees, decision trees</li>
                </ul>
            `
        }
    };
    
    return explanations[topic] && explanations[topic][difficulty] ? explanations[topic][difficulty] : '';
}

// Toggle answer visibility
function toggleAnswer(questionId) {
    const answerElement = document.getElementById(`answer-${questionId}`);
    const button = document.querySelector(`.show-answer-btn[data-question-id="${questionId}"]`);
    
    if (answerElement.classList.contains('visible')) {
        answerElement.classList.remove('visible');
        button.textContent = 'Show Answer';
    } else {
        answerElement.classList.add('visible');
        button.textContent = 'Hide Answer';
    }
}

// Navigate between questions
function navigateQuestions(direction) {
    if (direction === 'prev' && currentQuestionIndex > 0) {
        currentQuestionIndex--;
        displayQuestions();
    } else if (direction === 'next' && currentQuestionIndex < currentQuestions.length - 1) {
        currentQuestionIndex++;
        displayQuestions();
    } else if (direction === 'next' && currentQuestionIndex === currentQuestions.length - 1) {
        // This is the last question, go back to the form
        currentQuestions = [];
        currentQuestionIndex = 0;
        
        const questionsContainer = document.getElementById('questions-container');
        questionsContainer.innerHTML = '<div class="completed">All questions completed! Select new criteria to generate more questions.</div>';
        
        // Scroll to the form
        document.getElementById('question-form').scrollIntoView({ behavior: 'smooth' });
    }
}

// Render visualization based on data structure type
function renderVisualization(type, values, container) {
    if (!values || !container) return;
    
    container.innerHTML = '';
    
    if (type === 'Array') {
        renderArrayVisualization(values, container);
    } else if (type.includes('Linked List')) {
        renderLinkedListVisualization(values, container, type);
    } else if (type === 'Tree') {
        renderTreeVisualization(values, container);
    }
}

// Render array visualization
function renderArrayVisualization(values, container) {
    const arrayContainer = document.createElement('div');
    arrayContainer.className = 'array-visualization';
    
    const arrayItems = document.createElement('div');
    arrayItems.style.display = 'flex';
    arrayItems.style.flexWrap = 'wrap';
    arrayItems.style.gap = '8px';
    arrayItems.style.justifyContent = 'center';
    
    values.forEach((value, index) => {
        const arrayItem = document.createElement('div');
        arrayItem.className = 'array-item';
        arrayItem.textContent = value;
        arrayItem.style.animationDelay = `${index * 0.1}s`;
        
        // Add index label
        const indexLabel = document.createElement('div');
        indexLabel.style.fontSize = '10px';
        indexLabel.style.color = '#666';
        indexLabel.style.textAlign = 'center';
        indexLabel.style.marginTop = '2px';
        indexLabel.textContent = index;
        
        const itemContainer = document.createElement('div');
        itemContainer.style.display = 'flex';
        itemContainer.style.flexDirection = 'column';
        itemContainer.style.alignItems = 'center';
        itemContainer.appendChild(arrayItem);
        itemContainer.appendChild(indexLabel);
        
        arrayItems.appendChild(itemContainer);
    });
    
    arrayContainer.appendChild(arrayItems);
    container.appendChild(arrayContainer);
}

// Render linked list visualization
function renderLinkedListVisualization(values, container, type) {
    const linkedListContainer = document.createElement('div');
    linkedListContainer.className = 'linkedlist-visualization';
    
    const linkedListItems = document.createElement('div');
    linkedListItems.style.display = 'flex';
    linkedListItems.style.flexWrap = 'wrap';
    linkedListItems.style.alignItems = 'center';
    linkedListItems.style.gap = '20px';
    linkedListItems.style.justifyContent = 'center';
    
    values.forEach((value, index) => {
        const nodeContainer = document.createElement('div');
        nodeContainer.className = 'linkedlist-node';
        nodeContainer.style.position = 'relative';
        nodeContainer.style.display = 'flex';
        nodeContainer.style.alignItems = 'center';
        
        const node = document.createElement('div');
        node.className = 'linkedlist-item';
        node.textContent = value;
        node.style.animationDelay = `${index * 0.1}s`;
        
        // Add labels for head and tail
        if (index === 0) {
            const headLabel = document.createElement('div');
            headLabel.style.position = 'absolute';
            headLabel.style.top = '-25px';
            headLabel.style.left = '50%';
            headLabel.style.transform = 'translateX(-50%)';
            headLabel.style.fontSize = '12px';
            headLabel.style.fontWeight = 'bold';
            headLabel.style.color = '#059669';
            headLabel.textContent = 'HEAD';
            nodeContainer.appendChild(headLabel);
        }
        
        if (index === values.length - 1) {
            const tailLabel = document.createElement('div');
            tailLabel.style.position = 'absolute';
            tailLabel.style.bottom = '-25px';
            tailLabel.style.left = '50%';
            tailLabel.style.transform = 'translateX(-50%)';
            tailLabel.style.fontSize = '12px';
            tailLabel.style.fontWeight = 'bold';
            tailLabel.style.color = '#dc2626';
            tailLabel.textContent = 'TAIL';
            nodeContainer.appendChild(tailLabel);
        }
        
        nodeContainer.appendChild(node);
        
        // Add arrows based on list type
        if (index < values.length - 1 || type === 'Circular Linked List') {
            const arrow = document.createElement('div');
            arrow.style.width = '30px';
            arrow.style.height = '2px';
            arrow.style.backgroundColor = '#4b5563';
            arrow.style.position = 'relative';
            arrow.style.marginLeft = '10px';
            arrow.style.marginRight = '10px';
            
            // Arrow head
            const arrowHead = document.createElement('div');
            arrowHead.style.position = 'absolute';
            arrowHead.style.right = '0';
            arrowHead.style.top = '-3px';
            arrowHead.style.width = '8px';
            arrowHead.style.height = '8px';
            arrowHead.style.borderTop = '2px solid #4b5563';
            arrowHead.style.borderRight = '2px solid #4b5563';
            arrowHead.style.transform = 'rotate(45deg)';
            arrow.appendChild(arrowHead);
            
            nodeContainer.appendChild(arrow);
        }
        
        // For doubly linked list, add backward arrows
        if (type === 'Doubly Linked List' && index > 0) {
            const backArrow = document.createElement('div');
            backArrow.style.position = 'absolute';
            backArrow.style.bottom = '-15px';
            backArrow.style.left = '-25px';
            backArrow.style.width = '30px';
            backArrow.style.height = '2px';
            backArrow.style.backgroundColor = '#9ca3af';
            
            const backArrowHead = document.createElement('div');
            backArrowHead.style.position = 'absolute';
            backArrowHead.style.left = '0';
            backArrowHead.style.top = '-3px';
            backArrowHead.style.width = '8px';
            backArrowHead.style.height = '8px';
            backArrowHead.style.borderTop = '2px solid #9ca3af';
            backArrowHead.style.borderLeft = '2px solid #9ca3af';
            backArrowHead.style.transform = 'rotate(-45deg)';
            backArrow.appendChild(backArrowHead);
            
            nodeContainer.appendChild(backArrow);
        }
        
        linkedListItems.appendChild(nodeContainer);
    });
    
    // For circular linked list, add arrow from tail to head
    if (type === 'Circular Linked List' && values.length > 1) {
        const circularArrow = document.createElement('div');
        circularArrow.style.position = 'absolute';
        circularArrow.style.top = '50%';
        circularArrow.style.left = '50%';
        circularArrow.style.transform = 'translate(-50%, -50%)';
        circularArrow.style.width = '100px';
        circularArrow.style.height = '100px';
        circularArrow.style.border = '2px dashed #f97316';
        circularArrow.style.borderRadius = '50%';
        circularArrow.style.opacity = '0.7';
        linkedListContainer.appendChild(circularArrow);
    }
    
    linkedListContainer.appendChild(linkedListItems);
    container.appendChild(linkedListContainer);
}

// Render tree visualization with improved scaling
function renderTreeVisualization(values, container) {
    const treeContainer = document.createElement('div');
    treeContainer.className = 'tree-visualization';
    treeContainer.style.position = 'relative';
    treeContainer.style.width = '100%';
    treeContainer.style.height = '100%';
    treeContainer.style.overflow = 'auto';
    
    // Calculate optimal dimensions based on number of nodes
    const numNodes = values.length;
    const maxLevel = Math.floor(Math.log2(numNodes)) + 1;
    const maxNodesInLevel = Math.pow(2, maxLevel - 1);
    
    // Dynamic sizing based on container and number of nodes
    const containerRect = container.getBoundingClientRect();
    const containerWidth = Math.max(containerRect.width, 400);
    const containerHeight = Math.max(containerRect.height, 300);
    
    // Calculate node size and spacing
    const nodeSize = Math.max(20, Math.min(40, containerWidth / (maxNodesInLevel * 2)));
    const levelHeight = Math.max(60, containerHeight / (maxLevel + 1));
    
    // Create SVG with proper dimensions
    const svgWidth = Math.max(containerWidth, maxNodesInLevel * nodeSize * 2);
    const svgHeight = Math.max(containerHeight, maxLevel * levelHeight);
    
    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.setAttribute('width', svgWidth);
    svg.setAttribute('height', svgHeight);
    svg.setAttribute('viewBox', `0 0 ${svgWidth} ${svgHeight}`);
    svg.style.display = 'block';
    svg.style.margin = '0 auto';
    
    // Helper function to calculate node position
    function getNodePosition(index) {
        const level = Math.floor(Math.log2(index + 1));
        const positionInLevel = index - (Math.pow(2, level) - 1);
        const nodesInLevel = Math.pow(2, level);
        
        const x = (svgWidth / (nodesInLevel + 1)) * (positionInLevel + 1);
        const y = levelHeight * (level + 1);
        
        return { x, y, level };
    }
    
    // Draw edges first
    for (let i = 0; i < values.length; i++) {
        const leftChildIndex = 2 * i + 1;
        const rightChildIndex = 2 * i + 2;
        
        if (leftChildIndex < values.length || rightChildIndex < values.length) {
            const parentPos = getNodePosition(i);
            
            if (leftChildIndex < values.length) {
                const leftChildPos = getNodePosition(leftChildIndex);
                const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
                line.setAttribute('x1', parentPos.x);
                line.setAttribute('y1', parentPos.y);
                line.setAttribute('x2', leftChildPos.x);
                line.setAttribute('y2', leftChildPos.y);
                line.setAttribute('stroke', '#4b5563');
                line.setAttribute('stroke-width', '2');
                line.setAttribute('opacity', '0.7');
                svg.appendChild(line);
            }
            
            if (rightChildIndex < values.length) {
                const rightChildPos = getNodePosition(rightChildIndex);
                const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
                line.setAttribute('x1', parentPos.x);
                line.setAttribute('y1', parentPos.y);
                line.setAttribute('x2', rightChildPos.x);
                line.setAttribute('y2', rightChildPos.y);
                line.setAttribute('stroke', '#4b5563');
                line.setAttribute('stroke-width', '2');
                line.setAttribute('opacity', '0.7');
                svg.appendChild(line);
            }
        }
    }
    
    // Draw nodes
    values.forEach((value, i) => {
        const pos = getNodePosition(i);
        
        const nodeGroup = document.createElementNS('http://www.w3.org/2000/svg', 'g');
        nodeGroup.setAttribute('class', 'tree-node-group');
        
        const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
        circle.setAttribute('cx', pos.x);
        circle.setAttribute('cy', pos.y);
        circle.setAttribute('r', nodeSize / 2);
        circle.setAttribute('fill', i === 0 ? '#dc2626' : '#f97316'); // Root node is red
        circle.setAttribute('stroke', '#ffffff');
        circle.setAttribute('stroke-width', '2');
        circle.setAttribute('class', 'tree-node');
        circle.style.cursor = 'pointer';
        
        const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        text.setAttribute('x', pos.x);
        text.setAttribute('y', pos.y);
        text.setAttribute('text-anchor', 'middle');
        text.setAttribute('dominant-baseline', 'middle');
        text.setAttribute('fill', 'white');
        text.setAttribute('font-size', Math.max(10, nodeSize / 3));
        text.setAttribute('font-weight', 'bold');
        text.textContent = value;
        
        // Add labels for root
        if (i === 0) {
            const rootLabel = document.createElementNS('http://www.w3.org/2000/svg', 'text');
            rootLabel.setAttribute('x', pos.x);
            rootLabel.setAttribute('y', pos.y - nodeSize / 2 - 15);
            rootLabel.setAttribute('text-anchor', 'middle');
            rootLabel.setAttribute('fill', '#059669');
            rootLabel.setAttribute('font-size', '12');
            rootLabel.setAttribute('font-weight', 'bold');
            rootLabel.textContent = 'ROOT';
            nodeGroup.appendChild(rootLabel);
        }
        
        nodeGroup.appendChild(circle);
        nodeGroup.appendChild(text);
        svg.appendChild(nodeGroup);
        
        // Add hover effects
        nodeGroup.addEventListener('mouseenter', function() {
            circle.setAttribute('fill', '#ea580c');
            circle.setAttribute('transform', `scale(1.1)`);
            circle.setAttribute('transform-origin', `${pos.x} ${pos.y}`);
        });
        
        nodeGroup.addEventListener('mouseleave', function() {
            circle.setAttribute('fill', i === 0 ? '#dc2626' : '#f97316');
            circle.setAttribute('transform', 'scale(1)');
        });
    });
    
    treeContainer.appendChild(svg);
    container.appendChild(treeContainer);
}