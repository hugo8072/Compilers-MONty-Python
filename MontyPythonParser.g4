


parser grammar MontyPythonParser; 
options { tokenVocab=MontyPythonLexer; }



file_input: (NEWLINE | stmt)* EOF; // start rule



//stmt: simple_stmt | compound_stmt;
stmt: simple_stmt | compound_stmt | function;







simple_stmt: small_stmt NEWLINE;

small_stmt: functions_stmt|list_op|list_stmt|expr_stmt | flow_stmt | print_stmt;

expr_stmt:LIST_VALUE '=' expr
         |NAME '=' expr
         |NAME '=' logical_expr
         |TYPE_INT? NAME (EQUAL (PLUS|MINUS)? (INT|var_int_expr)) (COMMA NAME (EQUAL (PLUS|MINUS)? (INT|var_int_expr)))*
         |TYPE_INT NAME (COMMA NAME EQUAL? (INT|var_int_expr)?)*
         |TYPE_FLOAT NAME (COMMA NAME EQUAL? (INT|FLOAT|var_float_expr)?)*
         |TYPE_FLOAT? NAME (EQUAL (PLUS|MINUS)? (FLOAT|var_float_expr)) (COMMA NAME (EQUAL (PLUS|MINUS)? (FLOAT|var_float_expr)?))*//1
         |TYPE_FLOAT? NAME (EQUAL (PLUS|MINUS)? (INT|var_float_expr)) (COMMA NAME (EQUAL (PLUS|MINUS)? (INT|var_float_expr))?)* //2
         |TYPE_INT NAME EQUAL int_expr
         |TYPE_FLOAT NAME EQUAL float_expr
         |(TYPE_FLOAT|TYPE_INT)? NAME '=' input_func;
     


       // Podemos simplifcar isto usando TYPE_NUMBER... a refazer quando tivermos tempo
         //deveria bastar definir (EQUAL NUMBER) em TYPE_FLOAT float (1 a 4... bastaria 1 definiçao)
         // mas está a dar conflito...tentar obter feedback professor

         // não dá para colocar tipo e definir expressao logo de seguida
         //primeiro tem que se definir variavel e só depois fazer as expressoes

list_stmt: TYPE_INT LEFT_BRACKET RIGHT_BRACKET  NAME (EQUAL LEFT_BRACKET ((INT) (COMMA INT)*) RIGHT_BRACKET)?
         | TYPE_FLOAT LEFT_BRACKET RIGHT_BRACKET  NAME (EQUAL LEFT_BRACKET ((INT|FLOAT) (COMMA (INT|FLOAT))*) RIGHT_BRACKET)?
         | NAME EQUAL ((LEFT_BRACKET ((INT|FLOAT) (COMMA (INT|FLOAT))*) RIGHT_BRACKET)|(LEFT_BRACKET ((INT) (COMMA INT)*) RIGHT_BRACKET))
         ;


list_op: L_SIZE '(' NAME ')'
       | L_ADD '(' NAME COMMA (INT|FLOAT|NAME) COMMA (INT|FLOAT|NAME) ')'
       | L_REMOVE '(' NAME COMMA (INT|NAME) ')'
       | LIST_VALUE EQUAL (LIST_VALUE|NAME) (PLUS|MINUS|TIMES|DIVIDE)? (INT|FLOAT|NAME)?;


functions_stmt: DEF (TYPE_FLOAT|TYPE_INT) LEFT_BRACKET RIGHT_BRACKET NAME '('(TYPE_FLOAT|TYPE_INT) (LEFT_BRACKET RIGHT_BRACKET)? NAME (COMMA  (TYPE_FLOAT|TYPE_INT)? (LEFT_BRACKET RIGHT_BRACKET)? NAME)* ')' ':'
              |DEF (TYPE_FLOAT|TYPE_INT)? FUNCTION_DEF? NAME '(' ((TYPE_FLOAT|TYPE_INT)?(LEFT_BRACKET RIGHT_BRACKET)? NAME? (COMMA  (TYPE_FLOAT|TYPE_INT)?(LEFT_BRACKET RIGHT_BRACKET)? NAME)*) ')'  ':';
              
              // A melhorar este left  bracket right bracket. podemos simplificar para type_list ou algo assim
              //TYPE_NUMBER está a fazer conflito

function_def: NAME '(' (TYPE_FLOAT|TYPE_INT)? NAME?(COMMA  (TYPE_FLOAT|TYPE_INT)?  NAME)* ')';



