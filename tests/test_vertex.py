import sys
import unittest

import Vertex as V

class TestVertex(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.full_vertex = V.Vertex(label="Full", data={'data':1} )
        cls.empty_vertex = V.Vertex(label="Empty")

    # Testing Vertices where the data attribute is populated
    # Testing what happens where the full vertex is initialized
    def test_vertex_full_init(self):
        self.assertIsInstance(self.full_vertex, V.Vertex)
        self.assertTrue(hasattr(self.full_vertex, "label"))

    # Testing vertex label for the full vertex
    def test_full_vertex_label(self):
        self.assertIsInstance(self.full_vertex.label, str)
        self.assertEqual(self.full_vertex.label, "Full")
        self.assertEqual(self.full_vertex.get_label(), "Full")

    # Testing vertex data for the full vertex
    def test_full_vertex_data(self):
        self.assertTrue(hasattr(self.full_vertex, "data"))
        self.assertIsInstance(self.full_vertex.data, dict)
        self.assertIsInstance(self.full_vertex.get_data(), dict)
        self.assertEqual(self.full_vertex.data.get('data'), 1)

    # Testing vertex string representation
    def test_full_vertex_str(self):
        self.assertEqual(str(self.full_vertex),"Full|{'data': 1}")


    # Testing Vertices where the data attribute is NOT populated
    # Testing what happens where the empty vertex is initialized
    def test_vertex_empty_init(self):
        self.assertIsInstance(self.empty_vertex, V.Vertex)
        self.assertTrue(hasattr(self.empty_vertex, "label"))

    # Testing vertex label for the empty vertex
    def test_empty_vertex_label(self):
        self.assertIsInstance(self.empty_vertex.label, str)
        self.assertEqual(self.empty_vertex.label, "Empty")
        self.assertEqual(self.empty_vertex.get_label(), "Empty")

    # Testing vertex data for the empty vertex
    def test_empty_vertex_data(self):
        self.assertTrue(hasattr(self.empty_vertex, "data"))
        self.assertIsNone(self.empty_vertex.get_data())

    # Testing vertex string representation
    def test_empty_vertex_str(self):
        self.assertEqual(str(self.empty_vertex),"Empty|None")

if __name__ == "__main__":
    unittest.main()