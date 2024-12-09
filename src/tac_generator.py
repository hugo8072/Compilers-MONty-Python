from antlr4 import *
from output_dir.MontyPythonLexer import MontyPythonLexer
from output_dir.MontyPythonParser import MontyPythonParser
from output_dir.MontyPythonParserVisitor import MontyPythonParserVisitor


class TACGenerator(MontyPythonParserVisitor):
    """
    A class to generate Three Address Code (TAC) from a MontyPython parse tree.

    Attributes:
        tac (list): The list to store TAC instructions.
        temp_count (int): Counter for temporary variables.
        label_count (int): Counter for labels.
        int_vars (list): List to track integer variables.
        float_vars (list): List to track float variables.
        initialized_lists (set): Set to track initialized lists.
        initialized_variables (set): Set to track initialized variables.
        functions (dict): Dictionary to store function definitions.
    """

    def __init__(self):
        """
        Initializes the TACGenerator with empty lists and counters.
        """
        self.tac = []
        self.temp_count = 0
        self.label_count = 0  # Zé- Contador para rótulos
        self.int_vars = []  # RP Lista para rastrear variáveis de tipo int
        self.float_vars = []  # RP Lista para rastrear variáveis de tipo float
        self.initialized_lists = set()
        self.initialized_variables = set()
        self.functions = {}

    def get_int_vars(self):
        #   print("aqui")
        #   print(self.int_vars)
        return self.int_vars

    def get_float_vars(self):
        #  print("aqui2")
        #  print(self.float_vars)
        return self.float_vars

    def new_temp(self):
        """
        Generates a new temporary variable.

        Returns:
            str: The name of the new temporary variable.
        """
        self.temp_count += 1
        return f"t{self.temp_count}"

    def new_label(self):
        """
        Generates a new label.

        Returns:
            str: The name of the new label.
        """
        self.label_count += 1  # Zé
        return f"L{self.label_count}"  # Zé

    def add_function(self, function_name, function):
        """
        Adds a function to the functions dictionary.

        Args:
            function_name (str): The name of the function.
            function (str): The function definition.
        """
        self.functions[function_name] = function  # Adiciona a função ao dicionário

    # RP atribui o tipo à variavel
    def set_var_type(self, var_name, var_type):
        """
        Sets the type of a variable.

        Args:
            var_name (str): The name of the variable.
            var_type (str): The type of the variable.
        """
        if var_type == "int":
            if var_name not in self.int_vars:
                self.int_vars.append(var_name)
            if var_name in self.float_vars:
                self.float_vars.remove(var_name)
        elif var_type == "float":
            if var_name not in self.float_vars:
                self.float_vars.append(var_name)
            if var_name in self.int_vars:
                self.int_vars.remove(var_name)

    # RP retorna o tipo da variavel
    def get_var_type(self, var_name):
        """
        Gets the type of a variable.

        Args:
            var_name (str): The name of the variable.

        Returns:
            str: The type of the variable.
        """
        if var_name in self.int_vars:
            return "int"
        elif var_name in self.float_vars:
            return "float"
        else:
            return None

    # RP 31/05 confirma se variavel é usada em loop
    def is_used_in_condition_or_loop(self, var):
        """
        Checks if a variable is used in a condition or loop.

        Args:
            var (str): The variable to check.

        Returns:
            bool: True if the variable is used in a condition or loop, False otherwise.
        """
        for instr in self.tac:  # RP 31/05
            if isinstance(instr, str):  # RP 31/05
                if (f"if False {var}" in instr or f"if {var}" in instr or
                        f"goto {var}" in instr or f"while {var}" in instr or
                        f"for {var}" in instr):  # RP 31/05
                    return True  # RP 31/05
        return False  # RP 31/05

    # RP 31/05 extrai variavel do tac
    @staticmethod
    def extract_variables(expression):
        """
        Extracts variables from an expression.

        Args:
            expression (str): The expression to extract variables from.

        Returns:
            list: The list of extracted variables.
        """
        import re
        expression = str(expression)
        if expression is None:
            return set()
        if isinstance(expression, tuple):
            expression = ' '.join(expression)
        return set(re.findall(r'\b\w+\b', expression))

    def visitFile_input(self, ctx):
        """
        Visits the file input context and generates TAC.

        Args:
            ctx: The file input context.

        Returns:
            list: The generated TAC.
        """
        for stmt in ctx.stmt():
            self.visit(stmt)
        return self.tac

    def visitStmt(self, ctx):
        """
        Visits a statement context and generates TAC.

        Args:
            ctx: The statement context.

        Returns:
            list: The generated TAC.
        """
        if ctx.simple_stmt():
            self.visit(ctx.simple_stmt())
        elif ctx.compound_stmt():
            self.visit(ctx.compound_stmt())
        elif ctx.function():
            self.visit(ctx.function())
        return self.tac

    def visitSimple_stmt(self, ctx):
        """
        Visits a simple statement context and generates TAC.

        Args:
            ctx: The simple statement context.

        Returns:
            list: The generated TAC.
        """
        if ctx.small_stmt():
            self.visit(ctx.small_stmt())
        return self.tac

    def visitSmall_stmt(self, ctx):
        """
        Visits a small statement context and generates TAC.

        Args:
            ctx: The small statement context.

        Returns:
            list: The generated TAC.
        """
        if ctx.expr_stmt():
            self.visit(ctx.expr_stmt())
        elif ctx.list_stmt():
            self.visit(ctx.list_stmt())
        elif ctx.list_op():
            self.visit(ctx.list_op())
        elif ctx.print_stmt():
            self.visit(ctx.print_stmt())
        elif ctx.functions_stmt():
            self.visit(ctx.functions_stmt())
        return self.tac

    def visitPrint_stmt(self, ctx):
        """
        Visits a print statement context and generates TAC.

        Args:
            ctx: The print statement context.

        Returns:
            list: The generated TAC.
        """
        print_args = []
        current_arg = []
        for child in ctx.children[1:]:  # Ignora o 'print'
            text = child.getText()
            if text == ',':
                if current_arg:
                    print_args.append(''.join(current_arg).strip())
                    current_arg = []
            elif text not in {'(', ')'}:
                current_arg.append(text)

        # Adiciona o último argumento, se houver
        if current_arg:
            print_args.append(''.join(current_arg).strip())

        processed_args = []
        for arg in print_args:
            # print(arg)
            if arg.startswith('"') and arg.endswith('"'):
                # É uma string
                processed_args.append(arg)
            elif '(' in arg and ')' in arg:
                # Pode ser uma função, verificar se está definida
                func_name = arg.split('(')[0]
                if func_name in self.functions:
                    # processed_args.append(arg)
                    var_name1 = arg.split('(')[1].split(')')[0]
                    # print(var_name)

                    variable_found1 = False
                    for var_name in self.initialized_variables:

                        if f"{var_name}" == f"{var_name1}":
                            processed_args.append(arg)
                            variable_found1 = True
                            break  # Sai do loop se a variável for encontrada

                    for list_name in self.initialized_lists:
                        if f"{list_name}" == f"{var_name1}":
                            processed_args.append(arg)
                            variable_found1 = True
                            break  # Sai do loop se a variável for encontrada

                    if not variable_found1:
                        error_message = f'Error: variable "{var_name1}" is not defined.'
                        self.tac.append(f'print_error("{error_message}")')

                else:
                    # Função não definida, mensagem de erro
                    error_message = f'Error: function "{func_name}" is not defined.'
                    self.tac.append(f'print_error("{error_message}")')
                    continue
            else:
                # Verificar se a variável existe
                variable_found = False
                for var_name in self.initialized_variables:
                    if f"{var_name}" == f"{arg}":
                        processed_args.append(arg)
                        variable_found = True
                        break  # Sai do loop se a variável for encontrada

                if not variable_found:
                    # Variável não definida, mensagem de erro
                    error_message = f'Error: variable "{arg}" is not defined.'
                    self.tac.append(f'print_error("{error_message}")')
                    continue

        if len(processed_args) == 1:
            print_statement = f'print({processed_args[0]})'
        else:
            print_statement = 'print(' + ', '.join(processed_args) + ')'

        self.tac.append(print_statement)
        return self.tac

    def visitExpr_stmt(self, ctx):
        """
        Visits an expression statement context and generates TAC.

        Args:
            ctx: The expression statement context.

        Returns:
            list: The generated TAC.
        """
        first_word = ctx.getChild(0).getText()
        if first_word in ["int", "float"]:
            # Verificação para declaração de variáveis sem atribuição direta
            if ctx.getChildCount() == 2:  # Verifica se é uma declaração sem atribuição
                var_name = ctx.getChild(1).getText()
                self.initialized_variables.add(var_name)
                self.set_var_type(var_name, first_word)  # Define o tipo da variável
                if first_word == "int":
                    self.add_to_tac(var_name, "0")

                else:
                    self.add_to_tac(var_name, "0.0")

            elif ctx.getChild(3).getChild(0) and ctx.getChild(3).getChild(
                    0).getText() == "input":  # Verifica se o lado direito é uma função de input
                var_name = ctx.getChild(1)
                self.visitInput_func(ctx.getChild(3))  # Passa o nome da variável
                self.initialized_variables.add(var_name)
            else:
                self.handle_explicit_type_declaration(ctx, first_word)

        elif ctx.getChild(2).getText().startswith("size"):
            self.handle_size_operation(ctx)
        else:

            var_name = ctx.getChild(0).getText()

            if ctx.getChild(2).getChild(0).getText() == "input":  # Verifica se o lado direito é uma função de input
                self.visitInput_func(ctx.getChild(2))  # Passa o nome da variável
                self.initialized_variables.add(var_name)
            else:
                self.handle_implicit_type_declaration(ctx)
                return self.tac

        if ctx.getChildCount() > 2 and ctx.getChild(0).getText() == 'return':
            return_var = ctx.getChild(2).getText()
            if return_var not in self.initialized_variables:
                raise ValueError(f"Variável {return_var} não inicializada")

        return self.tac

    def handle_size_operation(self, ctx):
        """
        Handles size operations and generates TAC.

        Args:
            ctx: The size operation context.

        Returns:
            list: The generated TAC.
        """
        declaration_text = ctx.getText()
        var_name = ctx.getChild(0).getText()
        list_name = declaration_text[7:-1]
        self.add_to_tac(var_name, f"{list_name}.length")

    def handle_implicit_type_declaration(self, ctx):
        """
        Handles implicit type declarations and generates TAC.

        Args:
            ctx: The implicit type declaration context.

        Returns:
            list: The generated TAC.
        """

        var_name = ctx.getChild(0).getText()

        expression = ctx.getChild(2)

        # se não tiver tipo, coloca float
        self.set_var_type(var_name, 'float') if self.get_var_type(var_name) is None else None
        var_type = self.get_var_type(var_name)
        if self.is_expression(expression):

            # confirma o tipo, se não especificado ou int, é float
            value = self.visitExpr(expression, var_type)

            self.set_var_type(value, 'float') if self.get_var_type(value) is None else None
            # print(value, value_type, var_name, var_type)
            # faz cast
            # if var_type != value_type:# RP  31/05
            #    value = f"{var_type}({value})"# RP  31/05
        else:
            # print("entra 70")
            value = None
            if ctx.expr():
                value = self.visitExpr(expression, var_type)
            elif ctx.term():
                value = self.visitTerm(expression, var_type)
            elif ctx.factor():
                value = self.visitFactor(expression, var_type)
            elif ctx.primary():
                value = self.visitPrimary(expression, var_type)
            self.set_var_type(value, 'float') if self.get_var_type(value) is None else None
            # print(var_name, var_type, value, value_type)
            # if var_type != value_type:  # RP  31/05
            #    value = f"{var_type}({value})"  # RP  31/05

        if self.is_list(value):
            self.add_to_tac(var_name, value)
            self.initialized_variables.add(var_name)
        if self.is_int(value) or self.is_float(value):  # RP garante que é int ou float antes de colocar.0
            self.add_to_tac(var_name, self.format_value(value, var_type))
            self.initialized_variables.add(var_name)
        # else:
        # self.add_to_tac(var_name, value)
        else:
            self.add_to_tac(var_name, value)
            self.initialized_variables.add(var_name)

    def handle_explicit_type_declaration(self, ctx, var_type):
        """
        Handles explicit type declarations and generates TAC.

        Args:
            ctx: The explicit type declaration context.
            var_type (str): The type of the variable.

        Returns:
            list: The generated TAC.
        """
        declaration_text = ctx.getText()
        variables = declaration_text[len(var_type):].split(',')
        for var in variables:
            var = var.strip()
            if '=' in var:
                var_name, value = var.split('=')
                var_name = var_name.strip()
                value = self.format_value(value.strip(), var_type)
                self.add_to_tac(var_name, value)
            else:
                var_name = var.strip()
                if var_type == "int":
                    self.add_to_tac(var_name, "0")
                else:
                    self.add_to_tac(var_name, "0.0")
            self.set_var_type(var_name, var_type)  # RP Definir tipo da variável
            self.initialized_variables.add(var_name)  # Marcar a variável como inicializada

    @staticmethod
    def format_value(value, var_type):
        """
        Formats a value according to its type.

        Args:
            value (str): The value to format.
            var_type (str): The type of the variable.

        Returns:
            str: The formatted value.
        """
        if 'e' in value.lower():
            value = "{:.10f}".format(float(value))
        if var_type == "float" and '.' not in value:
            value = f"{value}.0"
        return value

    def add_to_tac(self, var_name, value):
        """
        Adds a variable and its value to the TAC.

        Args:
            var_name (str): The name of the variable.
            value (str): The value of the variable.
        """
        self.tac.append((var_name, value))

    # percorre o TAC e retira instruções de variaveis não usadas
    def tac_optimization(self):
        """
        Optimizes the TAC by removing unused variables.
        """
        live_vars = set()  # RP 31/05
        tac_reversed = list(reversed(self.tac))  # RP 31/05
        filtered_tac = []  # RP 31/05

        for instr in tac_reversed:  # RP 31/05 percorre o tac em reverso
            if isinstance(instr, tuple) and len(instr) == 2:  # RP 31/05
                var, value = instr  # RP 31/05
                used_vars = self.extract_variables(value)  # RP 31/05 extrai variaveis usadas
                if var.startswith('t'):  # RP 31/05 variaveis temporarias

                    if var in live_vars or var in used_vars:  # RP 31/05 se live ou usadas noutro momento
                        filtered_tac.append(instr)  # RP 31/05
                        live_vars.add(var)  # RP 31/05
                        live_vars.update(used_vars)  # RP 31/05
                else:  # RP 31/05
                    filtered_tac.append(instr)  # RP 31/05
                    live_vars.add(var)  # RP 31/05
                    live_vars.update(used_vars)  # RP 31/05
            elif isinstance(instr, str):  # RP 31/05
                filtered_tac.append(instr)  # RP 31/05
                live_vars.update(self.extract_variables(instr))  # RP 31/05

        filtered_tac.reverse()  # RP 31/05
        self.tac = filtered_tac  # RP 31/05

    def is_list(self, value):
        """
        Checks if a value is a list.

        Args:
            value (str): The value to check.

        Returns:
            bool: True if the value is a list, False otherwise.
        """
        if not isinstance(value, str):
            return False

        if '[' not in value or ']' not in value:
            return False

        name_part, element_part = value.split('[', 1)
        element_part = element_part.rstrip(']')

        if not name_part.isidentifier():
            return False

        if element_part.isdigit() or self.is_float(element_part) or element_part.isidentifier():
            return True

        return False

    @staticmethod
    def is_expression(ctx):
        """
        Checks if a context is an expression.

        Args:
            ctx: The context to check.

        Returns:
            bool: True if the context is an expression, False otherwise.
        """
        # Verifica se o contexto tem mais de um filho
        if ctx.getChildCount() > 1:
            return 1
        # Verifica se há exatamente um filho
        elif ctx.getChildCount() == 1:
            first_child = ctx.getChild(0)

            # print(f'Tipo do filho único: {type(first_child)}, Filho único: {first_child}')
            # Verifica se o filho único tem mais de um componente
            if hasattr(first_child, 'getChildCount') and first_child.getChildCount() > 1:
                # print("entra 101")
                return 1
            elif isinstance(first_child, list) and len(first_child) > 1:
                # print("entra 104")
                return 1
            elif hasattr(first_child, 'children') and len(first_child.children) > 1:
                # print("entra 107")
                return 1
        # print("entra 97")
        return 0

    @staticmethod
    def is_float(value):
        """
        Checks if a value is a float.

        Args:
            value (str): The value to check.

        Returns:
            bool: True if the value is a float, False otherwise.
        """
        try:
            float(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_int(value):
        """
        Checks if a value is an integer.

        Args:
            value (str): The value to check.

        Returns:
            bool: True if the value is an integer, False otherwise.
        """

        try:
            int(value)
            return '.' not in value and 'e' not in value.lower()
        except ValueError:
            return False

    def visitExpr(self, ctx, dest_type=None):
        """
        Visits an expression context and generates TAC.

        Args:
            ctx: The expression context.
            dest_type (str, optional): The destination type.

        Returns:
            str: The temporary variable holding the result.
        """
        # print("entra 103")
        cast_int = False
        if ctx.getChildCount() == 1:
            # print("entra 104")
            var = self.visit(ctx.getChild(0))
            # if not var.startswith('t') and var not in self.initialized_variables and not var.isdigit():
            # raise ValueError(f"Variável {var} não inicializada")

            return var
        else:
            # print("entra 107")
            left = self.visit(ctx.getChild(0))
            # if left not in self.initialized_variables and not left.isdigit():
            # raise ValueError(f"Variável {left} não inicializada")
            for i in range(1, ctx.getChildCount(), 2):
                # print("entra 336",left)
                op = ctx.getChild(i).getText()
                right = self.visit(ctx.getChild(i + 1))
                if left in {'0', '0.0'}:  # RP 31/05
                    left = right  # RP 31/05
                    continue  # RP 31/05
                if right in {'0', '0.0'}:  # RP 31/05
                    continue  # RP 31/05
                temp, cast_int = self.handle_type_and_conversion(left, right, op, dest_type)  # RP 31/05
                left = temp
            return f"int({left})" if cast_int is True else left  # RP 31/05

    def visitTerm(self, ctx, dest_type=None):
        """
        Visits a term context and generates TAC.

        Args:
            ctx: The term context.
            dest_type (str, optional): The destination type.

        Returns:
            str: The temporary variable holding the result.
        """
        # print("entra 120")
        if ctx.getChildCount() == 1:
            var = self.visit(ctx.getChild(0))
            # if var not in self.initialized_variables and not var.isdigit():
            #   raise ValueError(f"Variável {var} não inicializada")
            return var
        else:
            # print("entra 123")
            left = self.visit(ctx.getChild(0))
            # if left not in self.initialized_variables and not left.isdigit():
            #   raise ValueError(f"Variável {left} não inicializada")
            for i in range(1, ctx.getChildCount(), 2):
                op = ctx.getChild(i).getText()
                right = self.visit(ctx.getChild(i + 1))
                if left in {'0', '0.0'}:  # RP 31/05
                    continue  # RP 31/05
                if right in {'0', '0.0'}:  # RP 31/05
                    left = right
                    continue  # RP 31/05
                if left in {'1', '1.0'}:  # RP 31/05
                    left = right  # RP 31/05
                    continue  # RP 31/05
                if right in {'1', '1.0'}:  # RP 31/05
                    continue  # RP 31/05
                temp, _ = self.handle_type_and_conversion(left, right, op, dest_type)  # RP 31/05
                left = temp

            return left

    def visitEnd_function(self, ctx):
        """
        Visits an end function context and generates TAC.

        Args:
            ctx: The end function context.

        Returns:
            list: The generated TAC.
        """
        if ctx.getChildCount() > 1 and ctx.getChild(0).getText() == 'return':
            return_expression = ctx.getChild(1).getText()
            if return_expression.isdigit():
                self.tac.append(f"return {return_expression}")
                return return_expression
            else:
                self._validate_return_expression(return_expression)
                self.tac.append(f"return {return_expression}")
                return return_expression

    def _validate_return_expression(self, expr):
        """
        Validates a return expression.

        Args:
            expr (str): The return expression to validate.

        Returns:
            bool: True if the expression is valid, False otherwise.
        """
        tokens = self._tokenize_expression(expr)
        for token in tokens:
            if not self._is_valid_token(token):
                raise ValueError(f"Variável ou função não inicializada ou inválida: {token}")

    @staticmethod
    def _tokenize_expression(expr):
        """
        Tokenizes an expression.

        Args:
            expr (str): The expression to tokenize.

        Returns:
            list: The list of tokens.
        """
        # Simplesmente divide a expressão em tokens separados por espaços e caracteres especiais
        tokens = []
        current_token = ''
        i = 0
        while i < len(expr):
            if expr[i:i + 5] == 'size(':
                if current_token:
                    tokens.append(current_token.strip())
                    current_token = ''
                end_index = expr.find(')', i)
                tokens.append(expr[i:end_index + 1].strip())
                i = end_index + 1
            elif expr[i] in '/*+-':
                if current_token:
                    tokens.append(current_token.strip())
                    current_token = ''
                tokens.append(expr[i])
                i += 1
            elif expr[i] == '(':
                if current_token:
                    tokens.append(current_token.strip())
                    current_token = ''
                balance = 1
                j = i + 1
                while j < len(expr) and balance > 0:
                    if expr[j] == '(':
                        balance += 1
                    elif expr[j] == ')':
                        balance -= 1
                    j += 1
                tokens.append(expr[i:j].strip())
                i = j
            elif expr[i] == ' ':
                if current_token:
                    tokens.append(current_token.strip())
                    current_token = ''
                i += 1
            else:
                current_token += expr[i]
                i += 1
        if current_token:
            tokens.append(current_token.strip())
        return tokens

    def _is_valid_token(self, token):
        """
        Checks if a token is valid.

        Args:
            token (str): The token to check.

        Returns:
            bool: True if the token is valid, False otherwise.
        """
        if token in '/*+-':
            return True
        if token.isdigit():  # Validar inteiros
            return True
        if token.startswith("size(") and token.endswith(")"):
            list_var = token[5:-1]
            return all(var.strip() in self.initialized_lists for var in list_var.split(','))
        elif token.startswith("(") and token.endswith(")"):
            inner_expression = token[1:-1].strip()
            return self._validate_expression(inner_expression)
        elif '(' in token and ')' in token:
            inner_expression = token[token.find('(') + 1:token.rfind(')')].strip()
            function_name = token[:token.find('(')].strip()
            if function_name not in self.functions:
                return False
            return self._validate_expression(inner_expression)
        else:
            return token in self.initialized_variables or token in self.functions

    def _validate_expression(self, expr):
        """
        Validates an expression.

        Args:
            expr (str): The expression to validate.

        Returns:
            bool: True if the expression is valid, False otherwise.
        """
        tokens = self._tokenize_expression(expr)
        for token in tokens:
            if not self._is_valid_token(token):
                return False
        return True

    def visitFactor(self, ctx, dest_type=None):
        """
        Visits a factor context and generates TAC.

        Args:
            ctx: The factor context.
            dest_type (str, optional): The destination type.

        Returns:
            str: The temporary variable holding the result.
        """
        # print("entra 135")
        if ctx.getChildCount() == 1:
            var = self.visit(ctx.getChild(0))
            # if var not in self.initialized_variables and not var.isdigit():
            # raise ValueError(f"Variável {var} não inicializada")
            return var
        else:
            left = self.visit(ctx.getChild(0))
            # if left not in self.initialized_variables and not left.isdigit():
            # raise ValueError(f"Variável {left} não inicializada")
            # left_type = self.get_var_type(left)  # RP tipo
            leftinicial = self.visit(ctx.getChild(0))
            for i in range(1, ctx.getChildCount(), 2):
                op = ctx.getChild(i).getText()
                if op == '**':  # RP Se for **
                    try:  # RP ve se é int
                        exponent = int(ctx.getChild(i + 1).getText())
                        is_variable = False
                    except ValueError:  # RP senão, visita
                        exponent = self.visitPrimary(ctx.getChild(i + 1))
                        is_variable = True
                    if not is_variable:
                        if exponent == 0:  # RP caso especial expoente 0, retorna sempre 1
                            return f"1"
                        elif exponent <= 5:  # RP se o expoente for até 5, menos linhas sem loop, senão usa loop para
                            # poupar linhas de código
                            a = 1
                            while a < exponent:
                                temp = self.new_temp()
                                self.tac.append((temp, f"{left} * {leftinicial}"))
                                left = temp
                                a = a + 1
                            return left
                        else:
                            label_start = self.new_label()
                            label_end = self.new_label()
                            result = self.new_temp()
                            temp = self.new_temp()
                            base = self.new_temp()

                            self.tac.append((result, f"1"))
                            self.tac.append((temp, f"{exponent}"))
                            self.tac.append((base, f"{left}"))
                            self.tac.append((label_start, None))  # RP final como imprimir TAC trata do :, colocado None
                            # RP Loop positivo
                            self.tac.append(f"if {temp} <= 0 goto {label_end}")
                            self.tac.append((result, f"{result} * {base}"))
                            self.tac.append((temp, f"{temp} - 1"))
                            self.tac.append(f"goto {label_start}")
                            self.tac.append((label_end, None))  # RP final como imprimir TAC trata do :, colocado None
                            left = result
                        return left
                    else:
                        label_start = self.new_label()
                        label_expoente_neg = self.new_label()
                        label_negative = self.new_label()
                        label_end_negative = self.new_label()
                        label_end = self.new_label()
                        result = self.new_temp()
                        temp = self.new_temp()
                        base = self.new_temp()
                        # inicializa
                        self.tac.append((result, f"1"))
                        self.tac.append((temp, f"{exponent}"))
                        self.tac.append((base, f"{left}"))

                        self.tac.append(f"if {temp} < 0 goto {label_expoente_neg}")  # RP salto negativo
                        self.tac.append((label_start, None))  # RP final como imprimir TAC trata do :, colocado None
                        # RP Loop positivo
                        self.tac.append(f"if {temp} == 0 goto {label_end}")
                        self.tac.append((result, f"{result} * {base}"))
                        self.tac.append((temp, f"{temp} - 1"))
                        self.tac.append(f"goto {label_start}")
                        # RP se negativo
                        self.tac.append(
                            (label_expoente_neg, None))  # RP final como imprimir TAC trata do :, colocado None
                        self.tac.append((temp, f"- {temp}"))

                        # Loop negativo
                        self.tac.append((label_negative, None))  # RP final como imprimir TAC trata do :, colocado None
                        self.tac.append(f"if {temp} == 0 goto {label_end_negative}")
                        self.tac.append((result, f"{result} * {base}"))
                        self.tac.append((temp, f"{temp} - 1"))
                        self.tac.append(f"goto {label_negative}")
                        self.tac.append(
                            (label_end_negative, None))  # RP final como imprimir TAC trata do :, colocado None
                        self.tac.append((result, f"1 / {result}"))
                        self.tac.append((label_end, None))  # RP final como imprimir TAC trata do :, colocado None
                        left = result
                    return left

                right = self.visit(ctx.getChild(i + 1))
                if right not in self.initialized_variables and not right.isdigit():
                    raise ValueError(f"Variável {right} não inicializada")
                temp, _ = self.handle_type_and_conversion(left, right, op, dest_type)  # RP 31/05
                left = temp

            return left

    def visitPrimary(self, ctx, dest_type=None):
        """
        Visits a primary context and generates TAC.

        Args:
            ctx: The primary context.
            dest_type (str, optional): The destination type.

        Returns:
            str: The temporary variable holding the result.
        """
        if ctx.NAME():
            return ctx.NAME(0).getText()
            # if var not in self.initialized_variables:
            # raise ValueError(f"Variável {var} não inicializada")

        elif ctx.LIST_VALUE():
            return ctx.LIST_VALUE().getText()
        elif ctx.INT():
            return ctx.INT().getText()
        elif ctx.FLOAT():
            return ctx.FLOAT().getText()
        elif ctx.STRING():
            return ctx.STRING().getText()
        elif ctx.expr():
            return self.visit(ctx.expr())
        elif ctx.getChildCount() == 2:
            sign = ctx.getChild(0).getText()
            primary = self.visit(ctx.getChild(1))
            temp = self.new_temp()
            self.tac.append((temp, f"{sign}{primary}"))
            return temp

        elif ctx.input_func():
            return self.visitInput_func(ctx.input_func())

    def visitInput_func(self, ctx):
        """
        Visits an input function context and generates TAC.

        Args:
            ctx: The input function context.

        Returns:
            list: The generated TAC.
        """
        var_name = ctx.NAME().getText()
        prompt = self.visit(ctx.arg())
        self.tac.append((var_name, f"input({prompt})"))  # Directly use the given variable
        return var_name

    def visitArg(self, ctx):
        """
        Visits an argument context and generates TAC.

        Args:
            ctx: The argument context.

        Returns:
            str: The argument text.
        """
        # This method assumes that arg can be either a STRING or another expression
        if ctx.STRING():
            return ctx.STRING(0).getText()  # Access the first element of the list
        else:
            return self.visit(ctx.expr())

    def visitPrimary_int(self, ctx):
        return ctx.getText()

    def visitPrimary_float(self, ctx):
        return ctx.getText()

    @staticmethod
    def visitTerminal(node):
        return node.getText()

    def visitList_stmt(self, ctx):
        """
        Visits a list statement context and generates TAC.

        Args:
            ctx: The list statement context.

        Returns:
            list: The generated TAC.
        """
        declaration_text = ctx.getText()
        array = []

        if '=' in declaration_text:
            var_name, values = declaration_text.split('=')
            if 'int[]' in var_name:
                var_name = var_name[5:].strip()
                values = values.strip()[1:-1]
                value_list = values.split(',')
                for i in value_list:
                    try:
                        array.append(int(i))
                    except ValueError:
                        print("ERRO: Somente é possível números int em lista de int.")
                self.int_vars.append(var_name)
            elif 'float[]' in var_name:
                var_name = var_name[7:].strip()
                values = values.strip()[1:-1]
                value_list = values.split(',')
                for i in value_list:
                    try:
                        array.append(float(i))
                    except ValueError:
                        print("ERRO: Somente é possível números int e float em lista de float.")
                self.float_vars.append(var_name)
            else:
                var_name = var_name.strip()
                values = values.strip()[1:-1]
                value_list = values.split(',')
                for i in value_list:
                    array.append(float(i))
            self.add_to_tac(var_name, array)
            self.initialized_lists.add(var_name)

        else:
            var_name = declaration_text.strip()
            value = '[]'
            if 'int[]' in var_name:
                var_name = var_name[5:].strip()
            elif 'float[]' in var_name:
                var_name = var_name[7:].strip()
            self.add_to_tac(var_name, value)
            self.initialized_lists.add(var_name)

        return self.tac

    def visitList_op(self, ctx):
        """
        Visits a list operation context and generates TAC.

        Args:
            ctx: The list operation context.

        Returns:
            list: The generated TAC.
        """
        declaration_text = ctx.getText()
        if 'add' in declaration_text:
            param = declaration_text[4:-1].split(',')
            list_name = param[0].strip()
            if list_name not in self.initialized_lists:
                raise ValueError(f"Lista {list_name} não inicializada")

            index_str = param[1].strip()
            if not index_str.isdigit() and index_str not in self.initialized_variables:
                raise ValueError(f"Índice {index_str} não inicializado")

            value_str = param[2].strip()
            if not value_str.isdigit() and value_str not in self.initialized_variables:
                raise ValueError(f"Valor {value_str} não inicializado")

            new_value = value_str

            loop_label = self.new_label()
            end_label = self.new_label()
            len_temp = self.new_temp()
            index_temp = self.new_temp()
            last_index_temp = self.new_temp()
            last_index_value_temp = self.new_temp()
            new_len_temp = self.new_temp()
            incr_len_temp = self.new_temp()

            # Store the length of the list
            self.add_to_tac(len_temp, f"{list_name}.length")

            if index_str.isdigit():
                self.add_to_tac(index_temp, index_str)  # If it's a constant, store the constant in index_temp
            else:
                self.add_to_tac(index_temp, index_str)  # If it's a variable, store the variable in index_temp

            # Calculate the last index of the list
            self.add_to_tac(last_index_temp, f"{len_temp} - 1")

            # Label for the start of the loop
            self.add_to_tac(loop_label, "None")

            # If the index is greater than the size, go to the end
            self.tac.append(f"if {last_index_temp} < {index_temp} goto {end_label}")

            # Start from the end of the list
            self.add_to_tac(last_index_value_temp, f"{list_name}[{last_index_temp}]")

            # Move the element to the right
            self.add_to_tac(f"{list_name}[{last_index_temp} + 1]", last_index_value_temp)

            # Continue the loop if not reached the index i
            self.tac.append(f"goto {loop_label}")

            # Label for the end of the loop
            self.add_to_tac(end_label, "None")

            # Insert the new value at position i
            self.add_to_tac(f"{list_name}[{index_temp}]", new_value)

            # Store the current length
            self.add_to_tac(new_len_temp, f"{list_name}.length")

            # Increment the length of the list
            self.add_to_tac(incr_len_temp, f"{new_len_temp} + 1")

            # Update the length of the list
            self.add_to_tac(f"{list_name}.length", incr_len_temp)

        elif 'remove' in declaration_text:
            param = declaration_text[7:-1].split(',')
            list_name = param[0].strip()
            if list_name not in self.initialized_lists:
                raise ValueError(f"Lista {list_name} não inicializada")

            index_value = param[1].strip()
            # if index_value not in self.initialized_variables:
            # print("835")
            if not index_value.isdigit() and index_value not in self.initialized_variables:
                raise ValueError(f"Índice {index_value} não inicializado")

            loop_label = self.new_label()
            end_label = self.new_label()
            error_label = self.new_label()
            len_temp = self.new_temp()
            index_temp = self.new_temp()
            next_index_temp = self.new_temp()
            loop_temp = self.new_temp()
            current_len_temp = self.new_temp()
            new_len_temp = self.new_temp()

            # Store the length of the list
            self.add_to_tac(len_temp, f"{list_name}.length")

            if index_value.isdigit():
                self.add_to_tac(index_temp, index_value)  # If it's a constant, store the constant in index_temp
            else:
                self.add_to_tac(index_temp, index_value)  # If it's a variable, store the variable in index_temp

            # Check if the index is out of bounds
            self.tac.append(f"if {index_temp} >= {len_temp} goto {error_label}")
            self.tac.append(f"if {index_temp} < 0 goto {error_label}")  # Ensure the index is non-negative

            # Loop to shift elements
            self.add_to_tac(loop_label, "None")
            self.tac.append(f"if {index_temp} >= {len_temp} - 1 goto {end_label}")
            self.add_to_tac(next_index_temp, f"{index_temp} + 1")
            self.add_to_tac(loop_temp, f"{list_name}[{next_index_temp}]")
            self.add_to_tac(f"{list_name}[{index_temp}]", loop_temp)
            self.add_to_tac(index_temp, next_index_temp)
            self.tac.append(f"goto {loop_label}")

            # Update the list length
            self.add_to_tac(end_label, "None")
            self.add_to_tac(current_len_temp, f"{list_name}.length")
            self.add_to_tac(new_len_temp, f"{current_len_temp} - 1")
            self.add_to_tac(f"{list_name}.length", new_len_temp)
            self.tac.append(f"goto {end_label}")

            # Error handling for invalid index
            self.add_to_tac(error_label, "None")
            self.tac.append("print ERRO: Indice invalido para remocao")

        elif 'size' in declaration_text:
            list_name = declaration_text[5:-1].strip()
            if list_name not in self.initialized_lists:
                raise ValueError(f"Lista {list_name} não inicializada")

            temp = self.new_temp()
            self.add_to_tac(temp, f"{list_name}.length")

        elif '=' in declaration_text:
            list_name = ctx.getChild(0).getText()
            if ctx.getChildCount() > 3:
                left = ctx.getChild(2).getText()
                right = ctx.getChild(4).getText()
                op = ctx.getChild(3).getText()
                self.add_to_tac(list_name, f"{left} {op} {right}")
            else:
                self.add_to_tac(ctx.getChild(0), ctx.getChild(2))

    def initialize_list(self, list_name):
        self.initialized_lists.add(list_name)
        self.initialized_variables.add(list_name)  # Supondo que a lista também é tratada como uma variável

    def initialize_variable(self, variable_name):
        self.initialized_variables.add(variable_name)

    # Zé ate ao fim, da linha
    # Implementação das estruturas IF, ELSE e WHILE

    def visitFor_stmt(self, ctx):
        loop_var = ctx.getChild(1).getText()  # Acessa o nome da variável de loop

        if ctx.getChildCount() == 6:  # se sao 6 args é sinal que é for in list (nao me perguntem pq sao 6 e nao 5)

            iter_expr = ctx.getChild(3)

            # print(f"loop_var: {loop_var}, iter_expr: {iter_expr}, suite_result: {ctx.suite()}")
            self.visit_variable_for(loop_var, iter_expr, ctx.suite())

        elif ctx.getChildCount() == 9:  # hugo-entra no primeiro caso do range
            # Chama visit_range_for se houver 8 filhos
            # print("aiaiaia")
            iter_start = 0
            iter_expr = ctx.getChild(5).getText()
            iter_incr = 1
            # if isinstance(iter_expr, str):
            #   print("Texto de iter_expr:", iter_expr)
            # print("Tipo de iter_expr:", type(iter_expr))
            # print(f"loop_var: {loop_var}, iter_expr: {iter_expr}, suite_result: {ctx.suite()}")
            self.visit_range_for(loop_var, iter_start, iter_expr, iter_incr, ctx.suite())

        elif ctx.getChildCount() == 11:

            iter_var_use = ctx.getChild(1).getText()

            self.initialized_variables.add(iter_var_use)

            iter_start = ctx.getChild(5).getText()

            iter_expr = ctx.getChild(7).getText()

            iter_incr = 1

            self.visit_range_for(loop_var, iter_start, iter_expr, iter_incr, ctx.suite())

        elif ctx.getChildCount() == 13:
            iter_start = ctx.getChild(5).getText()
            iter_expr = ctx.getChild(7).getText()
            iter_incr = ctx.getChild(9).getText()
            # print(iter_start, iter_expr, iter_incr)
            self.visit_range_for(loop_var, iter_start, iter_expr, iter_incr, ctx.suite())

        return self.tac

    def visit_range_for(self, iter_start, var_expr, iter_inc, suite, range_type):

        # print("entra aqui 329")
        list_temp = var_expr
        # print("entra aqui 331")
        index_temp = self.new_temp()

        if range_type == 1:
            self.tac.append((index_temp, "0"))

        if range_type == 2 or range_type == 3:
            self.tac.append((index_temp, iter_start))

        # print("entra 333")
        loop_label = self.new_label()
        end_label = self.new_label()

        self.tac.append((loop_label, None))
        # print("entra aqui 336")

        temp_cond = self.new_temp()

        self.tac.append((temp_cond, f"{index_temp} < {list_temp}"))
        self.tac.append(f"if {temp_cond} == 0 goto {end_label}")  # RP final removi o none

        loop_var = self.new_temp()

        self.tac.append((loop_var, f"{index_temp}"))
        # self.tac.append((loop_var, f"{temp_loop_var}"))

        # Corpo do loop

        self.visit(suite)

        temp_var = self.new_temp()

        self.tac.append((temp_var, f"{index_temp} + {iter_inc}"))
        self.tac.append(f"{index_temp} = {temp_var}")  # RP final faltava um espaço
        self.tac.append(f"goto {loop_label}")  # RP final removi o none
        self.tac.append((end_label, None))

    def visit_variable_for(self, loop_var, var_expr, suite):
        # print("entra aqui 329")
        list_temp = var_expr
        # print("entra aqui 331")
        index_temp = self.new_temp()
        self.tac.append((index_temp, "0"))
        # print("entra 333")
        loop_label = self.new_label()
        end_label = self.new_label()
        self.tac.append((loop_label, None))
        # print("entra aqui 336")

        temp_cond = self.new_temp()
        self.tac.append((temp_cond, f"{index_temp} < len({list_temp})"))
        self.tac.append(f"if {temp_cond} == 0 goto {end_label}")  # RP final removi o none

        self.tac.append((loop_var, f"{list_temp}[{index_temp}]"))

        # Corpo do loop

        self.visit(suite)

        self.tac.append((index_temp, f"{index_temp} + 1"))
        self.tac.append(f"goto {loop_label}")  # RP final removi o none
        self.tac.append((end_label, None))

    def visitIf_stmt(self, ctx):
        if ctx.logical_expr():
            condition = self.visit(ctx.logical_expr(0))
            # label_start = self.new_label()
            label_else = self.new_label()
            label_end = self.new_label()

            self.tac.append(f"if False {condition} goto {label_else}")  # RP final removi o none
            self.visit(ctx.getChild(3))  # RP final permitir suite_func, n forçando o suite
            self.tac.append(f"goto {label_end}")  # RP final removi o none
            self.tac.append((label_else, None))

            for i in range(1, len(ctx.logical_expr())):
                condition = self.visit(ctx.logical_expr(i))
                label_elif_else = self.new_label()
                self.tac.append(f"if False {condition} goto {label_elif_else}")  # RP final removi o none
                self.visit(ctx.getChild(i))
                self.tac.append(f"goto {label_end}")  # RP final removi o none
                self.tac.append((label_elif_else, None))

            if ctx.ELSE():
                self.visit(ctx.getChild(6))

            self.tac.append((label_end, None))

        return self.tac

    def visitWhile_stmt(self, ctx):
        label_start = self.new_label()
        label_end = self.new_label()

        # Adicionando a condição do 'while'
        condition = self.visit(ctx.logical_expr())
        # Adicionando a etiqueta de início
        self.tac.append((label_start, None))
        self.tac.append(f"if False {condition} goto {label_end}")  # RP final removi o none

        # Visitando o corpo do 'while'
        self.visit(ctx.suite())

        # Adicionando a instrução para voltar ao início do 'while'
        self.tac.append(f"goto {label_start}")  # RP final removi o none

        # Adicionando a etiqueta de fim
        self.tac.append((label_end, None))

        return self.tac

    def visitLogical_expr(self, ctx):
        if ctx.getChildCount() > 1 and ctx.getChild(0).getText() == "not":
            condition = self.visit(ctx.getChild(1))
            temp = self.new_temp()
            self.tac.append((temp, f"not {condition}"))
            return temp
        else:
            left = self.visit(ctx.getChild(0))
            for i in range(1, ctx.getChildCount(), 2):
                op = ctx.getChild(i).getText()
                right = self.visit(ctx.getChild(i + 1))
                temp = self.new_temp()
                self.tac.append((temp, f"{left} {op} {right}"))
                left = temp
            return left

    def visitLogical_not(self, ctx):
        if ctx.getChildCount() > 1 and ctx.getChild(0).getText() == "not":
            condition = self.visit(ctx.getChild(1))
            temp = self.new_temp()
            self.tac.append((temp, f"not {condition}"))
            return temp
        return None

    def handle_type_and_conversion(self, left, right, op,
                                   dest_type):
        if self.is_int(right):  # RP 31/05
            right_type = 'int'  # RP 31/05
        elif self.is_float(right):  # RP 31/05
            right_type = 'float'  # RP 31/05
        else:  # RP 31/05
            right_type = self.get_var_type(right)  # RP 31/05

        temp = self.new_temp()  # RP 31/05

        if self.get_var_type(left) == 'int' and right_type == 'float':  # RP 31/05
            left = f"(float) {left}"  # RP 31/05
        elif self.get_var_type(left) == 'float' and right_type == 'int':  # RP 31/05
            right = f"(float) {right}"  # RP 31/05

        result = f"{left} {op} {right}"  # RP 31/05

        if dest_type == 'int' and 'float' in (self.get_var_type(left), right_type):  # RP 31/05
            cast_int = True  # RP 31/05
        else:  # RP 31/05
            cast_int = False  # RP 31/05

        self.tac.append((temp, result))  # RP 31/05
        self.set_var_type(temp, dest_type)  # RP 31/05
        return temp, cast_int  # RP 31/05

    def visitExprcomp(self, ctx, dest_type=None):
        if ctx.getChildCount() > 1 and ctx.getChild(0).getText() == "not":
            condition = self.visit(ctx.getChild(1))
            temp = self.new_temp()
            self.tac.append((temp, f"not {condition}"))
            return temp
        else:
            left = self.visit(ctx.getChild(0))
            for i in range(1, ctx.getChildCount(), 2):
                op = ctx.getChild(i).getText()
                right = self.visit(ctx.getChild(i + 1))
                temp, _ = self.handle_type_and_conversion(left, right, op, dest_type)  # RP 31/05

                left = temp
            return left

    def visitComparison(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            if ctx.getChildCount() > 2 and ctx.getChild(0).getText() == '(' and ctx.getChild(
                    ctx.getChildCount() - 1).getText() == ')':
                left = self.visit(ctx.getChild(1))
                for i in range(2, ctx.getChildCount() - 1, 2):
                    op = ctx.getChild(i).getText()
                    right = self.visit(ctx.getChild(i + 1))
                    temp = self.new_temp()
                    self.tac.append((temp, f"{left} {op} {right}"))
                    left = temp
                return left
            else:
                left = self.visit(ctx.getChild(0))
                for i in range(1, ctx.getChildCount(), 2):
                    op = ctx.getChild(i).getText()
                    right = self.visit(ctx.getChild(i + 1))
                    temp = self.new_temp()
                    self.tac.append((temp, f"{left} {op} {right}"))
                    left = temp
                return left

    def visitFunction(self, ctx):
        self.visit(ctx.functions_stmt())
        self.visit(ctx.suite_func())
        function_name = None
        return_type = None

        # Processar a declaração da função
        for i, child in enumerate(ctx.functions_stmt().children):

            if child.getText() == 'def':
                next_child = ctx.functions_stmt().getChild(i + 1).getText()
                if next_child in 'func':
                    function_name = ctx.functions_stmt().getChild(i + 2).getText()
                elif next_child in ['float', 'int']:  # Verifica se o próximo token é um tipo de retorno
                    return_type = next_child
                    next_child = ctx.functions_stmt().getChild(i + 2).getText()
                    if next_child == '[':
                        function_name = ctx.functions_stmt().getChild(i + 4).getText()
                        return_type = return_type + '[]'
                    else:
                        function_name = ctx.functions_stmt().getChild(i + 2).getText()
                else:
                    function_name = ctx.functions_stmt().getChild(i + 1).getText()

        # Verificação de variáveis retornadas inicializadas
        for stmt in ctx.suite_func().children:
            if stmt.getText().startswith('return'):
                return_var = stmt.getChild(1).getText()
                if return_var not in self.initialized_variables:
                    raise ValueError(f"Variable {return_var} not started")

        if return_type:
            self.tac.append(f"endfunc {return_type} {function_name}")
        else:
            self.tac.append(f"endfunc {function_name}")

        return self.tac

    def visitFunctions_stmt(self, ctx):

        function_name = None
        param_list = []
        param_types = []

        for i, child in enumerate(ctx.children):
            if child.getText() == 'def':

                next_child = ctx.getChild(i + 1).getText()
                if next_child in 'func':
                    # print("911")
                    function_name = ctx.getChild(i + 2).getText()

                elif next_child in ['float', 'int']:
                    next_child = ctx.getChild(i + 2).getText()
                    if next_child == '[':
                        function_name = ctx.getChild(i + 4).getText()
                    else:

                        function_name = ctx.getChild(i + 2).getText()

                else:
                    function_name = ctx.getChild(i + 1).getText()
            elif child.getText() in '[]':
                list_name = ctx.getChild(i + 1).getText()
                self.initialized_lists.add(list_name)
            elif child.getText() not in {'(', ')', ':', 'def', ',', '[', ']', function_name, 'float', 'int', 'func'}:
                param_type = child.getText()
                param_name = ctx.getChild(i).getText()
                param_types.append(param_type)
                param_list.append(param_name)
                self.set_var_type(param_name, param_type[:-2] if '[]' in param_type else param_type)
                self.initialized_variables.add(param_name)  # Marcar o parâmetro como inicializado

        # Generate TAC for function definition
        self.tac.append(f"func {function_name}")
        self.functions[function_name] = (param_list, param_types)
        for param in param_list:
            self.tac.append(f"param {param}")
            self.initialized_variables.add(param)

        return self.tac

    def visitFunctionCall(self, ctx):
        function_name = ctx.NAME().getText()
        arg_list = []

        # Process function arguments
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if child.getText() not in {'(', ')', ','} and not child.NAME():
                arg_list.append(self.visit(child))

        # Generate TAC for function call
        for arg in arg_list:
            self.tac.append(f"arg {arg}")
        ret_temp = self.new_temp()
        self.tac.append(f"{ret_temp} = call {function_name}, {len(arg_list)}")

        return ret_temp

    def generate_TAC(self, var_tree):
        self.visit(var_tree)
        self.tac_optimization()

        return self.tac


def generate_TAC(var_tree, flag):
    tac_generator = TACGenerator()
    generated_tree = tac_generator.generate_TAC(var_tree)
    ints = tac_generator.get_int_vars()
    floats = tac_generator.get_float_vars()

    if flag == 1:
        return generated_tree
    if flag == 2:
        return ints
    if flag == 3:
        return floats


# Exemplo de uso


# Exemplo de uso
input_stream = FileStream('test.mpy', encoding='utf-8')
lexer = MontyPythonLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = MontyPythonParser(stream)
tree = parser.file_input()
tac = generate_TAC(tree, 1)
int_vars = generate_TAC(tree, 2)
float_vars = generate_TAC(tree, 3)

# Imprimir a TAC
# Abre o arquivo 'test.tac' em modo de escrita ('w')
with open('test.tac', 'w') as f:
    f.write("TAC:\n")
    for instruction in tac:
        if isinstance(instruction, tuple) and len(instruction) == 2:
            if instruction[0] == instruction[1]:
                f.write(f"   {instruction[0]}\n")
            elif isinstance(instruction[0], str) and instruction[0].startswith('L'):
                f.write(f"{instruction[0]}:\n")
            elif isinstance(instruction[0], str) and instruction[0].startswith('return'):
                f.write(f"   {instruction[0]}  {instruction[1]}\n")
            else:
                if instruction[0] in int_vars:
                    f.write(f"   {instruction[0]} = {instruction[1]} 'int'\n")
                elif 'length' in instruction[0] or 'length' in instruction[1]:
                    f.write(f"   {instruction[0]} = {instruction[1]} 'int'\n")
                elif str(instruction[1]).isdigit():
                    f.write(f"   {instruction[0]} = {instruction[1]} 'int'\n")
                else:
                    f.write(f"   {instruction[0]} = {instruction[1]} 'float'\n")
        else:
            f.write(f"  {instruction}\n")
