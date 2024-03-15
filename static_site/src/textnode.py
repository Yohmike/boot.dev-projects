from typing import Optional, List
from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

valid_text_types = [
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image
    ]


class TextNode:
    def __init__(self, text: str, text_type: str, url: Optional[str] = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, __value: object) -> bool:
        return self.text == __value.text and \
            self.text_type == __value.text_type and \
            self.url == __value.url
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    valid_types = {
        text_type_text: LeafNode(tag=None, value=text_node.text),
        text_type_bold: LeafNode(tag="b", value=text_node.text),
        text_type_italic: LeafNode(tag="i", value=text_node.text),
        text_type_code: LeafNode(tag="code", value=text_node.text),
        text_type_link: LeafNode(
            tag="a", value=text_node.text, props={"href": text_node.url}),
        text_type_image: LeafNode(
            tag="img", 
            value="", 
            props={"src": text_node.url, "alt": text_node.text})
    }
    if valid_types.get(text_node.text_type) is None:
        raise Exception(f"Invalid type :{text_node.text_type}")
    else:
        return valid_types[text_node.text_type]


