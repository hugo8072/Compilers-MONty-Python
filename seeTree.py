import sys
from pathlib import Path
# Adicione o diretório de saída ao caminho de busca do Python
sys.path.append(str(Path(r'C:\Users\Hugo\Desktop\Compilador\output_dir')))

from antlr4 import FileStream, CommonTokenStream
from antlr4.tree.Tree import TerminalNodeImpl, ErrorNodeImpl
from antlr4.tree.Trees import Trees
from graphviz import Digraph
from MontyPythonLexer import MontyPythonLexer
from MontyPythonParser import MontyPythonParser

def main():
    # Garante que o caminho exista e cria se necessário
    output_dir = Path(r'C:\Users\Hugo\Desktop\Compilador\output_dir')
    if not output_dir.exists():
        output_dir.mkdir(parents=True)
    
    # Carrega o arquivo de teste com codificação UTF-8 e tratamento de erros
    try:
        input_stream = FileStream('test.mpy', encoding='utf-8')
    except FileNotFoundError:
        print("Erro: arquivo 'test.mpy' não encontrado.")
        return
    
    lexer = MontyPythonLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MontyPythonParser(stream)
    
    try:
        tree = parser.file_input()  # Gera a árvore de análise
    except Exception as e:
        print(f"Erro durante a análise: {e}")
        return
    
    if tree:  # Verifica se a árvore é válida
        visualize_tree(tree, parser.ruleNames, output_dir)
    else:
        print("Erro: Não foi possível gerar a árvore de análise.")

def visualize_tree(tree, ruleNames, output_dir):
    dot = Digraph(comment='ANTLR Parse Tree')  # Inicializa o gráfico
    node_count = 0

    def add_node(parent, child):
        nonlocal node_count
        child_id = str(node_count)
        
        label = None
        if isinstance(child, TerminalNodeImpl):
            label = child.getText()  # Obtém o texto para nós terminais
        elif isinstance(child, ErrorNodeImpl):
            return None  # Não adiciona nós de erro
        else:
            label = Trees.getNodeText(child, ruleNames)  # Obtém o texto para nós não-terminais
        
        # Adiciona um nó somente se o rótulo for válido e não estiver vazio
        if label and label.strip() and "<INVALID>" not in label:
            dot.node(child_id, label=label)
            if parent is not None:
                dot.edge(str(parent), child_id)
            node_count += 1
            return child_id
        else:
            return None  # Retorna None para nós inválidos ou vazios

    def build_graph(node, parent_id=None):
        current_id = add_node(parent_id, node)  # Adiciona o nó atual
        
        if current_id is not None:  # Apenas continua se o nó foi adicionado
            if hasattr(node, 'children') and node.children:  # Verifica se 'children' existe
                for child in node.children:
                    build_graph(child, current_id)  # Constrói o gráfico recursivamente
    
    # Adiciona o nó raiz e constrói a árvore
    root_id = add_node(None, tree)

    if root_id:  # Garante que um nó raiz válido foi adicionado
        if hasattr(tree, 'children') and tree.children:  # Garante que a árvore tenha filhos
            for child in tree.children:
                build_graph(child, root_id)  # Constrói o gráfico a partir da árvore de análise
    
    # Caminho do arquivo de saída
    output_file = output_dir / 'parse_tree'
    
    try:
        dot.render(str(output_file), view=True)  # Renderiza e visualiza a saída
    except Exception as e:
        print(f"Erro durante a renderização: {e}")

if __name__ == '__main__':
    main()
