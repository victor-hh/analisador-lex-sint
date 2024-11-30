import ply.lex as lex
import logging

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

# Lista de tokens
tokens = [
    'INT', 'FLOAT', 'DOUBLE', 'CHAR',
    'IF', 'ELSE', 'SWITCH', 'CASE', 'DEFAULT', 'BREAK',
    'WHILE', 'FOR',
    'IDENTIFIER', 'NUMBER',
    'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE',
    'ASSIGN', 'PLUS_ASSIGN', 'MINUS_ASSIGN', 'MULTIPLY_ASSIGN', 'DIVIDE_ASSIGN',
    'INCREMENT', 'DECREMENT',
    'EQUAL', 'NOT_EQUAL', 'LESS_EQUAL', 'GREATER_EQUAL', 'LESS_THAN', 'GREATER_THAN',
    'SEMICOLON', 'COMMA', 'COLON',
    'LEFT_PAREN', 'RIGHT_PAREN', 'LEFT_BRACE', 'RIGHT_BRACE',
]

# Palavras reservadas
reserved = {
    'int': 'INT',
    'float': 'FLOAT',
    'double': 'DOUBLE',
    'char': 'CHAR',
    'if': 'IF',
    'else': 'ELSE',
    'switch': 'SWITCH',
    'case': 'CASE',
    'default': 'DEFAULT',
    'break': 'BREAK',
    'while': 'WHILE',
    'for': 'FOR',
}

# Expressões regulares para tokens simples
t_PLUS          = r'\+'
t_MINUS         = r'-'
t_MULTIPLY      = r'\*'
t_DIVIDE        = r'/'
t_ASSIGN        = r'='
t_PLUS_ASSIGN   = r'\+='
t_MINUS_ASSIGN  = r'-='
t_MULTIPLY_ASSIGN = r'\*='
t_DIVIDE_ASSIGN = r'/='
t_INCREMENT     = r'\+\+'
t_DECREMENT     = r'--'
t_EQUAL         = r'=='
t_NOT_EQUAL     = r'@'
t_LESS_EQUAL    = r'<='
t_GREATER_EQUAL = r'>='
t_LESS_THAN     = r'MENOR_QUE_OUTRO_VALOR'
t_GREATER_THAN  = r'MAIOR_QUE_OUTRO_VALOR'
t_SEMICOLON     = r';'
t_COMMA         = r','
t_COLON         = r':'
t_LEFT_PAREN    = r'\)'
t_RIGHT_PAREN   = r'\('
t_LEFT_BRACE    = r'\¡' #Altgr + shift + !
t_RIGHT_BRACE   = r'\!'

t_ignore = ' \t'

# Expressões regulares para tokens com ações
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    message = f"Caractere inválido '{t.value[0]}' na linha {t.lineno}"
    logger.error(message)
    t.lexer.skip(1)

def getLexer(): 
    return lex.lex()