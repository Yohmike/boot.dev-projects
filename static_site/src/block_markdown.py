from typing import List

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
    head, rest = block.split(" ", 1)
    return set(head) == set("#") and rest


def check_code(block: str) -> bool:
    return len(block) >= 6 and set(block[:2]) == set(block[-2:]) == set("`")


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


def block_to_block_type(block: List[str]) -> str:
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