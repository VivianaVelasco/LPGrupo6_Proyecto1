import ply.lex as lex

"""Contribucion Viviana Velasco"""

reserved = {
  'abstract': 'ABSTRACT',
  'else': 'ELSE',
  'import': 'IMPORT',
  'show': 'SHOW',
  'as': 'AS',
  'enum': 'ENUM',
  'in': 'IN',
  'static': 'STATIC',
  'assert': 'ASSERT',
  'export': 'EXPORT',
  'interface': 'INTERFACE',
  'super': 'SUPER',
  'async': 'ASYNC',
  'extends': 'EXTENDS',
  'is': 'IS',
  'switch': 'SWITCH',
  'await': 'AWAIT',
  'extension': 'EXTENSION',
  'late': 'LATE',
  'sync': 'SYNC',
  'base': 'BASE',
  'external': 'EXTERNAL',
  'library': 'LIBRARY',
  'this': 'THIS',
  'break': 'BREAK',
  'factory': 'FACTORY',
  'mixin': 'MIXIN',
  'throw': 'THROW',
  'case': 'CASE',
  'false': 'FALSE',
  'new': 'NEW',
  'true': 'TRUE',
  'catch': 'CATCH',
  'final': 'FINAL',
  'null': 'NULL',
  'try': 'TRY',
  'class': 'CLASS',
  'on': 'ON',
  'typedef': 'TYPEDEF',
  'const': 'CONST',
  'finally': 'FINALLY',
  'operator': 'OPERATOR',
  'var': 'VAR',
  'continue': 'CONTINUE',
  'for': 'FOR',
  'part': 'PART',
  'void': 'VOID',
  'covariant': 'COVARIANT',
  'Function': 'FUNCTION',
  'required': 'REQUIRED',
  'when': 'WHEN',
  'default': 'DEFAULT',
  'get': 'GET',
  'rethrow': 'RETHROW',
  'while': 'WHILE',
  'deferred': 'DEFERRED',
  'hide': 'HIDE',
  'return': 'RETURN',
  'with': 'WITH',
  'do': 'DO',
  'if': 'IF',
  'sealed': 'SEALED',
  'yield': 'YIELD',
  'dynamic': 'DYNAMIC',
  'implements': 'IMPLEMENTS',
  'set': 'SET'
}

#Sequencia de tokens, puede ser lista o tupla
tokens = (
  'DATATYPES',
  'PLUS', 
  'MINUS', 
  'TIMES', 
  'DIVIDE', 
  'INT', 
  'FLOAT', 
  'LPAREN', 
  'RPAREN', 
  'ID',
  'EQUAL', 
  'EQUALC', 
  'COMMA', 
  'DIFFERENT', 
  'STR', 
  'GREATER', 
  'LESS', 
  'SEMICOLON', 
  'AND', 
  'OR', 
  'NOT', 
  'LIST', 
  'MAP', 
  'INCREMENT', 
  'DECREMENT',
  'PLUSEQUAL',
  'MINUSEQUAL',
  'MULTIPLUS',
  'DIVIDEEQUAL',
  'MOD',
  'SQUAREBRACKETLEFT',
  'SQUAREBRACKETRIGHT',
  'CURLYBRACKETLEFT',
  'CURLYBRACKETRIGHT',
  'DOLLAR',
  'DOT',
  'QUESTIONMARK',
  'GREATEREQ',
  'LESSEQ',
  'BOOLEAN',
  'MAPTYPE',
  'UNDERSCORE'

) + tuple(reserved.values())

#Exp Regulares para tokens de símbolos
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
"""Fin de Contribucion Viviana Velasco"""

# Contribuccion David Terreros
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_FLOAT = r'-?\d*\.\d+'
t_INT = r'-?\d+'
t_EQUAL = r'='
t_EQUALC = r'=='
t_COMMA = r','
t_DIFFERENT = r'!='
t_STR = r'("[^"]*"|\'[^\']*\')'
t_GREATER = r'>'
t_LESS = r'<'
t_SEMICOLON = r';'
t_AND = r'\&'
t_OR = r'\|'
t_NOT = r'\!'
t_LIST = r'\[\]'
t_MAP = r'\{\}'
t_INCREMENT = r'\+\+'
t_DECREMENT = r'--'
t_MOD = r'%'
t_PLUSEQUAL = r'\+='
t_MINUSEQUAL = r'-='
t_MULTIPLUS = r'\*='
t_DIVIDEEQUAL = r'\/='
t_CURLYBRACKETLEFT = r'\{'
t_CURLYBRACKETRIGHT = r'\}'
t_SQUAREBRACKETRIGHT = r'\]'
t_SQUAREBRACKETLEFT = r'\['
t_DOLLAR = r'\$'
t_DOT = r'\.'
t_QUESTIONMARK = r'\?'
t_GREATEREQ = r'=>'
t_LESSEQ = r'=<'
t_UNDERSCORE = r"_"


def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_DATATYPES(t):
  r"int|double|String|float|bool|num|var|dynamic"
  return t

def t_ID(t):
  r"[_?a-zA-Z][a-zA-Z0-9_]*"
  t.type = reserved.get(t.value.lower(), 'ID')
  return t

def t_MAPTYPE(t):
   r'<>\{\}'
   pass

t_ignore = ' \t'

def t_COMMENT_SIMPLE(t):
    r'\/\/.*'
    pass

def t_COMMENT_DOUBLE(t):
    r'\/\*.*\*\/'
    pass

def t_contarLineas(t):
  r"\n+"
  t.lexer.lineno += len(t.value)

def t_error(t):
  print("Componente léxico no reconocido '%s'" % t.value[0])
  t.lexer.skip(1)

def t_BOOLEAN(t):
  r"(True|False)"
  return t

# FIN de Contribuccion David Terreros.
lexer = lex.lex()

# Test
data = '''
        void main(List<String> args) {
          int _number = 0;
          print(_number);
        }
       '''

def consultarToken(data):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break 
        print(tok)