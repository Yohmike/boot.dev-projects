from typing import Optional
from htmlnode import LeafNode


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
    

def text_node_to_html_node(text_node):
    valid_types = {
        "text": LeafNode(tag=None, value=text_node.text),
        "bold": LeafNode(tag="b", value=text_node.text),
        "italic": LeafNode(tag="i", value=text_node.text),
        "code": LeafNode(tag="code", value=text_node.text),
        "link": LeafNode(tag="a", value=text_node.text, props={"href":text_node.url}),
        "image": LeafNode(tag="img", value=None, props={"src": text_node.url, "alt": text_node.text})
    }
    if valid_types.get(text_node.text_type) is None:
        raise Exception(f"Invalid type :{text_node.text_type}")
    else:
        return valid_types[text_node.text_type]
