import unittest

from block_markdown import markdown_to_blocks, block_to_block_type, \
    block_type_paragraph, block_type_heading, block_type_code, \
    block_type_quote, block_type_unordered_list, block_type_ordered_list


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
        doc = "* list item 1 \n- liist item 2"
        self.assertEqual(block_to_block_type(doc), block_type_unordered_list)

    def test_ordered_list(self):
        doc = "1. list item 1 \n2. list item 2"
        self.assertEqual(block_to_block_type(doc), block_type_ordered_list)

    def test_paragraph(self):
        doc = "Just a normal paragraph"
        self.assertEqual(block_to_block_type(doc), block_type_paragraph)


if __name__ == "__main__":
    unittest.main()