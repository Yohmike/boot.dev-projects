import unittest

from src.htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(tag="<b>",value="text", children=None, props={"href": "https://www.google.com", "target": "_blank"})        
        self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")

class testLeaftNode(unittest.TestCase):
    def test_simple_tag(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")
    
    def test_no_tag(self):
        node = LeafNode(None, "This is text.")
        self.assertEqual(node.to_html(), "This is text.")
    
    def test_props_tag(self):
        node = LeafNode("a", "Click me!", props={"href": "https://www.google.com"}) 
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

class testParentNode(unittest.TestCase):
    def test_one_child(self):
        node = ParentNode([LeafNode(tag=None, value="This is text")], tag="p")
        self.assertEqual(node.to_html(), "<p>This is text</p>")
    
    def test_two_children(self):
        node = ParentNode([LeafNode(tag=None, value="This is text"), LeafNode(tag="i", value="This is italic text")], tag="p")
        self.assertEqual(node.to_html(), "<p>This is text<i>This is italic text</i></p>")
    
    def test_one_level_deep(self):
        leaf = LeafNode("b", "This is bold text")
        parent = ParentNode([leaf], "i")
        grandparent = ParentNode([parent], "p")
        self.assertEqual(grandparent.to_html(), "<p><i><b>This is bold text</b></i></p>")
    
    def test_two_level_deep(self):
        leaf = LeafNode("b", "This is bold text")
        parent = ParentNode([leaf], "i")
        grandparent = ParentNode([parent], "p")
        greatgrandparent = ParentNode([grandparent], "body")
        self.assertEqual(greatgrandparent.to_html(), "<body><p><i><b>This is bold text</b></i></p></body>")

if __name__ == "__main__":
    unittest.main()