flow_stmt: break_stmt | continue_stmt;
break_stmt: 'break';
continue_stmt: 'continue';

compound_stmt: if_stmt | while_stmt| for_stmt;
if_stmt: 'if' logical_expr ':' (suite|suite_func) ('elif' logical_expr ':' (suite|suite_func))* ('else' ':' (suite|suite_func))?;

while_stmt: 'while' logical_expr ':' (suite|suite_func);

for_stmt : FOR NAME IN (RANGE|NAME) '('? expr? ','? expr? ','? expr? ')'? ':' (suite|suite_func);  // Hugo: Adicionei para o loop do For


function: functions_stmt  suite_func ;
end_function: RETURN (expr|NAME|simple_stmt|var_float_expr|var_int_expr|int_expr|float_expr);




suite_func: simple_stmt  |(NEWLINE INDENT stmt+ end_function? NEWLINE? DEDENT  )|NEWLINE INDENT end_function NEWLINE DEDENT; //vai dar asneira penso eu
// o NEWLINE? antes do DEDENT  foi adicionado... possivelmente vai entrar em conflito com a contagem dos niveis de indentacao futuramente


suite:simple_stmt   | (NEWLINE INDENT stmt+   DEDENT);

logical_not: NOT(logical_expr|comparison);

logical_op: AND | OR;

logical_expr : logical_not|(comparison (logical_op comparison)*);

exprcomp: expr (comp_op expr)*;

comparison: logical_not | (exprcomp | '(' (exprcomp logical_op?)*')');  // RP Final Parentesis no sitio errado

comp_op: '<'|'>'|'=='|'>='|'<='|'!=';

int_expr: term_int ((PLUS | MINUS) term_int)*
         | '(' int_expr ')'
         | INT;

float_expr: term_float ((PLUS | MINUS) term_float)*
           | '(' float_expr ')'
           | FLOAT
           |INT ;

var_int_expr: (LIST_VALUE|NAME) ((PLUS | MINUS) (term_int|NAME))* 
            |term_int ((PLUS | MINUS) (LIST_VALUE|NAME))*
            |'(' var_int_expr ')'
            |INT;
//alterar nome. isto já não é var_int_expression... uma vez que vai aceitar p.e.: x = x + y




var_float_expr:  (LIST_VALUE|NAME) ((PLUS | MINUS) (term_float|term_int|NAME))*
              |(term_float|term_int) ((PLUS | MINUS) (LIST_VALUE|NAME))*
              |'(' var_float_expr ')'
              |FLOAT
              |INT;

//same as var_int_expr

term_int: factor_int ((TIMES | DIVIDE | FLOOR_DIVIDE | MODULO) factor_int)*;

term_float: factor_float ((TIMES | DIVIDE | FLOOR_DIVIDE | MODULO) factor_float)*;

term_var_int: factor_var_int ((TIMES | DIVIDE | FLOOR_DIVIDE | MODULO) factor_int)*; // adicionado factor_var_int no final... 
//mudar nome no futuro pq 

term_var_float: factor_var_int ((TIMES | DIVIDE | FLOOR_DIVIDE | MODULO) (factor_int|factor_float))*;

factor_var_int: (LIST_VALUE|NAME) (EXPONENT primary_int)?;

factor_var_float: (LIST_VALUE|NAME) (EXPONENT (primary_int|primary_float))?;

factor_int: primary_int (EXPONENT primary_int)?;

factor_float: primary_float (EXPONENT primary_float)?;

primary_int: INT | '(' int_expr ')';

primary_float: FLOAT | INT | '(' float_expr ')';



expr: term ((PLUS | MINUS) term)*;

term: factor ((TIMES | DIVIDE | FLOOR_DIVIDE | MODULO) factor)*;

factor: primary (EXPONENT primary)?;

primary:LIST_VALUE|NAME LPAR expr RPAR |NAME'('NAME')'|L_SIZE'('NAME')'| NAME | INT | FLOAT | STRING
       | '(' expr ')'
       | (PLUS | MINUS) primary;

//NAME(NAME) muito possivelmente dará raia no futuro. a rever


input_func: INPUT '(' arg ')'; 
print_stmt: PRINT '(' arg  (COMMA arg)* ')'; 
arg :LIST_VALUE|function_def|STRING+| NAME   | NUMBER | expr;
