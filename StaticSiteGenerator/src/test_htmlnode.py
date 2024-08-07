import unittest

from htmlnode import HTMLNode,LeafNode,ParentNode

class TestParentNode(unittest.TestCase):
    def test_no_tag(self):
        node=ParentNode(tag=None,children=[LeafNode("b", "Bold text",None),LeafNode(None, "Normal text",None),LeafNode("i", "italic text",None),LeafNode(None, "Normal text",None)],props=None)
        with self.assertRaises(ValueError):
            node.to_html()

    def no_children(self):
        node=ParentNode(tag="p",children=None,props=None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_base_case(self):
        node=ParentNode(tag="p",children=[LeafNode("b", "Bold text",None),LeafNode(None, "Normal text",None),LeafNode("i", "italic text",None),LeafNode(None, "Normal text",None)],props=None)
        test_result="<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(),test_result)
    
    def test_nested_parent(self):
        children=[LeafNode("b", "Bold text",None),LeafNode(None, "Normal text",None),LeafNode("i", "italic text",None),LeafNode(None, "Normal text",None),ParentNode(tag="p",children=[LeafNode("b", "Bold text",None),LeafNode(None, "Normal text",None),LeafNode("i", "italic text",None),LeafNode(None, "Normal text",None)],props=None)]
        node=ParentNode(tag="p",children=children,props=None)
        test_result="<p><b>Bold text</b>Normal text<i>italic text</i>Normal text<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></p>"
        self.assertEqual(node.to_html(),test_result)
        




class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node=HTMLNode(props={"href": "https://www.google.com", "target": "_blank",})
        test_node=' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(),test_node)

    def test_repr_none(self):
        node=HTMLNode(props=None)
        test_repr=None
        self.assertNotEqual(node.props_to_html(),test_repr)

    def test_props_none(self):
        node=HTMLNode(props=None)
        test_node=' href="https://www.google.com" target="_blank"'
        self.assertNotEqual(node.props_to_html(),test_node)

   
class TestLeafNode(unittest.TestCase):
    def test_value_required(self):
        node=LeafNode(tag=None,value=None,props=None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_no_props(self):
        node=LeafNode(tag='a',value='Click me!',props=None)
        test_html='<a>Click me!</a>'
        self.assertEqual(node.to_html(),test_html)

    def test_with_props(self):
        node=LeafNode(tag='a',value='Click me!',props={"href": "https://www.google.com", "target": "_blank",})
        test_html='<a href="https://www.google.com" target="_blank">Click me!</a>'
        self.assertEqual(node.to_html(),test_html)

if __name__ == "__main__":
    unittest.main()