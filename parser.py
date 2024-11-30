import ply.yacc as yacc
from lexer import tokens

# Precedência dos operadores
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
)

# Regras gramaticais
def p_program(p):
    '''program : decl_var_list stmt_list'''
    pass

def p_decl_var_list(p):
    '''decl_var_list : decl_var_list decl_var
                     | empty'''
    pass

def p_decl_var(p):
    '''decl_var : type id_list SEMICOLON'''
    pass

def p_type(p):
    '''type : INT
            | FLOAT
            | DOUBLE
            | CHAR'''
    pass

def p_id_list(p):
    '''id_list : id_list COMMA IDENTIFIER
               | IDENTIFIER'''
    pass

def p_stmt_list(p):
    '''stmt_list : stmt_list stmt
                 | empty'''
    pass

def p_stmt(p):
    '''stmt : if_stmt
            | switch_stmt
            | while_stmt
            | for_stmt
            | assign_expr SEMICOLON'''
    pass

def p_if_stmt(p):
    '''if_stmt : IF LEFT_PAREN condition RIGHT_PAREN LEFT_BRACE stmt_list RIGHT_BRACE else_part'''
    pass

def p_else_part(p):
    '''else_part : ELSE LEFT_BRACE stmt_list RIGHT_BRACE
                 | empty'''
    pass

def p_switch_stmt(p):
    '''switch_stmt : SWITCH LEFT_PAREN IDENTIFIER RIGHT_PAREN LEFT_BRACE case_list default_part RIGHT_BRACE'''
    pass

def p_case_list(p):
    '''case_list : case_list case_item
                 | empty'''
    pass

def p_case_item(p):
    '''case_item : CASE NUMBER COLON stmt_list BREAK SEMICOLON
                 | CASE NUMBER COLON stmt_list'''
    pass

def p_default_part(p):
    '''default_part : DEFAULT COLON stmt_list
                    | empty'''
    pass

def p_while_stmt(p):
    '''while_stmt : WHILE LEFT_PAREN condition RIGHT_PAREN LEFT_BRACE stmt_list RIGHT_BRACE'''
    pass

def p_for_stmt(p):
    '''for_stmt : FOR LEFT_PAREN assign_expr SEMICOLON condition SEMICOLON assign_expr RIGHT_PAREN LEFT_BRACE stmt_list RIGHT_BRACE'''
    pass

def p_assign_expr(p):
    '''assign_expr : IDENTIFIER ASSIGN expr
                   | IDENTIFIER PLUS_ASSIGN expr
                   | IDENTIFIER MINUS_ASSIGN expr
                   | IDENTIFIER MULTIPLY_ASSIGN expr
                   | IDENTIFIER DIVIDE_ASSIGN expr
                   | IDENTIFIER INCREMENT
                   | IDENTIFIER DECREMENT'''
    pass

def p_expr(p):
    '''expr : expr PLUS expr
            | expr MINUS expr
            | expr MULTIPLY expr
            | expr DIVIDE expr
            | LEFT_PAREN expr RIGHT_PAREN
            | NUMBER
            | IDENTIFIER'''
    pass

def p_condition(p):
    '''condition : expr relational_operator expr'''
    pass

def p_relational_operator(p):
    '''relational_operator : EQUAL
                           | NOT_EQUAL
                           | LESS_EQUAL
                           | GREATER_EQUAL
                           | LESS_THAN
                           | GREATER_THAN'''
    pass

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    if p:
        message = f"Erro de sintaxe em '{p.value}' na linha {p.lineno}"
        raise SyntaxError(message)
    else:
        message = "Erro de sintaxe no final do arquivo"
        raise SyntaxError(message)

parser = yacc.yacc()
