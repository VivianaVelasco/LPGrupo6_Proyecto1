from lexico import tokens
import ply.yacc as yacc

#Inicio Contribucion Viviana Velasco
def p_condiciones(p):
    'condicion : BOOLEAN | ID EQUALC ID | ID GREATER ID | ID LESS ID | ID DIFFERENT ID | ID GREATEREQ ID | ID LESSEQ ID'

def p_condicionif(p):
   'condicionif: IF LPAREN condicion RPAREN CURLYBRACKETLEFT CURLYBRACKETRIGHT'


# Contribuccion de David Terreros => Map, For y Funcion Normal.

def p_instruccionesMas(p):
  '''instruccionesMas : instruccion 
  | instruccion instruccionesMas
  '''

def p_instruccion(p):
  '''instruccion : asignacion
  |
  '''

def p_asignacion(p):
  '''asignacion : DATATYPES ID EQUAL VALUES SEMICOLON
  '''

def p_values(p):
  '''values : INT
  | FLOAT
  | BOOLEAN
  | STRING
  '''

def p_estructuraMap(p):
   '''estructuraMap : '''

def p_sentenciaIf(p):
   '''sentenciaIf :'''

def p_funcion(p):
   '''funcion :'''


def p_error(p):
  if p:
    print("Error de sintaxis en token:", p.type)
  else:
    print("Syntax error at EOF")

# Build the parser
sintactico = yacc.yacc()

# Testear Codigo
data = '''

'''

# Correr
for i, linea in data:
    sintactico.parse(linea)

# while True:
  # try:
  #   s = input('dart > ')
  # except EOFError:
  #   break
  # if not data: continue
  # result = sintactico.parse(data)
  # if result != None: print(result)