import sys

from antlr4 import *
from antlr4.tree.Trees import Trees

from output_dir.MontyPythonLexer import MontyPythonLexer
from output_dir.MontyPythonParser import MontyPythonParser

from tac_generator import generate_TAC  # Importing the function to generate TAC

sys.path.append(r'C:\output_dir')


def main():
    input_file = 'test.mpy'  # Input file
    input_stream = FileStream(input_file, encoding='utf-8')
    lexer = MontyPythonLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MontyPythonParser(stream)
    tree = parser.file_input()

    # Generate and print the AST
    print("AST:")
    print(Trees.toStringTree(tree, None, parser))

    # Generate and print the TAC
    # tac = generate_TAC(tree,1)
    tac = generate_TAC(tree, 3)


if __name__ == '__main__':
    main()
