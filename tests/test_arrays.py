import unittest
import sys
import os

# Add the parent directory to the path to import the app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app, generate_random_values, filter_questions, load_questions
import pandas as pd

class TestArrayQuestions(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.app = app.test_client()
        self.app.testing = True
        
        # Sample array questions for testing
        self.sample_questions = pd.DataFrame([
            {
                'id': 1,
                'topic': 'Array',
                'difficulty': 1,
                'question': 'Given an array [VALUES], what is the element at index 2?',
                'answer': 'The element at index 2 is [VALUE].'
            },
            {
                'id': 2,
                'topic': 'Array',
                'difficulty': 2,
                'question': 'Find the second largest element in array [VALUES].',
                'answer': 'The second largest element is [SECOND_MAX].'
            },
            {
                'id': 3,
                'topic': 'Array',
                'difficulty': 3,
                'question': 'Implement Kadane\'s algorithm for array [VALUES].',
                'answer': 'Use dynamic programming to find maximum subarray sum.'
            }
        ])
    
    def test_generate_random_values_array(self):
        """Test that random values are generated correctly for arrays."""
        values = generate_random_values('Array')
        
        # Check that values is a list
        self.assertIsInstance(values, list)
        
        # Check that the list has between 5-10 elements
        self.assertGreaterEqual(len(values), 5)
        self.assertLessEqual(len(values), 10)
        
        # Check that all values are integers between 1-99
        for value in values:
            self.assertIsInstance(value, int)
            self.assertGreaterEqual(value, 1)
            self.assertLessEqual(value, 99)
    
    def test_filter_questions_array_beginner(self):
        """Test filtering array questions for beginner level."""
        filtered = filter_questions(self.sample_questions, 'Array', 1, 1)
        
        # Should return exactly 1 question
        self.assertEqual(len(filtered), 1)
        
        # Should be the correct question
        self.assertEqual(filtered[0]['topic'], 'Array')
        self.assertEqual(filtered[0]['difficulty'], 1)
    
    def test_filter_questions_array_intermediate(self):
        """Test filtering array questions for intermediate level."""
        filtered = filter_questions(self.sample_questions, 'Array', 2, 1)
        
        # Should return exactly 1 question
        self.assertEqual(len(filtered), 1)
        
        # Should be the correct question
        self.assertEqual(filtered[0]['topic'], 'Array')
        self.assertEqual(filtered[0]['difficulty'], 2)
    
    def test_filter_questions_array_advanced(self):
        """Test filtering array questions for advanced level."""
        filtered = filter_questions(self.sample_questions, 'Array', 3, 1)
        
        # Should return exactly 1 question
        self.assertEqual(len(filtered), 1)
        
        # Should be the correct question
        self.assertEqual(filtered[0]['topic'], 'Array')
        self.assertEqual(filtered[0]['difficulty'], 3)
    
    def test_filter_questions_insufficient_questions(self):
        """Test filtering when there are insufficient questions."""
        # Request more questions than available
        filtered = filter_questions(self.sample_questions, 'Array', 1, 5)
        
        # Should return all available questions for that difficulty
        self.assertEqual(len(filtered), 1)
    
    def test_array_question_structure(self):
        """Test that array questions have the correct structure."""
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
    
    def test_array_difficulty_progression(self):
        """Test that array questions show proper difficulty progression."""
        beginner = self.sample_questions[self.sample_questions['difficulty'] == 1]
        intermediate = self.sample_questions[self.sample_questions['difficulty'] == 2]
        advanced = self.sample_questions[self.sample_questions['difficulty'] == 3]
        
        # Check that we have questions at each level
        self.assertGreater(len(beginner), 0)
        self.assertGreater(len(intermediate), 0)
        self.assertGreater(len(advanced), 0)
        
        # Check that advanced questions are more complex (contain code or algorithms)
        advanced_question = advanced.iloc[0]['question']
        self.assertTrue(
            'algorithm' in advanced_question.lower() or 
            'implement' in advanced_question.lower() or
            len(advanced_question) > 50
        )
    
    def test_array_question_placeholders(self):
        """Test that array questions contain proper placeholders."""
        for _, question in self.sample_questions.iterrows():
            question_text = question['question']
            answer_text = question['answer']
            
            # Check that questions contain [VALUES] placeholder
            if 'array' in question_text.lower():
                self.assertIn('[VALUES]', question_text)
    
    def test_get_questions_endpoint_array(self):
        """Test the /get_questions endpoint for arrays."""
        response = self.app.post('/get_questions', 
                                json={
                                    'topic': 'Array',
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

if __name__ == '__main__':
    unittest.main()