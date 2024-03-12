from typing import Dict, List, Optional

class HTMLNode():
    def __init__(self, 
                 tag: Optional[str] = None, 
                 value: Optional[str] = None, 
                 children: Optional[List['HTMLNode']] = None, 
                 props: Optional[Dict[str,str]] = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self) -> None:
        raise NotImplemented("to_html not implemented")
    
    def props_to_html(self) -> str:
        if self.props is None:
            return ""
        else:
            elements = []
            for key in self.props:
                elements.append(f" {key}=\"{self.props[key]}\"")
            return  "".join(elements)
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag: str | None = None, 
                 value: str | None = None, 
                 props: Dict[str, str] | None = None) -> None:
        super().__init__(tag, value, None, props)
    
    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("No value for leaf node")
        if self.tag is not None:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        else:
            return f"{self.value}"
    
    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    

class ParentNode(HTMLNode):
    def __init__(self, 
                 children: List[HTMLNode],
                 tag: str | None = None, 
                 props: Dict[str, str] | None = None
                 ) -> None:
        super().__init__(tag=tag, value=None, children=children, props=props)
    
    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("No tag provided")
        if self.children is None:
            raise ValueError("ParentNode has no children, should this be a LeafNode?")
        child_tags = "".join([child.to_html() for child in self.children])
        return f"<{self.tag}{self.props_to_html()}>{child_tags}</{self.tag}>"

    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
        