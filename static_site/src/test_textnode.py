import unittest

from textnode import TextNode, split_nodes_delimiter, \
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

class TestSplitNodes(unittest.TestCase):
    def test_simple_node(self):
        node = TextNode("This is a text node", text_type_text)
        nodes = split_nodes_delimiter([node], "", text_type_text)
        self.assertEqual(nodes, [node])
    
    def test_simple_bold(self):
        node = TextNode("This is a **bold** textnode", text_type_text)
        nodes = split_nodes_delimiter([node], "**", text_type_bold)
        expected_nodes = [
            TextNode("This is a ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" textnode", text_type_text)
        ]
        self.assertEqual(nodes, expected_nodes)

    def test_starts_with_bold(self):
        node = TextNode("**bold** textnode", text_type_text)
        nodes = split_nodes_delimiter([node], "**", text_type_bold)
        expected_nodes = [
            TextNode("bold", text_type_bold),
            TextNode(" textnode", text_type_text)
        ]
        self.assertEqual(nodes, expected_nodes)

    def test_ends_with_bold(self):
        node = TextNode("this is very **bold**", text_type_text)
        nodes = split_nodes_delimiter([node], "**", text_type_bold)
        expected_nodes = [
            TextNode("this is very ", text_type_text),
            TextNode("bold", text_type_bold)
        ]
        self.assertEqual(nodes, expected_nodes)
    
    def test_multiple_types(self):
        node = TextNode("this is very **bold** and **bold**", text_type_text)
        nodes = split_nodes_delimiter([node], "**", text_type_bold)
        expected_nodes = [
            TextNode("this is very ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" and ", text_type_text),
            TextNode("bold", text_type_bold)
        ]
        self.assertEqual(nodes, expected_nodes)
    
    def test_multiple_different_types(self):
        node = TextNode(
            "this is very **bold** and *italic* and `code`", text_type_text
            )
        nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertEqual(nodes, [
            TextNode("this is very ", text_type_text),
            TextNode("bold", text_type_bold), 
            TextNode(" and *italic* and `code`", text_type_text)
            ])
        nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
        self.assertEqual(nodes, [
            TextNode("this is very ", text_type_text),
            TextNode("bold", text_type_bold), 
            TextNode(" and ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" and `code`", text_type_text)
            ])
        nodes = split_nodes_delimiter(nodes, "`", text_type_code)
        expected_nodes = [
            TextNode("this is very ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" and ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" and ", text_type_text),
            TextNode("code", text_type_code),
        ]
        #self.assertEqual(nodes, expected_nodes)
    
    
    
if __name__ == "__main__":
    unittest.main()