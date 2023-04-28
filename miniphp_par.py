import ply.yacc as yacc
from miniphp_lex import tokens
import miniphp_lex
import sys

VERBOSE = 1
error_found = False

def p_program(p):
    'program : OPENPHP declaration_list CLOSEPHP'
    pass

def p_declaration_list(p):
	'''declaration_list : declaration_list  declaration
                            | declaration
    '''
	pass

def p_declaration(p):
	'''declaration : var_declaration
				        | fun_declaration
                        | statement_list
				        | header_declaration
    '''
	pass

def p_header_declaration(p):
    '''header_declaration : INCLUDE QUOTATIONMARKSD ID DOT PHP QUOTATIONMARKSD SEMICOLON
                            | INCLUDE QUOTATIONMARKSS ID DOT PHP QUOTATIONMARKSS SEMICOLON
                            | REQUIRE QUOTATIONMARKSD ID DOT PHP QUOTATIONMARKSD SEMICOLON
                            | REQUIRE QUOTATIONMARKSS ID DOT PHP QUOTATIONMARKSS SEMICOLON
    '''
    pass

def p_var_declaration_1(p):
    'var_declaration : var_declaration2 SEMICOLON'
    pass

def p_var_declaration_2(p):
    '''var_declaration2 : VARI COMMA var_declaration2
                        | VARI
                        | VARI EQUAL QUOTATIONMARKSS text QUOTATIONMARKSS COMMA var_declaration2
                        | VARI EQUAL QUOTATIONMARKSS text QUOTATIONMARKSS
                        | VARI EQUAL VARI COMMA var_declaration2
                        | VARI EQUAL VARI
                        | VARI EQUAL NUMBER COMMA var_declaration2
                        | VARI EQUAL NUMBER
                        | VARI EQUAL var_declaration2
                        | VARI EQUAL AMPERSANT VARI COMMA var_declaration2
                        | VARI EQUAL AMPERSANT VARI'''
    pass


def p_fun_declaration(p):
    '''fun_declaration : FUNCTION ID LPAREN params RPAREN fun_body'''
    pass


def p_params(p):
    '''params : var_declaration2
              | empty'''
    pass

def p_fun_body(p):
    '''fun_body : LBLOCK local_declarations statement_list RBLOCK'''
    pass

def p_local_declarations(p):
    '''local_declarations : local_declarations var_declaration
                          | empty'''
    pass

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | empty'''
    pass


def p_statement(p):
    '''statement : expression_statement
                | print_statement
                | selection_statement
                | iteration_statement
                | return_statement'''
    pass

def p_expression_statement(p):
    '''expression_statement : expression SEMICOLON
                            | SEMICOLON'''
    pass


def p_print_statement(p):
    '''print_statement : ECHO print_statement2 SEMICOLON
                         | ECHO QUOTATIONMARKSD print_statement2 QUOTATIONMARKSD'''
    pass


def p_print_statement2(p):
    '''print_statement2 : VARI COMMA print_statement2
                         | VARI
                         | text
                         | NUMBER'''
    pass

def p_text(p):
    '''text : text ID
             | ID'''
    pass

def p_selection_statement(p):
    """selection_statement : IF LPAREN expression RPAREN statement_block
                           | IF LPAREN expression RPAREN statement_block ELSE statement_block
                           | SWITCH LPAREN VARI RPAREN LBLOCK statement RBLOCK
                           | CASE NUMBER COLON statement BREAK SEMICOLON
                           | DEFAULT COLON statement BREAK SEMICOLON"""
    pass


def p_iteration_statement(p):
    """iteration_statement : WHILE LPAREN expression RPAREN statement_block
                           | FOR LPAREN var_declaration2 SEMICOLON expression SEMICOLON additive_expression RPAREN statement_block"""
    pass

def p_statement_block(p):
    """statement_block : LBLOCK statement_list RBLOCK
                       | statement"""
    pass

def p_return_statement(p):
    """return_statement : RETURN SEMICOLON
                        | RETURN expression SEMICOLON
                        | RETURN ID LPAREN params RPAREN SEMICOLON"""
    pass

def p_expression(p):
    """expression : var EQUAL expression
                  | simple_expression"""
    pass


def p_var(p):
    """var : VARI
           | VARI LBRACKET NUMBER RBRACKET
           | VARI LBRACKET VARI RBRACKET"""
    pass

def p_simple_expression(p):
    """simple_expression : additive_expression relop additive_expression
                         | additive_expression"""
    pass


def p_additive_expression(p):
    """additive_expression : additive_expression addop term
                           | term
                           | term MINUSMINUS
                           | term PLUSPLUS"""
    pass



def p_relop(p):
    """relop : LESS
            | LESSEQUAL
            | GREATER
            | GREATEREQUAL
            | DISTINTEQUAL
            | EQUALEQUAL
    """
    pass

def p_addop(p):
    """addop : PLUS
            | MINUS
    """
    pass

def p_mulop(p):
    """mulop : TIMES
            | DIVIDE"""
    pass

def p_term(p):
    """term : term mulop factor
            | factor"""
    pass

def p_factor(p):
    """factor : LPAREN expression RPAREN
              | var
              | NUMBER"""
    pass

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    global error_found
    error_found = True
    if VERBOSE == 1:
        if p is not None:
            print("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL TOKEN  " + str(p.value))
        else:
            print("ERROR SINTACTICO EN LA LINEA: " + str(miniphp_lex.lexer.lineno))
    else:
        raise Exception('syntax', 'error')

parser = yacc.yacc()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file = sys.argv[1]
    else:
        file = 'test.php'
    f = open(file, 'r')
    data = f.read()
    parser.parse(data, tracking=True)
    
    if not error_found: 
        print("El analisis sintactico ha finalizado correctamente")
    
