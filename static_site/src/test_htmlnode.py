import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(tag="<b>",value="text", children=None, props={"href": "https://www.google.com", "target": "_blank"})        
        self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")
    

if __name__ == "__main__":
    unittest.main()