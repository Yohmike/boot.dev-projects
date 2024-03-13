import unittest

from textnode import TextNode, \
    text_type_bold, text_type_text, text_type_italic, text_type_code, \
    text_type_image, text_type_link

from inline_markdown import split_nodes_delimiter,\
    extract_markdown_images, extract_markdown_links, \
    split_nodes_image, split_nodes_link

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
        node = TextNode("this is very **bold bold** and **bold**", text_type_text)
        nodes = split_nodes_delimiter([node], "**", text_type_bold)
        expected_nodes = [
            TextNode("this is very ", text_type_text),
            TextNode("bold bold", text_type_bold),
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
        self.assertEqual(nodes, expected_nodes)


class TestExtractFunctions(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) \
            and ![another](https://i.imgur.com/dfsdkjfd.png)"
        markdown = extract_markdown_images(text)
        self.assertEqual(
            markdown,
            [("image", "https://i.imgur.com/zjjcJKZ.png"), 
             ("another", "https://i.imgur.com/dfsdkjfd.png")
            ]
        )
    
    def test_extract_markdown_links(self):
        text = "This is text with a [link](https://www.example.com) \
            and [another](https://www.example.com/another)"
        markdown = extract_markdown_links(text)
        self.assertEqual(
            markdown,
            [("link", "https://www.example.com"), 
             ("another", "https://www.example.com/another")
             ])

class TextSplitNodesImage(unittest.TestCase):
    def test_simple_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
        text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes,[
            TextNode("This is text with an ", text_type_text),
            TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
        ])

    def test_multiple_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) "
                "and another ![second image](https://i.imgur.com/3elNhQu.png)",
        text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes,[
            TextNode("This is text with an ", text_type_text),
            TextNode("image", text_type_image, 
                     "https://i.imgur.com/zjjcJKZ.png"
            ),
            TextNode(" and another ", text_type_text),
            TextNode(
                "second image", text_type_image, 
                "https://i.imgur.com/3elNhQu.png"
            ),
        ])

class TextSplitNodesLinks(unittest.TestCase):
    def test_simple_link(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png)",
        text_type_text,
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes,[
            TextNode("This is text with an ", text_type_text),
            TextNode("link", text_type_link, "https://i.imgur.com/zjjcJKZ.png"),
        ])

    def test_multiple_links(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) "
                "and another [second link](https://i.imgur.com/3elNhQu.png)",
        text_type_text,
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes,[
            TextNode("This is text with an ", text_type_text),
            TextNode("link", text_type_link, 
                     "https://i.imgur.com/zjjcJKZ.png"
            ),
            TextNode(" and another ", text_type_text),
            TextNode(
                "second link", text_type_link, 
                "https://i.imgur.com/3elNhQu.png"
            ),
        ])


if __name__ == "__main__":
    unittest.main()