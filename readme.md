﻿MONTy Python Language Guide
Overview
This repository contains the comprehensive guide for MONTy Python, a custom programming language developed for educational purposes in the 2023/24 academic year. MONTy Python stands for "My Own Narrowed Typed Python," featuring explicitly typed variables and unique syntax rules. 


To test the generation of the lexer and parser:

1. Use the command line to navigate to the folder containing MontyPythonLexer and MontyPythonParser.

2. Use the following command to generate the intermediate files:
   java -cp "C:\Program Files\Java\jdk-21\lib\antlr-4.13.1-complete.jar" org.antlr.v4.Tool -Dlanguage=Python3 -listener -visitor MontyPythonLexer.g4 MontyPythonParser.g4 -o output_dir
   (or the path to ANTLR on your computer)

After that, type the following in the terminal:
   python test.py
   - This will generate the intermediate file (.tac).

   python generate_p3.py
   - This will generate the file with the final code (.asm).

The file `seeTree` does the same but shows the tree:
- Modify `sys.path.append(r'C:\Users\Hugo\Desktop\compilador\output_dir')` to your directory.
- Then run:
   python seeTree.py
   - This will create a PDF with the tree in a folder named output.

Both `test.py` and `seeTree.py` test the file "test.mpy".

5. To generate the optimized Three Address Code from the MontyPython code present in the file test.mpy, run the following command in the terminal:
   python tac_generator.py
