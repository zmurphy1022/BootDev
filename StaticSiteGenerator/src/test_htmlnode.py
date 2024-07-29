import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node=HTMLNode(props={"href": "https://www.google.com", "target": "_blank",})
        test_node=' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(),test_node)

    def test_repr_none(self):
        node=HTMLNode(props=None)
        test_repr=None
        self.assertEqual(node.props_to_html(),test_repr)

    def test_props_none(self):
        node=HTMLNode(props=None)
        test_node=' href="https://www.google.com" target="_blank"'
        self.assertNotEqual(node.props_to_html(),test_node)

    # def test_to_html(self):
    #     node=HTMLNode(NotImplementedError)
    #     with self.assertRaises() as err:
    #         node.to_html()
    #     result=err.exception
    #     self.assertEqual(result,NotImplementedError)      


if __name__ == "__main__":
    unittest.main()