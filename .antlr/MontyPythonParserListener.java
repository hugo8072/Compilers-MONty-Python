// Generated from d:/Downloads/Compilador(2)-novo/Compilador-novo/MontyPythonParser.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link MontyPythonParser}.
 */
public interface MontyPythonParserListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#file_input}.
	 * @param ctx the parse tree
	 */
	void enterFile_input(MontyPythonParser.File_inputContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#file_input}.
	 * @param ctx the parse tree
	 */
	void exitFile_input(MontyPythonParser.File_inputContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#stmt}.
	 * @param ctx the parse tree
	 */
	void enterStmt(MontyPythonParser.StmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#stmt}.
	 * @param ctx the parse tree
	 */
	void exitStmt(MontyPythonParser.StmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#simple_stmt}.
	 * @param ctx the parse tree
	 */
	void enterSimple_stmt(MontyPythonParser.Simple_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#simple_stmt}.
	 * @param ctx the parse tree
	 */
	void exitSimple_stmt(MontyPythonParser.Simple_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#small_stmt}.
	 * @param ctx the parse tree
	 */
	void enterSmall_stmt(MontyPythonParser.Small_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#small_stmt}.
	 * @param ctx the parse tree
	 */
	void exitSmall_stmt(MontyPythonParser.Small_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#expr_stmt}.
	 * @param ctx the parse tree
	 */
	void enterExpr_stmt(MontyPythonParser.Expr_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#expr_stmt}.
	 * @param ctx the parse tree
	 */
	void exitExpr_stmt(MontyPythonParser.Expr_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#list_stmt}.
	 * @param ctx the parse tree
	 */
	void enterList_stmt(MontyPythonParser.List_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#list_stmt}.
	 * @param ctx the parse tree
	 */
	void exitList_stmt(MontyPythonParser.List_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#list_op}.
	 * @param ctx the parse tree
	 */
	void enterList_op(MontyPythonParser.List_opContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#list_op}.
	 * @param ctx the parse tree
	 */
	void exitList_op(MontyPythonParser.List_opContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#functions_stmt}.
	 * @param ctx the parse tree
	 */
	void enterFunctions_stmt(MontyPythonParser.Functions_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#functions_stmt}.
	 * @param ctx the parse tree
	 */
	void exitFunctions_stmt(MontyPythonParser.Functions_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#function_def}.
	 * @param ctx the parse tree
	 */
	void enterFunction_def(MontyPythonParser.Function_defContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#function_def}.
	 * @param ctx the parse tree
	 */
	void exitFunction_def(MontyPythonParser.Function_defContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#flow_stmt}.
	 * @param ctx the parse tree
	 */
	void enterFlow_stmt(MontyPythonParser.Flow_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#flow_stmt}.
	 * @param ctx the parse tree
	 */
	void exitFlow_stmt(MontyPythonParser.Flow_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#break_stmt}.
	 * @param ctx the parse tree
	 */
	void enterBreak_stmt(MontyPythonParser.Break_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#break_stmt}.
	 * @param ctx the parse tree
	 */
	void exitBreak_stmt(MontyPythonParser.Break_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#continue_stmt}.
	 * @param ctx the parse tree
	 */
	void enterContinue_stmt(MontyPythonParser.Continue_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#continue_stmt}.
	 * @param ctx the parse tree
	 */
	void exitContinue_stmt(MontyPythonParser.Continue_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#compound_stmt}.
	 * @param ctx the parse tree
	 */
	void enterCompound_stmt(MontyPythonParser.Compound_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#compound_stmt}.
	 * @param ctx the parse tree
	 */
	void exitCompound_stmt(MontyPythonParser.Compound_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#if_stmt}.
	 * @param ctx the parse tree
	 */
	void enterIf_stmt(MontyPythonParser.If_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#if_stmt}.
	 * @param ctx the parse tree
	 */
	void exitIf_stmt(MontyPythonParser.If_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#while_stmt}.
	 * @param ctx the parse tree
	 */
	void enterWhile_stmt(MontyPythonParser.While_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#while_stmt}.
	 * @param ctx the parse tree
	 */
	void exitWhile_stmt(MontyPythonParser.While_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#for_stmt}.
	 * @param ctx the parse tree
	 */
	void enterFor_stmt(MontyPythonParser.For_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#for_stmt}.
	 * @param ctx the parse tree
	 */
	void exitFor_stmt(MontyPythonParser.For_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#function}.
	 * @param ctx the parse tree
	 */
	void enterFunction(MontyPythonParser.FunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#function}.
	 * @param ctx the parse tree
	 */
	void exitFunction(MontyPythonParser.FunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#end_function}.
	 * @param ctx the parse tree
	 */
	void enterEnd_function(MontyPythonParser.End_functionContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#end_function}.
	 * @param ctx the parse tree
	 */
	void exitEnd_function(MontyPythonParser.End_functionContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#suite_func}.
	 * @param ctx the parse tree
	 */
	void enterSuite_func(MontyPythonParser.Suite_funcContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#suite_func}.
	 * @param ctx the parse tree
	 */
	void exitSuite_func(MontyPythonParser.Suite_funcContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#suite}.
	 * @param ctx the parse tree
	 */
	void enterSuite(MontyPythonParser.SuiteContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#suite}.
	 * @param ctx the parse tree
	 */
	void exitSuite(MontyPythonParser.SuiteContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#logical_not}.
	 * @param ctx the parse tree
	 */
	void enterLogical_not(MontyPythonParser.Logical_notContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#logical_not}.
	 * @param ctx the parse tree
	 */
	void exitLogical_not(MontyPythonParser.Logical_notContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#logical_op}.
	 * @param ctx the parse tree
	 */
	void enterLogical_op(MontyPythonParser.Logical_opContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#logical_op}.
	 * @param ctx the parse tree
	 */
	void exitLogical_op(MontyPythonParser.Logical_opContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#logical_expr}.
	 * @param ctx the parse tree
	 */
	void enterLogical_expr(MontyPythonParser.Logical_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#logical_expr}.
	 * @param ctx the parse tree
	 */
	void exitLogical_expr(MontyPythonParser.Logical_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#exprcomp}.
	 * @param ctx the parse tree
	 */
	void enterExprcomp(MontyPythonParser.ExprcompContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#exprcomp}.
	 * @param ctx the parse tree
	 */
	void exitExprcomp(MontyPythonParser.ExprcompContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#comparison}.
	 * @param ctx the parse tree
	 */
	void enterComparison(MontyPythonParser.ComparisonContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#comparison}.
	 * @param ctx the parse tree
	 */
	void exitComparison(MontyPythonParser.ComparisonContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#comp_op}.
	 * @param ctx the parse tree
	 */
	void enterComp_op(MontyPythonParser.Comp_opContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#comp_op}.
	 * @param ctx the parse tree
	 */
	void exitComp_op(MontyPythonParser.Comp_opContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#int_expr}.
	 * @param ctx the parse tree
	 */
	void enterInt_expr(MontyPythonParser.Int_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#int_expr}.
	 * @param ctx the parse tree
	 */
	void exitInt_expr(MontyPythonParser.Int_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#float_expr}.
	 * @param ctx the parse tree
	 */
	void enterFloat_expr(MontyPythonParser.Float_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#float_expr}.
	 * @param ctx the parse tree
	 */
	void exitFloat_expr(MontyPythonParser.Float_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#var_int_expr}.
	 * @param ctx the parse tree
	 */
	void enterVar_int_expr(MontyPythonParser.Var_int_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#var_int_expr}.
	 * @param ctx the parse tree
	 */
	void exitVar_int_expr(MontyPythonParser.Var_int_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#var_float_expr}.
	 * @param ctx the parse tree
	 */
	void enterVar_float_expr(MontyPythonParser.Var_float_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#var_float_expr}.
	 * @param ctx the parse tree
	 */
	void exitVar_float_expr(MontyPythonParser.Var_float_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#term_int}.
	 * @param ctx the parse tree
	 */
	void enterTerm_int(MontyPythonParser.Term_intContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#term_int}.
	 * @param ctx the parse tree
	 */
	void exitTerm_int(MontyPythonParser.Term_intContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#term_float}.
	 * @param ctx the parse tree
	 */
	void enterTerm_float(MontyPythonParser.Term_floatContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#term_float}.
	 * @param ctx the parse tree
	 */
	void exitTerm_float(MontyPythonParser.Term_floatContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#term_var_int}.
	 * @param ctx the parse tree
	 */
	void enterTerm_var_int(MontyPythonParser.Term_var_intContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#term_var_int}.
	 * @param ctx the parse tree
	 */
	void exitTerm_var_int(MontyPythonParser.Term_var_intContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#term_var_float}.
	 * @param ctx the parse tree
	 */
	void enterTerm_var_float(MontyPythonParser.Term_var_floatContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#term_var_float}.
	 * @param ctx the parse tree
	 */
	void exitTerm_var_float(MontyPythonParser.Term_var_floatContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#factor_var_int}.
	 * @param ctx the parse tree
	 */
	void enterFactor_var_int(MontyPythonParser.Factor_var_intContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#factor_var_int}.
	 * @param ctx the parse tree
	 */
	void exitFactor_var_int(MontyPythonParser.Factor_var_intContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#factor_var_float}.
	 * @param ctx the parse tree
	 */
	void enterFactor_var_float(MontyPythonParser.Factor_var_floatContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#factor_var_float}.
	 * @param ctx the parse tree
	 */
	void exitFactor_var_float(MontyPythonParser.Factor_var_floatContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#factor_int}.
	 * @param ctx the parse tree
	 */
	void enterFactor_int(MontyPythonParser.Factor_intContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#factor_int}.
	 * @param ctx the parse tree
	 */
	void exitFactor_int(MontyPythonParser.Factor_intContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#factor_float}.
	 * @param ctx the parse tree
	 */
	void enterFactor_float(MontyPythonParser.Factor_floatContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#factor_float}.
	 * @param ctx the parse tree
	 */
	void exitFactor_float(MontyPythonParser.Factor_floatContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#primary_int}.
	 * @param ctx the parse tree
	 */
	void enterPrimary_int(MontyPythonParser.Primary_intContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#primary_int}.
	 * @param ctx the parse tree
	 */
	void exitPrimary_int(MontyPythonParser.Primary_intContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#primary_float}.
	 * @param ctx the parse tree
	 */
	void enterPrimary_float(MontyPythonParser.Primary_floatContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#primary_float}.
	 * @param ctx the parse tree
	 */
	void exitPrimary_float(MontyPythonParser.Primary_floatContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(MontyPythonParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(MontyPythonParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm(MontyPythonParser.TermContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm(MontyPythonParser.TermContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(MontyPythonParser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(MontyPythonParser.FactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#primary}.
	 * @param ctx the parse tree
	 */
	void enterPrimary(MontyPythonParser.PrimaryContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#primary}.
	 * @param ctx the parse tree
	 */
	void exitPrimary(MontyPythonParser.PrimaryContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#input_func}.
	 * @param ctx the parse tree
	 */
	void enterInput_func(MontyPythonParser.Input_funcContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#input_func}.
	 * @param ctx the parse tree
	 */
	void exitInput_func(MontyPythonParser.Input_funcContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#print_stmt}.
	 * @param ctx the parse tree
	 */
	void enterPrint_stmt(MontyPythonParser.Print_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#print_stmt}.
	 * @param ctx the parse tree
	 */
	void exitPrint_stmt(MontyPythonParser.Print_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MontyPythonParser#arg}.
	 * @param ctx the parse tree
	 */
	void enterArg(MontyPythonParser.ArgContext ctx);
	/**
	 * Exit a parse tree produced by {@link MontyPythonParser#arg}.
	 * @param ctx the parse tree
	 */
	void exitArg(MontyPythonParser.ArgContext ctx);
}