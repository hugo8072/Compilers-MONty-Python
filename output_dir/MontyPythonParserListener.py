# Generated from MontyPythonParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MontyPythonParser import MontyPythonParser
else:
    from MontyPythonParser import MontyPythonParser

# This class defines a complete listener for a parse tree produced by MontyPythonParser.
class MontyPythonParserListener(ParseTreeListener):

    # Enter a parse tree produced by MontyPythonParser#file_input.
    def enterFile_input(self, ctx:MontyPythonParser.File_inputContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#file_input.
    def exitFile_input(self, ctx:MontyPythonParser.File_inputContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#stmt.
    def enterStmt(self, ctx:MontyPythonParser.StmtContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#stmt.
    def exitStmt(self, ctx:MontyPythonParser.StmtContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#simple_stmt.
    def enterSimple_stmt(self, ctx:MontyPythonParser.Simple_stmtContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#simple_stmt.
    def exitSimple_stmt(self, ctx:MontyPythonParser.Simple_stmtContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#small_stmt.
    def enterSmall_stmt(self, ctx:MontyPythonParser.Small_stmtContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#small_stmt.
    def exitSmall_stmt(self, ctx:MontyPythonParser.Small_stmtContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#expr_stmt.
    def enterExpr_stmt(self, ctx:MontyPythonParser.Expr_stmtContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#expr_stmt.
    def exitExpr_stmt(self, ctx:MontyPythonParser.Expr_stmtContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#list_stmt.
    def enterList_stmt(self, ctx:MontyPythonParser.List_stmtContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#list_stmt.
    def exitList_stmt(self, ctx:MontyPythonParser.List_stmtContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#list_op.
    def enterList_op(self, ctx:MontyPythonParser.List_opContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#list_op.
    def exitList_op(self, ctx:MontyPythonParser.List_opContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#functions_stmt.
    def enterFunctions_stmt(self, ctx:MontyPythonParser.Functions_stmtContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#functions_stmt.
    def exitFunctions_stmt(self, ctx:MontyPythonParser.Functions_stmtContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#function_def.
    def enterFunction_def(self, ctx:MontyPythonParser.Function_defContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#function_def.
    def exitFunction_def(self, ctx:MontyPythonParser.Function_defContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#flow_stmt.
    def enterFlow_stmt(self, ctx:MontyPythonParser.Flow_stmtContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#flow_stmt.
    def exitFlow_stmt(self, ctx:MontyPythonParser.Flow_stmtContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#break_stmt.
    def enterBreak_stmt(self, ctx:MontyPythonParser.Break_stmtContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#break_stmt.
    def exitBreak_stmt(self, ctx:MontyPythonParser.Break_stmtContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#continue_stmt.
    def enterContinue_stmt(self, ctx:MontyPythonParser.Continue_stmtContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#continue_stmt.
    def exitContinue_stmt(self, ctx:MontyPythonParser.Continue_stmtContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#compound_stmt.
    def enterCompound_stmt(self, ctx:MontyPythonParser.Compound_stmtContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#compound_stmt.
    def exitCompound_stmt(self, ctx:MontyPythonParser.Compound_stmtContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#if_stmt.
    def enterIf_stmt(self, ctx:MontyPythonParser.If_stmtContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#if_stmt.
    def exitIf_stmt(self, ctx:MontyPythonParser.If_stmtContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#while_stmt.
    def enterWhile_stmt(self, ctx:MontyPythonParser.While_stmtContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#while_stmt.
    def exitWhile_stmt(self, ctx:MontyPythonParser.While_stmtContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#for_stmt.
    def enterFor_stmt(self, ctx:MontyPythonParser.For_stmtContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#for_stmt.
    def exitFor_stmt(self, ctx:MontyPythonParser.For_stmtContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#function.
    def enterFunction(self, ctx:MontyPythonParser.FunctionContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#function.
    def exitFunction(self, ctx:MontyPythonParser.FunctionContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#end_function.
    def enterEnd_function(self, ctx:MontyPythonParser.End_functionContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#end_function.
    def exitEnd_function(self, ctx:MontyPythonParser.End_functionContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#suite_func.
    def enterSuite_func(self, ctx:MontyPythonParser.Suite_funcContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#suite_func.
    def exitSuite_func(self, ctx:MontyPythonParser.Suite_funcContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#suite.
    def enterSuite(self, ctx:MontyPythonParser.SuiteContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#suite.
    def exitSuite(self, ctx:MontyPythonParser.SuiteContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#logical_not.
    def enterLogical_not(self, ctx:MontyPythonParser.Logical_notContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#logical_not.
    def exitLogical_not(self, ctx:MontyPythonParser.Logical_notContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#logical_op.
    def enterLogical_op(self, ctx:MontyPythonParser.Logical_opContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#logical_op.
    def exitLogical_op(self, ctx:MontyPythonParser.Logical_opContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#logical_expr.
    def enterLogical_expr(self, ctx:MontyPythonParser.Logical_exprContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#logical_expr.
    def exitLogical_expr(self, ctx:MontyPythonParser.Logical_exprContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#exprcomp.
    def enterExprcomp(self, ctx:MontyPythonParser.ExprcompContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#exprcomp.
    def exitExprcomp(self, ctx:MontyPythonParser.ExprcompContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#comparison.
    def enterComparison(self, ctx:MontyPythonParser.ComparisonContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#comparison.
    def exitComparison(self, ctx:MontyPythonParser.ComparisonContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#comp_op.
    def enterComp_op(self, ctx:MontyPythonParser.Comp_opContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#comp_op.
    def exitComp_op(self, ctx:MontyPythonParser.Comp_opContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#int_expr.
    def enterInt_expr(self, ctx:MontyPythonParser.Int_exprContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#int_expr.
    def exitInt_expr(self, ctx:MontyPythonParser.Int_exprContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#float_expr.
    def enterFloat_expr(self, ctx:MontyPythonParser.Float_exprContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#float_expr.
    def exitFloat_expr(self, ctx:MontyPythonParser.Float_exprContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#var_int_expr.
    def enterVar_int_expr(self, ctx:MontyPythonParser.Var_int_exprContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#var_int_expr.
    def exitVar_int_expr(self, ctx:MontyPythonParser.Var_int_exprContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#var_float_expr.
    def enterVar_float_expr(self, ctx:MontyPythonParser.Var_float_exprContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#var_float_expr.
    def exitVar_float_expr(self, ctx:MontyPythonParser.Var_float_exprContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#term_int.
    def enterTerm_int(self, ctx:MontyPythonParser.Term_intContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#term_int.
    def exitTerm_int(self, ctx:MontyPythonParser.Term_intContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#term_float.
    def enterTerm_float(self, ctx:MontyPythonParser.Term_floatContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#term_float.
    def exitTerm_float(self, ctx:MontyPythonParser.Term_floatContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#term_var_int.
    def enterTerm_var_int(self, ctx:MontyPythonParser.Term_var_intContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#term_var_int.
    def exitTerm_var_int(self, ctx:MontyPythonParser.Term_var_intContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#term_var_float.
    def enterTerm_var_float(self, ctx:MontyPythonParser.Term_var_floatContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#term_var_float.
    def exitTerm_var_float(self, ctx:MontyPythonParser.Term_var_floatContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#factor_var_int.
    def enterFactor_var_int(self, ctx:MontyPythonParser.Factor_var_intContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#factor_var_int.
    def exitFactor_var_int(self, ctx:MontyPythonParser.Factor_var_intContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#factor_var_float.
    def enterFactor_var_float(self, ctx:MontyPythonParser.Factor_var_floatContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#factor_var_float.
    def exitFactor_var_float(self, ctx:MontyPythonParser.Factor_var_floatContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#factor_int.
    def enterFactor_int(self, ctx:MontyPythonParser.Factor_intContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#factor_int.
    def exitFactor_int(self, ctx:MontyPythonParser.Factor_intContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#factor_float.
    def enterFactor_float(self, ctx:MontyPythonParser.Factor_floatContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#factor_float.
    def exitFactor_float(self, ctx:MontyPythonParser.Factor_floatContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#primary_int.
    def enterPrimary_int(self, ctx:MontyPythonParser.Primary_intContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#primary_int.
    def exitPrimary_int(self, ctx:MontyPythonParser.Primary_intContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#primary_float.
    def enterPrimary_float(self, ctx:MontyPythonParser.Primary_floatContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#primary_float.
    def exitPrimary_float(self, ctx:MontyPythonParser.Primary_floatContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#expr.
    def enterExpr(self, ctx:MontyPythonParser.ExprContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#expr.
    def exitExpr(self, ctx:MontyPythonParser.ExprContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#term.
    def enterTerm(self, ctx:MontyPythonParser.TermContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#term.
    def exitTerm(self, ctx:MontyPythonParser.TermContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#factor.
    def enterFactor(self, ctx:MontyPythonParser.FactorContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#factor.
    def exitFactor(self, ctx:MontyPythonParser.FactorContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#primary.
    def enterPrimary(self, ctx:MontyPythonParser.PrimaryContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#primary.
    def exitPrimary(self, ctx:MontyPythonParser.PrimaryContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#input_func.
    def enterInput_func(self, ctx:MontyPythonParser.Input_funcContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#input_func.
    def exitInput_func(self, ctx:MontyPythonParser.Input_funcContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#print_stmt.
    def enterPrint_stmt(self, ctx:MontyPythonParser.Print_stmtContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#print_stmt.
    def exitPrint_stmt(self, ctx:MontyPythonParser.Print_stmtContext):
        pass


    # Enter a parse tree produced by MontyPythonParser#arg.
    def enterArg(self, ctx:MontyPythonParser.ArgContext):
        pass

    # Exit a parse tree produced by MontyPythonParser#arg.
    def exitArg(self, ctx:MontyPythonParser.ArgContext):
        pass



del MontyPythonParser