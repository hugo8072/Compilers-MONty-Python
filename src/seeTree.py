import sys
from pathlib import Path

from antlr4 import FileStream, CommonTokenStream
from antlr4.tree.Tree import TerminalNodeImpl, ErrorNodeImpl
from antlr4.tree.Trees import Trees

from graphviz import Digraph

from MontyPythonLexer import MontyPythonLexer
from MontyPythonParser import MontyPythonParser

# Add the output directory to the Python search path
sys.path.append(str(Path('C:/output_dir')))


def main():
    """
    Main function to parse the input file and visualize the parse tree.
    """
    # Ensure the path exists and create it if necessary
    output_dir = Path('C:/output_dir')
    if not output_dir.exists():
        output_dir.mkdir(parents=True)

    # Load the test file with UTF-8 encoding and error handling
    try:
        input_stream = FileStream('test.mpy', encoding='utf-8')
    except FileNotFoundError:
        print("Error: 'test.mpy' file not found.")
        return

    lexer = MontyPythonLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MontyPythonParser(stream)

    try:
        tree = parser.file_input()  # Generate the parse tree
    except Exception as e:
        print(f"Error during parsing: {e}")
        return

    if tree:  # Check if the tree is valid
        visualize_tree(tree, parser.ruleNames, output_dir)
    else:
        print("Error: Could not generate the parse tree.")


def visualize_tree(tree, ruleNames, output_dir):
    """
    Visualizes the parse tree using Graphviz.

    Args:
        tree: The parse tree to visualize.
        ruleNames: The list of rule names from the parser.
        output_dir: The directory to save the output file.
    """
    dot = Digraph(comment='ANTLR Parse Tree')  # Initialize the graph
    node_count = 0

    def add_node(parent, node):
        nonlocal node_count
        child_id = str(node_count)

        if isinstance(node, TerminalNodeImpl):
            label = child.getText()  # Get the text for terminal nodes
        elif isinstance(node, ErrorNodeImpl):
            return None  # Do not add error nodes
        else:
            label = Trees.getNodeText(node, ruleNames)  # Get the text for non-terminal nodes

        # Add a node only if the label is valid and not empty
        if label and label.strip() and "<INVALID>" not in label:
            dot.node(child_id, label=label)
            if parent is not None:
                dot.edge(str(parent), child_id)
            node_count += 1
            return child_id
        else:
            return None  # Return None for invalid or empty nodes

    def build_graph(node, parent_id=None):
        current_id = add_node(parent_id, node)  # Add the current node

        if current_id is not None:  # Continue only if the node was added
            if hasattr(node, 'children') and node.children:  # Check if 'children' exists
                for child in node.children:
                    build_graph(child, current_id)  # Recursively build the graph

    # Add the root node and build the tree
    root_id = add_node(None, tree)

    if root_id:  # Ensure a valid root node was added
        if hasattr(tree, 'children') and tree.children:  # Ensure the tree has children
            for child in tree.children:
                build_graph(child, root_id)  # Build the graph from the parse tree

    # Output file path
    output_file = output_dir / 'parse_tree'

    try:
        dot.render(str(output_file), view=True)  # Render and view the output
    except Exception as e:
        print(f"Error during rendering: {e}")


if __name__ == '__main__':
    main()
