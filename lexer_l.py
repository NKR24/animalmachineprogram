import ply.lex as lex
import ply.yacc as yacc

# Определение лексем (токенов)
tokens = (
    'NUMBER',
    'STRING',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'RBRACE',
    'LBRACE',
    'RBRACKET',
    'LBRACKET',
    'ANIMALS'
)

# Определение регулярных выражений для токенов
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'

# Определение регулярного выражения для токена NUMBER
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Определение регулярного выражения для токена STRING
def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]
    return t

# Функция для определения токена ANIMALS
def t_ANIMALS(t):
    r'cat|dog|elephant|lion|tiger'  # Регулярное выражение для определения токена ANIMALS
    return t

# Определение игнорируемых символов (пробелы и табуляции)
t_ignore = ' \t'

# Обработка ошибок лексического анализа
def t_error(t):
    print("Нераспознанный символ:", t.value[0])
    t.lexer.skip(1)

# Создание лексера
lexer = lex.lex()
