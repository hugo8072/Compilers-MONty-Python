

lexer grammar MontyPythonLexer;
options { superClass=MontyPythonLexerBase; }
tokens {
    // the following tokens are only for compatibility with the PythonLexerBase class
    LSQB, RSQB, LBRACE, RBRACE, TYPE_COMMENT, FSTRING_START, FSTRING_MIDDLE, FSTRING_END

    // https://docs.python.org/3.8/reference/lexical_analysis.html#indentation
  , INDENT, DEDENT
}

/*
 * lexer rules    https://docs.python.org/3.8/reference/lexical_analysis.html#
 */

// https://docs.python.org/3.8/reference/lexical_analysis.html#keywords

ELSE     : 'else';
BREAK    : 'break';
CONTINUE : 'continue';
WHILE    : 'while';
ELIF     : 'elif';
IF       : 'if';
FOR      : 'for';   
IN       : 'in';    
RANGE    : 'range'; 



PRINT    : 'print'; 
INPUT    : 'input'; 


// https://docs.python.org/3.8/library/token.html#token.OP
LPAR         : '(';  // OPEN_PAREN
RPAR         : ')';  // CLOSE_PAREN
COLON        : ':';
PLUS         : '+' ;  
MINUS        : '-' ; 
TIMES        : '*' ;  
DIVIDE       : '/' ;  
FLOOR_DIVIDE: '//' ;  
MODULO       : '%' ;  
EXPONENT     :'**' ;  
LESS         : '<';
GREATER      : '>';
EQUAL        : '=';
COMMA        : ',';
EQEQUAL      : '==';
NOTEQUAL     : '!=';
LESSEQUAL    : '<=';
GREATEREQUAL : '>=';



LEFT_BRACKET: '[';
RIGHT_BRACKET: ']';

//logical
AND: 'and';
OR : 'or';
NOT : 'not';

//lists functions
L_ADD: 'add';
L_SIZE: 'size';
L_REMOVE: 'remove';

//functions
RETURN: 'return';
DEF: 'def';
FUNCTION_DEF: 'func';



 
TYPE_INT: 'int';
TYPE_FLOAT: 'float';
TYPE_NUMBER: (TYPE_INT|TYPE_FLOAT); 




NAME: ('_' | [a-z]) ('_' | [a-zA-Z0-9])*;






// https://docs.python.org/3.8/reference/lexical_analysis.html#physical-lines
NEWLINE : '\r'? '\n'; // Unix, Windows

// https://docs.python.org/3.8/reference/lexical_analysis.html#comments
COMMENT : '#'+ ~[\r\n]*               -> channel(HIDDEN);

// https://docs.python.org/3.8/reference/lexical_analysis.html#whitespace-between-tokens
WS : [ \t\f]+                        -> channel(HIDDEN);

// https://docs.python.org/3.8/reference/lexical_analysis.html#explicit-line-joining
EXPLICIT_LINE_JOINING : '\\' NEWLINE -> channel(HIDDEN);







//tentamos colocar float primeiro para a primeira associação no caso de 
//nao se definir tipo mas entrava em conflito com outras regras
INT   :  [0-9]+;

FLOAT :  [0-9]+ ('.' [0-9]*)? ('e' | 'E') ('+' | '-')? [0-9]+
      |  [0-9]+ '.'? [0-9]* ; 



LIST_VALUE: NAME LEFT_BRACKET (INT|FLOAT|NAME) RIGHT_BRACKET;
//INT_LIST : LEFT_BRACKET (INT) (COMMA INT)* RIGHT_BRACKET;
//FLOAT_LIST: LEFT_BRACKET (INT|FLOAT) (COMMA (INT|FLOAT))* RIGHT_BRACKET;




NUMBER : (INT|FLOAT);

ERRORTOKEN : . ; // catch unrecognized characters and redirect these errors to the parser






 STRING : '"' .*? '"';








 

















// the following lexer modes are only for compatibility with the PythonLexerBase class
mode SINGLE_QUOTE_FSTRING_MODE; A : . ;
mode DOUBLE_QUOTE_FSTRING_MODE; B : . ;
mode LONG_SINGLE_QUOTE_FSTRING_MODE; C : . ;
mode LONG_DOUBLE_QUOTE_FSTRING_MODE; D : . ;
mode SINGLE_QUOTE_FORMAT_SPECIFICATION_MODE; E : . ;
mode DOUBLE_QUOTE_FORMAT_SPECIFICATION_MODE; F : . ;






