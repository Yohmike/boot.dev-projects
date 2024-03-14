from src.textnode import TextNode, text_node_to_html_node


def main():
    node = TextNode("This is a text node", "bold", "https://www/boot/dev")
    print(node)
    print(text_node_to_html_node(node).to_html())

if __name__ == "__main__":
    main()