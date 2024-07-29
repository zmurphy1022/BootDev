import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_repr_none(self):
        node=TextNode("This is a text node", "bold")
        test_repr="TextNode(This is a text node, bold)"
        self.assertEqual(node.__repr__(),test_repr)

    def test_repr_type(self):
        node=TextNode("This is a text node", "italic")
        test_repr="TextNode(This is a text node, bold)"
        self.assertNotEqual(node.__repr__(),test_repr)        


if __name__ == "__main__":
    unittest.main()