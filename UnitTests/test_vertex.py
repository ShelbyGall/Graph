import sys
sys.path.append('./')

import unittest

import Vertex as V

class TestVertex(unittest.TestCase):
    def test_vetex_label(self):
        v = V.Vertex("Vertex 1")
        self.assertEqual(v.label, "Vertex 1")
        self.assertEqual(v.get_label(), "Vertex 1")

    def test_vertex_data(self):
        v = V.Vertex(label="Vertex 1", data={'data':1} )
        self.assertIsInstance(v.data, dict)
        self.assertIsInstance(v.get_data(), dict)

    def test_vertex_str(self):
        v = V.Vertex(label="Vertex 1", data={'data':1} )
        self.assertEqual(str(v),"Vertex 1|{'data': 1}")

if __name__ == "__main__":
    unittest.main(verbosity=2)