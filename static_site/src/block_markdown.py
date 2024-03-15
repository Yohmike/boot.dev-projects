from typing import List

from htmlnode import HTMLNode, ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


def markdown_to_blocks(doc: str) -> List[str]:
    sections = doc.split("\n\n")
    sections = [s.strip() for s in sections if s]
    return sections


def check_heading(block: str) -> bool:
    if " " not in block:
        return False
    head, rest = block.split(" ", 1)
    return set(head) == set("#") and rest


def check_code(block: str) -> bool:
    return len(block) >= 6 and set(block[:3]) == set(block[-3:]) == set("`")


def check_quote(block: str) -> bool:
    lines = block.split("\n")
    for line in lines:
        if not line.startswith(">"):
            return False
    return True


def check_unordered_list(block: str) -> bool:
    lines = block.split("\n")
    for line in lines:
        if not (line.startswith("*") or line.startswith("-")):
            return False
    return True


def check_ordered_list(block: str) -> bool:
    lines = block.split("\n")
    for i, line in enumerate(lines, start=1):
        if not line.startswith(f"{i}."):
            return False
    return True


def block_to_block_type(block: str) -> str:
    if check_heading(block):
        return block_type_heading
    if check_code(block):
        return block_type_code
    if check_quote(block):
        return block_type_quote
    if check_unordered_list(block):
        return block_type_unordered_list
    if check_ordered_list(block):
        return block_type_ordered_list
    return block_type_paragraph


def convert_block_quote(block: str) -> HTMLNode:
    block_type = block_to_block_type(block)

    if block_type != block_type_quote:
        raise Exception("Can't convert block to quote")

    no_quotes = " ".join([s[2:] for s in block.split("\n")])
    children = [
        text_node_to_html_node(node) for node in text_to_textnodes(no_quotes)
    ]

    return ParentNode(children, tag="blockquote")


def convert_block_unordered_list(block: str) -> HTMLNode:
    block_type = block_to_block_type(block)

    if block_type != block_type_unordered_list:
        raise Exception("Can't convert block to unordered list")

    list_children = []
    for line in block.split("\n"):
        children = [
            text_node_to_html_node(node) for node in text_to_textnodes(line[2:])
        ]
        list_children.append(ParentNode(children, tag="li"))

    return ParentNode(list_children, tag="ul")


def convert_block_ordered_list(block: str) -> HTMLNode:
    block_type = block_to_block_type(block)

    if block_type != block_type_ordered_list:
        raise Exception("Can't convert block to ordered list")

    list_children = []
    for line in block.split("\n"):
        _, content = line.split(".", 1)
        children = [
            text_node_to_html_node(node) for node in \
                text_to_textnodes(content[1:])
        ]
        list_children.append(ParentNode(children, tag="li"))

    return ParentNode(list_children, tag="ol")


def convert_block_code(block: str) -> HTMLNode:
    block_type = block_to_block_type(block)

    if block_type != block_type_code:
        raise Exception("Can't convert block to code")

    children = [
        text_node_to_html_node(node) for node in text_to_textnodes(block[3:-3])
    ]
    code_node = ParentNode(children, tag="code")
    return ParentNode([code_node], tag="pre")


def convert_block_heading(block: str) -> HTMLNode:
    block_type = block_to_block_type(block)

    if block_type != block_type_heading:
        raise Exception("Can't convert block to heading")

    head, content = block.split(" ", 1)
    children = [
        text_node_to_html_node(node) for node in text_to_textnodes(content)
    ]

    return ParentNode(children, tag=f"h{head.count("#")}")


def convert_block_paragraph(block: str) -> HTMLNode:
    block_type = block_to_block_type(block)

    if block_type != block_type_paragraph:
        raise Exception("Can't convert block to paragraph")
    block = " ".join(block.split("\n"))
    children = [
        text_node_to_html_node(node) for node in text_to_textnodes(block)
    ]

    return ParentNode(children, tag="p")


def markdown_to_html_node(markdown:str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        
        if block_type == block_type_paragraph:
            children.append(convert_block_paragraph(block))
        if block_type == block_type_heading:
            children.append(convert_block_heading(block))
        if block_type == block_type_code:
            children.append(convert_block_code(block))
        if block_type == block_type_quote:
            children.append(convert_block_quote(block))
        if block_type == block_type_unordered_list:
            children.append(convert_block_unordered_list(block))
        if block_type == block_type_ordered_list:
            children.append(convert_block_ordered_list(block))
    parent = ParentNode(children=children, tag="div")

    return parent