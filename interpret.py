import ply.yacc as yacc
from lexer_l import tokens

# Определение синтаксических правил с учетом токена STRING
# (обновленные правила для операторов, скобок и добавленное правило для строки)

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MULTIPLY expression
                  | expression DIVIDE expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_string(p):
    'expression : STRING'
    p[0] = p[1]

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_brace(p):
    'expression : LBRACE expression RBRACE'
    p[0] = p[2]

def p_expression_bracket(p):
    'expression : LBRACKET expression RBRACKET'
    p[0] = p[2]

def p_error(p):
    print("Синтаксическая ошибка:", p)

# Создание парсера
parser = yacc.yacc()

# Функция интерпретации выражения
def interpret_expression(expression):
    result = parser.parse(expression)
    return result

# Пример использования интерпретатора с поддержкой строки
data = '2 + (2 * 2)'
result = interpret_expression(data)
print(result)
