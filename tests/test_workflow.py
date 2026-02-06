import unittest
from main import run_workflow

class TestMultiAgentSystem(unittest.TestCase):
    """Unit tests for the multi-agent system"""
    
    def test_workflow_execution(self):
        """Test that the workflow executes successfully"""
        query = "Explain the concept of machine learning"
        result = run_workflow(query)
        
        self.assertTrue(result.get("complete"))
        self.assertIsNotNone(result.get("research"))
        self.assertIsNotNone(result.get("analysis"))
        self.assertIsNotNone(result.get("coding"))
    
    def test_empty_query(self):
        """Test that the workflow handles empty queries"""
        query = ""
        result = run_workflow(query)
        
        self.assertTrue(result.get("complete"))
        self.assertIsNotNone(result.get("research"))
        self.assertIsNotNone(result.get("analysis"))
        self.assertIsNotNone(result.get("coding"))
    
    def test_complex_query(self):
        """Test that the workflow handles complex queries"""
        query = "Explain quantum computing and its applications in cryptography"
        result = run_workflow(query)
        
        self.assertTrue(result.get("complete"))
        self.assertIsNotNone(result.get("research"))
        self.assertIsNotNone(result.get("analysis"))
        self.assertIsNotNone(result.get("coding"))


if __name__ == "__main__":
    unittest.main()