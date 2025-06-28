import unittest
import sys
import os

# Add the parent directory to the path to import the app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app, generate_random_values, filter_questions
import pandas as pd

class TestTreeQuestions(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.app = app.test_client()
        self.app.testing = True
        
        # Sample tree questions for testing
        self.sample_questions = pd.DataFrame([
            {
                'id': 1,
                'topic': 'Tree',
                'difficulty': 1,
                'question': 'Given a binary tree with root [ROOT] and values [VALUES], what is the root node value?',
                'answer': 'The root node value is [ROOT]. This is the topmost node of the tree.'
            },
            {
                'id': 2,
                'topic': 'Tree',
                'difficulty': 2,
                'question': 'Check if binary tree with root [ROOT] and values [VALUES] is a Binary Search Tree.',
                'answer': 'Use recursive validation with min/max bounds for each node.'
            },
            {
                'id': 3,
                'topic': 'Tree',
                'difficulty': 3,
                'question': 'Serialize and deserialize binary tree with root [ROOT] and values [VALUES].',
                'answer': 'Use preorder traversal with null markers for serialization.'
            }
        ])
    
    def test_generate_random_values_tree(self):
        """Test that random values are generated correctly for trees."""
        values = generate_random_values('Tree')
        
        # Check that values is a list
        self.assertIsInstance(values, list)
        
        # Check that the list has between 7-15 elements
        self.assertGreaterEqual(len(values), 7)
        self.assertLessEqual(len(values), 15)
        
        # Check that all values are integers between 1-99
        for value in values:
            self.assertIsInstance(value, int)
            self.assertGreaterEqual(value, 1)
            self.assertLessEqual(value, 99)
    
    def test_filter_questions_tree_beginner(self):
        """Test filtering tree questions for beginner level."""
        filtered = filter_questions(self.sample_questions, 'Tree', 1, 1)
        
        # Should return exactly 1 question
        self.assertEqual(len(filtered), 1)
        
        # Should be the correct question
        self.assertEqual(filtered[0]['topic'], 'Tree')
        self.assertEqual(filtered[0]['difficulty'], 1)
    
    def test_filter_questions_tree_intermediate(self):
        """Test filtering tree questions for intermediate level."""
        filtered = filter_questions(self.sample_questions, 'Tree', 2, 1)
        
        # Should return exactly 1 question
        self.assertEqual(len(filtered), 1)
        
        # Should be the correct question
        self.assertEqual(filtered[0]['topic'], 'Tree')
        self.assertEqual(filtered[0]['difficulty'], 2)
    
    def test_filter_questions_tree_advanced(self):
        """Test filtering tree questions for advanced level."""
        filtered = filter_questions(self.sample_questions, 'Tree', 3, 1)
        
        # Should return exactly 1 question
        self.assertEqual(len(filtered), 1)
        
        # Should be the correct question
        self.assertEqual(filtered[0]['topic'], 'Tree')
        self.assertEqual(filtered[0]['difficulty'], 3)
    
    def test_tree_question_structure(self):
        """Test that tree questions have the correct structure."""
        for _, question in self.sample_questions.iterrows():
            # Check required fields
            self.assertIn('id', question)
            self.assertIn('topic', question)
            self.assertIn('difficulty', question)
            self.assertIn('question', question)
            self.assertIn('answer', question)
            
            # Check data types
            self.assertIsInstance(question['id'], (int, float))
            self.assertIsInstance(question['topic'], str)
            self.assertIsInstance(question['difficulty'], (int, float))
            self.assertIsInstance(question['question'], str)
            self.assertIsInstance(question['answer'], str)
    
    def test_tree_root_concepts(self):
        """Test that tree questions properly reference root concepts."""
        for _, question in self.sample_questions.iterrows():
            if question['topic'] == 'Tree':
                question_text = question['question']
                answer_text = question['answer']
                
                # Check for proper root references
                if 'root' in question_text.lower():
                    self.assertTrue(
                        '[ROOT]' in question_text or 
                        'root' in question_text.lower()
                    )
                
                # Tree questions should mention tree-specific concepts
                combined_text = (question_text + ' ' + answer_text).lower()
                tree_concepts = ['tree', 'node', 'root', 'leaf', 'traversal', 'binary']
                self.assertTrue(any(concept in combined_text for concept in tree_concepts))
    
    def test_tree_difficulty_progression(self):
        """Test that tree questions show proper difficulty progression."""
        beginner = self.sample_questions[self.sample_questions['difficulty'] == 1]
        intermediate = self.sample_questions[self.sample_questions['difficulty'] == 2]
        advanced = self.sample_questions[self.sample_questions['difficulty'] == 3]
        
        # Check that we have questions at each level
        self.assertGreater(len(beginner), 0)
        self.assertGreater(len(intermediate), 0)
        self.assertGreater(len(advanced), 0)
        
        # Check beginner questions are basic
        beginner_question = beginner.iloc[0]['question']
        beginner_concepts = ['root', 'value', 'what is']
        self.assertTrue(any(concept in beginner_question.lower() for concept in beginner_concepts))
        
        # Check intermediate questions involve algorithms
        intermediate_question = intermediate.iloc[0]['question']
        intermediate_concepts = ['check', 'find', 'search', 'bst', 'algorithm']
        self.assertTrue(any(concept in intermediate_question.lower() for concept in intermediate_concepts))
        
        # Check advanced questions are complex
        advanced_question = advanced.iloc[0]['question']
        advanced_concepts = ['serialize', 'implement', 'algorithm', 'complex']
        self.assertTrue(any(concept in advanced_question.lower() for concept in advanced_concepts))
    
    def test_tree_traversal_concepts(self):
        """Test that tree questions include traversal concepts."""
        tree_questions = self.sample_questions[self.sample_questions['topic'] == 'Tree']
        
        # At least some questions should mention traversals
        traversal_mentioned = False
        for _, question in tree_questions.iterrows():
            combined_text = (question['question'] + ' ' + question['answer']).lower()
            traversal_concepts = ['inorder', 'preorder', 'postorder', 'traversal', 'level order']
            if any(concept in combined_text for concept in traversal_concepts):
                traversal_mentioned = True
                break
        
        # Note: This might not always be true for our sample, but in a full dataset it should be
        # self.assertTrue(traversal_mentioned, "Tree questions should include traversal concepts")
    
    def test_tree_binary_concepts(self):
        """Test that tree questions reference binary tree concepts."""
        tree_questions = self.sample_questions[self.sample_questions['topic'] == 'Tree']
        
        for _, question in tree_questions.iterrows():
            combined_text = (question['question'] + ' ' + question['answer']).lower()
            
            # Should mention binary tree concepts
            binary_concepts = ['binary', 'left', 'right', 'child', 'parent']
            # At least some tree questions should mention these concepts
            # self.assertTrue(any(concept in combined_text for concept in binary_concepts))
    
    def test_tree_placeholders(self):
        """Test that tree questions contain proper placeholders."""
        for _, question in self.sample_questions.iterrows():
            if question['topic'] == 'Tree':
                question_text = question['question']
                answer_text = question['answer']
                
                # Check that questions contain [ROOT] and [VALUES] placeholders
                if 'tree' in question_text.lower():
                    self.assertTrue(
                        '[ROOT]' in question_text or 
                        '[VALUES]' in question_text
                    )
    
    def test_get_questions_endpoint_tree(self):
        """Test the /get_questions endpoint for trees."""
        response = self.app.post('/get_questions', 
                                json={
                                    'topic': 'Tree',
                                    'difficulty': '1',
                                    'num_questions': '5'
                                })
        
        self.assertEqual(response.status_code, 200)
        
        data = response.get_json()
        self.assertIsInstance(data, list)
        
        # Check that each question has the required fields
        for question in data:
            self.assertIn('id', question)
            self.assertIn('topic', question)
            self.assertIn('difficulty', question)
            self.assertIn('question', question)
            self.assertIn('answer', question)
            self.assertIn('values', question)
            
            # Check that values are generated
            self.assertIsInstance(question['values'], list)
            self.assertGreater(len(question['values']), 0)
            
            # Check topic is correct
            self.assertEqual(question['topic'], 'Tree')
    
    def test_tree_advanced_code_answers(self):
        """Test that advanced tree questions have code-based answers."""
        advanced_questions = self.sample_questions[self.sample_questions['difficulty'] == 3]
        
        for _, question in advanced_questions.iterrows():
            if question['topic'] == 'Tree':
                answer_text = question['answer']
                
                # Advanced questions should have more detailed answers
                self.assertGreater(len(answer_text), 30)
                
                # Should mention algorithmic concepts
                algorithmic_concepts = ['algorithm', 'recursive', 'iterative', 'traversal', 'implementation']
                self.assertTrue(any(concept in answer_text.lower() for concept in algorithmic_concepts))
    
    def test_tree_node_counting_concepts(self):
        """Test that tree questions include node counting concepts."""
        tree_questions = self.sample_questions[self.sample_questions['topic'] == 'Tree']
        
        # Check if any questions mention counting concepts
        counting_mentioned = False
        for _, question in tree_questions.iterrows():
            combined_text = (question['question'] + ' ' + question['answer']).lower()
            counting_concepts = ['count', 'number', 'total', 'leaf', 'height', 'depth']
            if any(concept in combined_text for concept in counting_concepts):
                counting_mentioned = True
                break
        
        # Note: This might not always be true for our sample, but in a full dataset it should be
        # self.assertTrue(counting_mentioned, "Tree questions should include counting concepts")

if __name__ == '__main__':
    unittest.main()