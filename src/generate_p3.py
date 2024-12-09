import re


def generate_p3_assembly(input_file, output_file):
    """
    Generates P3 assembly code from a given input file and writes it to an output file.

    Args:
        input_file (str): The path to the input file containing the code.
        output_file (str): The path to the output file where the assembly code will be written.
    """

    def split_expression(expr, op):
        """
        Splits an expression into operands based on a specific operator.

        Args:
            expr (str): The expression to split.
            op (str): The operator to split the expression by.

        Returns:
            tuple: A tuple containing the left and right operands.

        Raises:
            ValueError: If the operator is not found in the expression.
        """
        escaped_op = re.escape(op)
        pattern = rf'(.*?){escaped_op}(.*)'
        match = re.match(pattern, expr)
        if match:
            left_operand = match.group(1).strip()
            right_operand = match.group(2).strip()
            return left_operand, right_operand
        else:
            raise ValueError("Operator not found in expression")

    def aritmetica(arg_line):
        """
        Processes arithmetic operations and generates corresponding assembly code.

        Args:
            arg_line (str): The line containing the arithmetic operation.

        Returns:
            str: The generated assembly code.
        """
        left_part, ari_type_part = arg_line.split("'", 1)
        ari_var_name, expr = left_part.split('=', 1)
        ari_var_name = ari_var_name.strip()
        expr = expr.strip()

        # Determine the operator in the expression
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
            raise ValueError(f"Unknown operation in {expr}")

        left_operand, right_operand = split_expression(expr, op)
        left_operand = left_operand.strip()
        right_operand = right_operand.strip()

        # Generate assembly code for the operation
        assembly_code = []
        if op == '*':
            assembly_code.append(f"    movl {left_operand}, %eax")
            assembly_code.append(f"    imull {right_operand}, %eax")
            assembly_code.append(f"    movl %eax, {ari_var_name}")
        elif op == '/':
            assembly_code.append(f"    movl {left_operand}, %eax")
            assembly_code.append(f"    cdq")
            assembly_code.append(f"    idivl {right_operand}")
            assembly_code.append(f"    movl %eax, {ari_var_name}")
        elif op == '//':
            assembly_code.append(f"    movl {left_operand}, %eax")
            assembly_code.append(f"    cdq")
            assembly_code.append(f"    idivl {right_operand}")
            assembly_code.append(f"    movl %eax, {ari_var_name}")
        elif op == '%':
            assembly_code.append(f"    movl {left_operand}, %eax")
            assembly_code.append(f"    cdq")
            assembly_code.append(f"    idivl {right_operand}")
            assembly_code.append(f"    movl %edx, {ari_var_name}")
        elif op == '+':
            assembly_code.append(f"    movl {left_operand}, %eax")
            assembly_code.append(f"    addl {right_operand}, %eax")
            assembly_code.append(f"    movl %eax, {ari_var_name}")
        elif op == '-':
            assembly_code.append(f"    movl {left_operand}, %eax")
            assembly_code.append(f"    subl {right_operand}, %eax")
            assembly_code.append(f"    movl %eax, {ari_var_name}")
        return '\n'.join(assembly_code)

    def is_unary_minus(expr):
        """
        Checks if the minus sign in an expression is unary.

        Args:
            expr (str): The expression to check.

        Returns:
            bool: True if the minus sign is unary, False otherwise.
        """
        expr = expr.strip()
        return expr.startswith('-') and not re.search(r'\w\s*-\s*\w', expr)

    # Open the input file for reading
    with open(input_file, 'r') as f_in:
        lines = f_in.readlines()

    # Open the output file for writing
    with open(output_file, 'w') as f_out:
        f_out.write(".section .data\n")

        defined_vars = {}  # Dictionary to store defined variables
        defined_lists = {}  # Dictionary to keep track of defined lists

        # First pass: collect variables, values, and types
        for line in lines:
            line = line.strip()
            if line and '=' in line and "'" in line and '[' not in line:
                var_part, type_part = line.split("'", 1)
                var_name, value_str = var_part.split('=', 1)
                var_name = var_name.strip()
                value_str = value_str.strip()
                var_type = type_part.strip().replace("'", "")
                if '(' in value_str and ')' in value_str:
                    value_str = value_str.split(')')[-1].strip()
                if 'length' in var_name:
                    list_name = var_name.split('.')[0]
                    list_name = list_name.strip()
                    for n in defined_lists:
                        if n == list_name:
                            value_str = defined_lists[n][1]
                if var_name not in defined_vars:
                    defined_vars[var_name] = (value_str, var_type)
            elif '= [' in line:
                lista_int = []

                var_part, type_part = line.split("'", 1)
                list_name, value_str = var_part.split('=', 1)
                var_type = type_part.strip().replace("'", "")
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
                        if i.isdigit():
                            lista_float[j] = float(i)
                            j = j + 1

                    list_length = len(lista_float)
                    defined_lists[list_name] = (lista_float, list_length, var_type)
            elif '[' in line:
                var_part, type_part = line.split("'", 1)
                var_name, value_str = var_part.split('=', 1)
                var_name = var_name.strip()
                value_str = value_str.strip()
                var_type = type_part.strip().replace("'", "")
                if '[' in value_str and value_str[0] != '[':
                    defined_vars[var_name] = (0, var_type)

        # Second pass: define in the .data section
        for var_name, (value_str, var_type) in defined_vars.items():
            try:
                float_value = float(value_str)
                if var_type == 'float':
                    f_out.write(f"{var_name}: .float {float_value}\n")
                elif var_type == 'int' and float_value.is_integer():
                    f_out.write(f"{var_name}: .int {int(float_value)}\n")
                else:
                    print(f"Error: Type mismatch for {var_name} = {value_str}")
            except ValueError:
                f_out.write(f"{var_name}: .{var_type} 0\n")

        for list_name, (lista, length, var_type) in defined_lists.items():
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

        f_out.write("\n.section .text\n")
        f_out.write(".globl main\n")
        f_out.write("main:\n")

        # Third pass: process arithmetic operations and other instructions
        for line in lines:
            line = line.strip()
            if line and '=' in line and '[' not in line and '>' not in line and (
                    '*' in line or '//' in line or '/' in line or '%' in line or '+' in line or (
                    '-' in line and not is_unary_minus(line.split('=')[1].strip()))):
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
                if line == "TAC:":
                    continue
                f_out.write(f"{line}\n")

        # Add code to exit the program
        f_out.write("\n; Exit the program\n")
        f_out.write("    movl $1, %eax\n")
        f_out.write("    xorl %ebx, %ebx\n")
        f_out.write("    int $0x80\n")

    print(f'Assembly file successfully generated: {output_file}')


# Example usage:
generate_p3_assembly('test.tac', 'test.asm')
