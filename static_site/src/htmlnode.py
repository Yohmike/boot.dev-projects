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
