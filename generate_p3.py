import re

def generate_p3_assembly(input_file, output_file):
    # Função para dividir uma expressão em operandos com base num operador específico
    def split_expression(expr, op):
        escaped_op = re.escape(op)  # Adiciona uma barra invertida antes de caracteres especiais no operador para que sejam tratados como caracteres literais na expressão regular
        pattern = rf'(.*?){escaped_op}(.*)'  # Regex para dividir na primeira ocorrência do operador
        match = re.match(pattern, expr)
        if match:
            left_operand = match.group(1).strip()
            right_operand = match.group(2).strip()
            return left_operand, right_operand
        else:
            raise ValueError("Operador não encontrado na expressão")

    # Função para processar operações aritméticas
    def aritmetica(arg_line):
        left_part, ari_type_part = arg_line.split("'", 1)
        ari_var_name, expr = left_part.split('=', 1)
        ari_var_name = ari_var_name.strip()
        expr = expr.strip()

        # Determinar o operador na expressão
        if '*' in expr:
            op = '*'
        elif '//' in expr:
            op = '//'
        elif '/' in expr:
            op = '/'
        elif '%' in expr:
            op = '%'
        elif '+' in expr:
            op = '+'
        elif '-' in expr:
            op = '-'
        else:
            raise ValueError(f"Operação desconhecida em {expr}")

        left_operand, right_operand = split_expression(expr, op)
        left_operand = left_operand.strip()
        right_operand = right_operand.strip()

        # Gerar código assembly para a operação
        assembly_code = []
        if op == '*':
            assembly_code.append(f"    movl {left_operand}, %eax")
            assembly_code.append(f"    imull {right_operand}, %eax")
            assembly_code.append(f"    movl %eax, {ari_var_name}")
        elif op == '/':
            assembly_code.append(f"    movl {left_operand}, %eax")
            assembly_code.append(f"    cdq")  # Extensão de sinal de EAX para EDX:EAX
            assembly_code.append(f"    idivl {right_operand}")  # Dividir EDX:EAX pelo operando direito
            assembly_code.append(f"    movl %eax, {ari_var_name}")  # Mover o quociente para a variável
        elif op == '//':
            assembly_code.append(f"    movl {left_operand}, %eax")
            assembly_code.append(f"    cdq")
            assembly_code.append(f"    idivl {right_operand}")
            assembly_code.append(f"    movl %eax, {ari_var_name}")  # Mover o quociente para a variável
        elif op == '%':
            assembly_code.append(f"    movl {left_operand}, %eax")
            assembly_code.append(f"    cdq")
            assembly_code.append(f"    idivl {right_operand}")
            assembly_code.append(f"    movl %edx, {ari_var_name}")  # Mover o resto para a variável
        elif op == '+':
            assembly_code.append(f"    movl {left_operand}, %eax")
            assembly_code.append(f"    addl {right_operand}, %eax")
            assembly_code.append(f"    movl %eax, {ari_var_name}")
        elif op == '-':
            assembly_code.append(f"    movl {left_operand}, %eax")
            assembly_code.append(f"    subl {right_operand}, %eax")
            assembly_code.append(f"    movl %eax, {ari_var_name}")
        return '\n'.join(assembly_code)

    # Função para verificar se o sinal de menos é unário
    def is_unary_minus(expr):
        expr = expr.strip()
        return expr.startswith('-') and not re.search(r'\w\s*-\s*\w', expr)
    


    # Abrir o ficheiro de entrada para leitura
    with open(input_file, 'r') as f_in:
        lines = f_in.readlines()

    # Abrir o ficheiro de saída para escrita
    with open(output_file, 'w') as f_out:
        f_out.write(".section .data\n")

        defined_vars = {}  # Dicionário para armazenar variáveis definidas
        defined_lists = {} # Dicionário para manter o controle das listas definidas

        # Primeira passagem: coletar variáveis, valores e tipos
        for line in lines:
            line = line.strip()
            if line and '=' in line and "'" in line and not '[' in line:
                var_part, type_part = line.split("'", 1)  # Dividir pela primeira ocorrência de '
                var_name, value_str = var_part.split('=', 1)  # Dividir pela primeira ocorrência de =
                var_name = var_name.strip()
                value_str = value_str.strip()
                var_type = type_part.strip().replace("'", "")  # Remover aspas simples adicionais
                if '(' in value_str and ')' in value_str:
                    value_str = value_str.split(')')[-1].strip()
                if 'length' in var_name:                       # Obtem o tamanho da lista para variável do tipo lista.length - Paulo
                    list_name = var_name.split('.')[0]
                    list_name = list_name.strip()
                    for n in defined_lists:
                        if n == list_name:
                            value_str = defined_lists[n][1]
                            
                if var_name not in defined_vars:
                    defined_vars[var_name] = (value_str, var_type)
        
            # Paulo
            # coleta das listas e seus valores 
            elif '= [' in line: 
                lista_int = []
                lista_float = []
                var_part, type_part = line.split("'", 1)  # Divide pela primeira ocorrência de '
                list_name, value_str = var_part.split('=', 1)  # Divide pela primeira ocorrência de =
                var_type = type_part.strip().replace("'", "")  # Remove aspas simples adicionais
                list_name = list_name.strip()
                if 'int' in type_part:
                    for i in value_str:
                        if i.isdigit():
                            lista_int.append(int(i))
                    list_length = len(lista_int)
                    defined_lists[list_name] = (lista_int, list_length, var_type)
                elif 'float' in type_part:
                    value_str = value_str.replace('[', '')
                    value_str = value_str.replace(']', '')
                    value_str = value_str.replace("'", '')
                    value_str = value_str.replace(" ", '')
                    lista_float = value_str.split(',')
                    j = 0
                    for i in lista_float:
                        try:
                            lista_float[j] = float(i)
                            j = j + 1
                        except:
                            pass
                    list_length = len(lista_float)
                    defined_lists[list_name] = (lista_float, list_length, var_type)

            elif '[' in line:   # Trata as atribuições do tipo t4 = list[t3]
                var_part, type_part = line.split("'", 1)  # Dividir pela primeira ocorrência de '
                var_name, value_str = var_part.split('=', 1)  # Dividir pela primeira ocorrência de =
                var_name = var_name.strip()
                value_str = value_str.strip()
                var_type = type_part.strip().replace("'", "")  # Remover aspas simples adicionais
                if '[' in value_str and value_str[0] != '[':
                    defined_vars[var_name] = (0, var_type)


        # Segunda passagem: definir na seção .data
        for var_name, (value_str, var_type) in defined_vars.items():
            try:
                float_value = float(value_str)
                if var_type == 'float':
                    f_out.write(f"{var_name}: .float {float_value}\n")
                elif var_type == 'int' and float_value.is_integer():
                    f_out.write(f"{var_name}: .int {int(float_value)}\n")
                else:
                    print(f"Erro: Incompatibilidade de tipo para {var_name} = {value_str}")
            except ValueError as e:
                f_out.write(f"{var_name}: .{var_type} 0\n")
        
        # Paulo
        # Definição de cada valor da lista
        for list_name, (lista, length, var_type) in defined_lists.items():
            try:  
                if var_type == 'float':
                    f_out.write(f"{list_name}: .float ")
                    for i in lista:
                        if i == lista[-1]:
                            f_out.write(f"{i}")
                        else:
                            f_out.write(f"{i}, ")
                        
                elif var_type == 'int':
                    f_out.write(f"{list_name}: .int ")
                    for i in lista:
                        if i == lista[-1]:
                            f_out.write(f"{i}")
                        else:
                            f_out.write(f"{i}, ")
            except:
                pass

        f_out.write("\n.section .text\n")
        f_out.write(".globl main\n")
        f_out.write("main:\n")

        # Terceira passagem: processar operações aritméticas e outras instruções
        for line in lines:
            line = line.strip()
            if line and '=' in line and not '[' in line and not '>' in line and ('*' in line or '//' in line or '/' in line or '%' in line or '+' in line or ('-' in line and not is_unary_minus(line.split('=')[1].strip()))):  # confirma se - é unário
                f_out.write(aritmetica(line) + '\n')
            elif line and '=' in line and "'" in line:
                var_part, type_part = line.split("'", 1)
                var_name, value_str = var_part.split('=', 1)
                var_name = var_name.strip()
                value_str = value_str.strip()

                if value_str in defined_vars:
                    f_out.write(f"    movl {value_str}, {var_name}\n")
            elif line.startswith('if'):
                condition_part = line.split('goto')[0].strip()
                label = line.split('goto')[1].strip()
                condition_var = condition_part.split()[1]
                f_out.write(f"    cmpl $0, {condition_var}\n")
                f_out.write(f"    jle {label}\n")
            elif line.startswith('goto'):
                label = line.split()[1].strip()
                f_out.write(f"    jmp {label}\n")
            elif line.endswith(':'):
                if line == "TAC:":  # ignora TAC:
                    continue
                f_out.write(f"{line}\n")
        

        # Adicionar código para sair do programa
        f_out.write("\n; Exit the program\n")
        f_out.write("    movl $1, %eax\n")
        f_out.write("    xorl %ebx, %ebx\n")
        f_out.write("    int $0x80\n")

    print(f'Ficheiro assembly gerado com sucesso: {output_file}')


# Exemplo de uso:
generate_p3_assembly('test.tac', 'test.asm')
