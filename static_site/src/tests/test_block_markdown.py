import unittest

from src.block_markdown import markdown_to_blocks, block_to_block_type, \
    block_type_paragraph, block_type_heading, block_type_code, \
    block_type_quote, block_type_unordered_list, block_type_ordered_list, \
    convert_block_heading, convert_block_code, convert_block_quote, \
    convert_block_unordered_list, convert_block_ordered_list, \
    convert_block_paragraph, markdown_to_html_node

from src.htmlnode import ParentNode, LeafNode

class TestMarkdownToBlock(unittest.TestCase):
    def test_no_block(self):
        doc = "This block is alone"
        blocks = markdown_to_blocks(doc)
        self.assertEqual(blocks, [doc])

    def test_two_blocks(self):
        doc = "This is **bolded** paragraph\n" \
            "\n" \
            "This is another paragraph with *italic* text and `code` here\n" \
            "This is the same paragraph on a new line\n" \
            "\n" \
            "* This is a list\n" \
            "* with items"
        blocks = markdown_to_blocks(doc)
        self.assertEqual(blocks, [
            "This is **bolded** paragraph",
            "This is another paragraph with *italic* text and `code` here\n" \
            "This is the same paragraph on a new line",
            "* This is a list\n" \
            "* with items"
        ])

    def test_empty_blocks(self):
        doc = "This is **bolded** paragraph\n" \
            "\n" \
            "This is another paragraph with *italic* text and `code` here\n" \
            "This is the same paragraph on a new line\n" \
            "\n\n\n" \
            "* This is a list\n" \
            "* with items"
        blocks = markdown_to_blocks(doc)
        self.assertEqual(blocks, [
            "This is **bolded** paragraph",
            "This is another paragraph with *italic* text and `code` here\n" \
            "This is the same paragraph on a new line",
            "* This is a list\n" \
            "* with items"
        ])


class TestMarkdownBlockType(unittest.TestCase):
    def test_heading(self):
        doc = "### Heading"
        self.assertEqual(block_to_block_type(doc), block_type_heading)
    
    def test_code(self):
        doc = "``` print(Hello World)```"
        self.assertEqual(block_to_block_type(doc), block_type_code)
    
    def test_quote(self):
        doc = "> quote line1 \n> quote line 2"
        self.assertEqual(block_to_block_type(doc), block_type_quote)
    
    def test_unordered_list(self):
        doc = "* list item 1 \n- list item 2"
        self.assertEqual(block_to_block_type(doc), block_type_unordered_list)

    def test_ordered_list(self):
        doc = "1. list item 1 \n2. list item 2"
        self.assertEqual(block_to_block_type(doc), block_type_ordered_list)

    def test_paragraph(self):
        doc = "Just a normal paragraph"
        self.assertEqual(block_to_block_type(doc), block_type_paragraph)

class TestMarkdownBlockToHTMLNode(unittest.TestCase):
    def test_heading(self):
        doc = "### Heading"
        e_node = ParentNode([LeafNode(tag=None, value="Heading")], tag="h3")
        node = convert_block_heading(doc)
        self.assertEqual(node.to_html(), e_node.to_html())
    
    def test_code(self):
        doc = "``` print(Hello World)```"
        e_node = ParentNode(
            children=[ParentNode(
                children=[LeafNode(tag=None, value=" print(Hello World)")], 
                tag="code"
                )],
            tag="pre")
        node = convert_block_code(doc)
        self.assertEqual(node.to_html(), e_node.to_html())

    def test_quote(self):
        doc = "> quote line1\n> other line"
        e_node = ParentNode(
            children=[LeafNode(tag=None, value="quote line1 other line")], 
            tag="blockquote"
        )
        node = convert_block_quote(doc)
        self.assertEqual(node.to_html(), e_node.to_html())

    def test_unordered_list(self):
        doc = "* list item 1 \n- list item 2"
        e_node = ParentNode(
            children=[
                ParentNode(
                    children=[
                        LeafNode(tag=None, value="list item 1 "),
                    ],
                    tag="li"
                ), ParentNode(
                    children=[
                        LeafNode(tag=None, value="list item 2")],  
                    tag="li"
                )
            ],
            tag="ul"
        )
        node = convert_block_unordered_list(doc)
        self.assertEqual(node.to_html(), e_node.to_html())

    def test_ordered_list(self):
            doc = "1. list item 1 \n2. list item 2"
            e_node = ParentNode(
                children=[
                    ParentNode(
                        children=[
                            LeafNode(tag=None, value="list item 1 "),
                        ],
                        tag="li"
                    ), ParentNode(
                        children=[
                            LeafNode(tag=None, value="list item 2")],  
                        tag="li"
                    )
                ],
                tag="ol"
            )
            node = convert_block_ordered_list(doc)
            self.assertEqual(node.to_html(), e_node.to_html())

    def test_paragraph(self):
        doc = "Just a normal paragraph"
        e_node = ParentNode([LeafNode(tag=None, value=doc)], tag="p")
        node = convert_block_paragraph(doc)
        self.assertEqual(node.to_html(), e_node.to_html())


class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag</p></div>",
        )



if __name__ == "__main__":
    unittest.main()