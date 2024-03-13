import re
from typing import List, Tuple
from textnode import TextNode, \
    text_type_text, text_type_image, text_type_link, \
    text_type_bold, text_type_italic, text_type_code

def split_nodes_delimiter(
        old_nodes: List[TextNode], 
        delimiter: str, 
        text_type: str
        ) -> List[TextNode]:
    new_nodes = []
    if not delimiter:
        return old_nodes
    for node in old_nodes:
        if not isinstance(node, TextNode) or \
            (isinstance(node, TextNode) and node.text_type != text_type_text):
            new_nodes.append(node)
        else:
            split_nodes = []
            text_to_split = node.text
            if text_to_split.count(delimiter) % 2 != 0:
                raise Exception(
                    f"closing delimiter \"{delimiter}\" not found \
                      for \"{text_to_split}\"")
            else:
                parts = text_to_split.split(delimiter)
                for i in range(0, len(parts)):
                    if i % 2 == 0:
                        if parts[i]:
                            split_nodes.append(
                                TextNode(parts[i], text_type_text)
                            )
                    else:
                        split_nodes.append(TextNode(parts[i], text_type))
            new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text:str) -> List[Tuple[str, str]]:
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text:str) -> List[Tuple[str, str]]:
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches

def split_nodes_image(old_nodes: List[TextNode]) -> List[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        else:
            split_nodes = []
            text_to_split = node.text
            images = extract_markdown_images(text_to_split)
            left = text_to_split
            for image_text, image_link in images:
                image_str = f"![{image_text}]({image_link})"
                try:
                    current, left = left.split(image_str, 1)
                except ValueError:
                    raise Exception("Imvalid markdown, check image tag")
                if current != "":
                    split_nodes.append(
                        TextNode(current, text_type_text)
                    )
                split_nodes.append(
                    TextNode(image_text, text_type_image, url=image_link)
                )
        if left:
            split_nodes.append(
                TextNode(left, text_type_text)
            )
        new_nodes.extend(split_nodes)
    return new_nodes


def split_nodes_link(old_nodes: List[TextNode]) -> List[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            
        else:
            split_nodes = []
            text_to_split = node.text
            links = extract_markdown_links(text_to_split)
            left = text_to_split
            for link_text, link_url in links:
                link_str = f"[{link_text}]({link_url})"
                try:
                    current, left = left.split(link_str, 1)
                except ValueError:
                    raise Exception("Invalid markdown, check link tag")
                if current != "":
                    split_nodes.append(
                        TextNode(current, text_type_text)
                    )
                split_nodes.append(
                    TextNode(link_text, text_type_link, url=link_url)
                )
            if left:
                split_nodes.append(
                    TextNode(left, text_type_text)
                )
            new_nodes.extend(split_nodes)
    return new_nodes


def text_to_textnodes(text: str) -> List[TextNode]:
    root_node = TextNode(text, text_type_text)
    nodes = split_nodes_delimiter([root_node], "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes