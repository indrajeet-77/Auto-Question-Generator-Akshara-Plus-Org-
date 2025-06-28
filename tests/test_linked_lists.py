import unittest
import sys
import os

# Add the parent directory to the path to import the app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app, generate_random_values, filter_questions
import pandas as pd

class TestLinkedListQuestions(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.app = app.test_client()
        self.app.testing = True
        
        # Sample linked list questions for testing
        self.sample_questions = pd.DataFrame([
            {
                'id': 1,
                'topic': 'Singly Linked List',
                'difficulty': 1,
                'question': 'Given a singly linked list with head [HEAD] and values [VALUES], what is the value of the head node?',
                'answer': 'The value of the head node is [HEAD].'
            },
            {
                'id': 2,
                'topic': 'Singly Linked List',
                'difficulty': 2,
                'question': 'Reverse a singly linked list with head [HEAD] and values [VALUES].',
                'answer': 'Use iterative approach with three pointers: prev, current, next.'
            },
            {
                'id': 3,
                'topic': 'Doubly Linked List',
                'difficulty': 1,
                'question': 'Given a doubly linked list with head [HEAD] and values [VALUES], what is the tail node value?',
                'answer': 'The tail node value is [TAIL]. In doubly linked list, tail.next is NULL.'
            },
            {
                'id': 4,
                'topic': 'Circular Linked List',
                'difficulty': 1,
                'question': 'Given a circular linked list with head [HEAD] and values [VALUES], what makes it circular?',
                'answer': 'The last node\'s next pointer points back to the head [HEAD] instead of NULL.'
            }
        ])
    
    def test_generate_random_values_singly_linked_list(self):
        """Test that random values are generated correctly for singly linked lists."""
        values = generate_random_values('Singly Linked List')
        
        # Check that values is a list
        self.assertIsInstance(values, list)
        
        # Check that the list has between 5-8 elements
        self.assertGreaterEqual(len(values), 5)
        self.assertLessEqual(len(values), 8)
        
        # Check that all values are integers between 1-99
        for value in values:
            self.assertIsInstance(value, int)
            self.assertGreaterEqual(value, 1)
            self.assertLessEqual(value, 99)
    
    def test_generate_random_values_doubly_linked_list(self):
        """Test that random values are generated correctly for doubly linked lists."""
        values = generate_random_values('Doubly Linked List')
        
        # Check that values is a list
        self.assertIsInstance(values, list)
        
        # Check that the list has between 5-8 elements
        self.assertGreaterEqual(len(values), 5)
        self.assertLessEqual(len(values), 8)
        
        # Check that all values are integers between 1-99
        for value in values:
            self.assertIsInstance(value, int)
            self.assertGreaterEqual(value, 1)
            self.assertLessEqual(value, 99)
    
    def test_generate_random_values_circular_linked_list(self):
        """Test that random values are generated correctly for circular linked lists."""
        values = generate_random_values('Circular Linked List')
        
        # Check that values is a list
        self.assertIsInstance(values, list)
        
        # Check that the list has between 5-8 elements
        self.assertGreaterEqual(len(values), 5)
        self.assertLessEqual(len(values), 8)
        
        # Check that all values are integers between 1-99
        for value in values:
            self.assertIsInstance(value, int)
            self.assertGreaterEqual(value, 1)
            self.assertLessEqual(value, 99)
    
    def test_filter_questions_singly_linked_list(self):
        """Test filtering singly linked list questions."""
        filtered = filter_questions(self.sample_questions, 'Singly Linked List', 1, 1)
        
        # Should return exactly 1 question
        self.assertEqual(len(filtered), 1)
        
        # Should be the correct question
        self.assertEqual(filtered[0]['topic'], 'Singly Linked List')
        self.assertEqual(filtered[0]['difficulty'], 1)
    
    def test_filter_questions_doubly_linked_list(self):
        """Test filtering doubly linked list questions."""
        filtered = filter_questions(self.sample_questions, 'Doubly Linked List', 1, 1)
        
        # Should return exactly 1 question
        self.assertEqual(len(filtered), 1)
        
        # Should be the correct question
        self.assertEqual(filtered[0]['topic'], 'Doubly Linked List')
        self.assertEqual(filtered[0]['difficulty'], 1)
    
    def test_filter_questions_circular_linked_list(self):
        """Test filtering circular linked list questions."""
        filtered = filter_questions(self.sample_questions, 'Circular Linked List', 1, 1)
        
        # Should return exactly 1 question
        self.assertEqual(len(filtered), 1)
        
        # Should be the correct question
        self.assertEqual(filtered[0]['topic'], 'Circular Linked List')
        self.assertEqual(filtered[0]['difficulty'], 1)
    
    def test_linked_list_question_structure(self):
        """Test that linked list questions have the correct structure."""
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
    
    def test_linked_list_head_tail_concepts(self):
        """Test that linked list questions properly reference head and tail concepts."""
        for _, question in self.sample_questions.iterrows():
            if 'Linked List' in question['topic']:
                question_text = question['question']
                answer_text = question['answer']
                
                # Check for proper head/tail references
                if 'head' in question_text.lower():
                    self.assertTrue(
                        '[HEAD]' in question_text or 
                        'head' in question_text.lower()
                    )
                
                if 'tail' in question_text.lower() or 'tail' in answer_text.lower():
                    self.assertTrue(
                        '[TAIL]' in answer_text or 
                        'tail' in answer_text.lower()
                    )
    
    def test_linked_list_type_specific_concepts(self):
        """Test that different linked list types have appropriate concepts."""
        singly_questions = self.sample_questions[
            self.sample_questions['topic'] == 'Singly Linked List'
        ]
        doubly_questions = self.sample_questions[
            self.sample_questions['topic'] == 'Doubly Linked List'
        ]
        circular_questions = self.sample_questions[
            self.sample_questions['topic'] == 'Circular Linked List'
        ]
        
        # Check singly linked list concepts
        for _, question in singly_questions.iterrows():
            # Should mention next pointers or single direction
            text = (question['question'] + ' ' + question['answer']).lower()
            self.assertTrue(
                'next' in text or 
                'head' in text or 
                'singly' in text
            )
        
        # Check doubly linked list concepts
        for _, question in doubly_questions.iterrows():
            # Should mention prev pointers or bidirectional
            text = (question['question'] + ' ' + question['answer']).lower()
            self.assertTrue(
                'prev' in text or 
                'doubly' in text or 
                'backward' in text or
                'bidirectional' in text
            )
        
        # Check circular linked list concepts
        for _, question in circular_questions.iterrows():
            # Should mention circular property
            text = (question['question'] + ' ' + question['answer']).lower()
            self.assertTrue(
                'circular' in text or 
                'circle' in text or 
                'points back' in text
            )
    
    def test_linked_list_difficulty_progression(self):
        """Test that linked list questions show proper difficulty progression."""
        beginner = self.sample_questions[self.sample_questions['difficulty'] == 1]
        intermediate = self.sample_questions[self.sample_questions['difficulty'] == 2]
        
        # Check that we have questions at different levels
        self.assertGreater(len(beginner), 0)
        
        # Check that intermediate questions are more complex
        if len(intermediate) > 0:
            intermediate_question = intermediate.iloc[0]['question']
            self.assertTrue(
                'reverse' in intermediate_question.lower() or 
                'algorithm' in intermediate_question.lower() or
                len(intermediate_question) > 60
            )
    
    def test_get_questions_endpoint_singly_linked_list(self):
        """Test the /get_questions endpoint for singly linked lists."""
        response = self.app.post('/get_questions', 
                                json={
                                    'topic': 'Singly Linked List',
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
            self.assertEqual(question['topic'], 'Singly Linked List')
    
    def test_get_questions_endpoint_doubly_linked_list(self):
        """Test the /get_questions endpoint for doubly linked lists."""
        response = self.app.post('/get_questions', 
                                json={
                                    'topic': 'Doubly Linked List',
                                    'difficulty': '1',
                                    'num_questions': '3'
                                })
        
        self.assertEqual(response.status_code, 200)
        
        data = response.get_json()
        self.assertIsInstance(data, list)
        
        # Check that each question has the required fields
        for question in data:
            self.assertEqual(question['topic'], 'Doubly Linked List')
    
    def test_get_questions_endpoint_circular_linked_list(self):
        """Test the /get_questions endpoint for circular linked lists."""
        response = self.app.post('/get_questions', 
                                json={
                                    'topic': 'Circular Linked List',
                                    'difficulty': '1',
                                    'num_questions': '3'
                                })
        
        self.assertEqual(response.status_code, 200)
        
        data = response.get_json()
        self.assertIsInstance(data, list)
        
        # Check that each question has the required fields
        for question in data:
            self.assertEqual(question['topic'], 'Circular Linked List')

if __name__ == '__main__':
    unittest.main()