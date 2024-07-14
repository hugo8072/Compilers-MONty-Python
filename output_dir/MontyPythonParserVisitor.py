# Generated from MontyPythonParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MontyPythonParser import MontyPythonParser
else:
    from MontyPythonParser import MontyPythonParser

# This class defines a complete generic visitor for a parse tree produced by MontyPythonParser.

class MontyPythonParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MontyPythonParser#file_input.
    def visitFile_input(self, ctx:MontyPythonParser.File_inputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#stmt.
    def visitStmt(self, ctx:MontyPythonParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#simple_stmt.
    def visitSimple_stmt(self, ctx:MontyPythonParser.Simple_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#small_stmt.
    def visitSmall_stmt(self, ctx:MontyPythonParser.Small_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#expr_stmt.
    def visitExpr_stmt(self, ctx:MontyPythonParser.Expr_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#list_stmt.
    def visitList_stmt(self, ctx:MontyPythonParser.List_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#list_op.
    def visitList_op(self, ctx:MontyPythonParser.List_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#functions_stmt.
    def visitFunctions_stmt(self, ctx:MontyPythonParser.Functions_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#function_def.
    def visitFunction_def(self, ctx:MontyPythonParser.Function_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#flow_stmt.
    def visitFlow_stmt(self, ctx:MontyPythonParser.Flow_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#break_stmt.
    def visitBreak_stmt(self, ctx:MontyPythonParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#continue_stmt.
    def visitContinue_stmt(self, ctx:MontyPythonParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#compound_stmt.
    def visitCompound_stmt(self, ctx:MontyPythonParser.Compound_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#if_stmt.
    def visitIf_stmt(self, ctx:MontyPythonParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#while_stmt.
    def visitWhile_stmt(self, ctx:MontyPythonParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#for_stmt.
    def visitFor_stmt(self, ctx:MontyPythonParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#function.
    def visitFunction(self, ctx:MontyPythonParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#end_function.
    def visitEnd_function(self, ctx:MontyPythonParser.End_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#suite_func.
    def visitSuite_func(self, ctx:MontyPythonParser.Suite_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#suite.
    def visitSuite(self, ctx:MontyPythonParser.SuiteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#logical_not.
    def visitLogical_not(self, ctx:MontyPythonParser.Logical_notContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#logical_op.
    def visitLogical_op(self, ctx:MontyPythonParser.Logical_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#logical_expr.
    def visitLogical_expr(self, ctx:MontyPythonParser.Logical_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#exprcomp.
    def visitExprcomp(self, ctx:MontyPythonParser.ExprcompContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#comparison.
    def visitComparison(self, ctx:MontyPythonParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#comp_op.
    def visitComp_op(self, ctx:MontyPythonParser.Comp_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#int_expr.
    def visitInt_expr(self, ctx:MontyPythonParser.Int_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#float_expr.
    def visitFloat_expr(self, ctx:MontyPythonParser.Float_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#var_int_expr.
    def visitVar_int_expr(self, ctx:MontyPythonParser.Var_int_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#var_float_expr.
    def visitVar_float_expr(self, ctx:MontyPythonParser.Var_float_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#term_int.
    def visitTerm_int(self, ctx:MontyPythonParser.Term_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#term_float.
    def visitTerm_float(self, ctx:MontyPythonParser.Term_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#term_var_int.
    def visitTerm_var_int(self, ctx:MontyPythonParser.Term_var_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#term_var_float.
    def visitTerm_var_float(self, ctx:MontyPythonParser.Term_var_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#factor_var_int.
    def visitFactor_var_int(self, ctx:MontyPythonParser.Factor_var_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#factor_var_float.
    def visitFactor_var_float(self, ctx:MontyPythonParser.Factor_var_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#factor_int.
    def visitFactor_int(self, ctx:MontyPythonParser.Factor_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#factor_float.
    def visitFactor_float(self, ctx:MontyPythonParser.Factor_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#primary_int.
    def visitPrimary_int(self, ctx:MontyPythonParser.Primary_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#primary_float.
    def visitPrimary_float(self, ctx:MontyPythonParser.Primary_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#expr.
    def visitExpr(self, ctx:MontyPythonParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#term.
    def visitTerm(self, ctx:MontyPythonParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#factor.
    def visitFactor(self, ctx:MontyPythonParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#primary.
    def visitPrimary(self, ctx:MontyPythonParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#input_func.
    def visitInput_func(self, ctx:MontyPythonParser.Input_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#print_stmt.
    def visitPrint_stmt(self, ctx:MontyPythonParser.Print_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MontyPythonParser#arg.
    def visitArg(self, ctx:MontyPythonParser.ArgContext):
        return self.visitChildren(ctx)



del MontyPythonParser