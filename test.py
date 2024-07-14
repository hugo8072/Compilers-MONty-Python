import sys
# Note: Use a raw string for the path to avoid escape character issues
sys.path.append(r'C:\Users\Hugo\Desktop\Compilador\output_dir')

from antlr4 import *
from output_dir.MontyPythonLexer import MontyPythonLexer
from output_dir.MontyPythonParser import MontyPythonParser
from antlr4.tree.Trees import Trees
from tac_generator import generate_TAC  # Importando a função para gerar o TAC

def main():
    input_file = 'test.mpy'  # Arquivo de entrada
    input_stream = FileStream(input_file, encoding='utf-8')
    lexer = MontyPythonLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MontyPythonParser(stream)
    tree = parser.file_input()

    # Gerar e imprimir a árvore AST
    print("AST:")
    print(Trees.toStringTree(tree, None, parser))

    # Gerar e imprimir a árvore TAC
    #tac = generate_TAC(tree,1)
    tac= generate_TAC(tree,3)

if __name__ == '__main__':
    main()
