import unittest

from textnode import TextNode, \
    text_type_bold, text_type_text, text_type_italic, text_type_code


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertEqual(node, node2)
    
    def test_neq_text(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is another text node", text_type_bold)
        self.assertNotEqual(node, node2)
    
    def test_neq_type(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_italic)
        self.assertNotEqual(node, node2)
    
    def test_neq_url(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode(
            "This is a text node", text_type_bold, url="www.google.com"
            )
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()