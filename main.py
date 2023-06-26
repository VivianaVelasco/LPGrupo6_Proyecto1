from lexico import tokens
import ply.yacc as yacc

#Inicio Contribucion Viviana Velasco
#Funcion 
def p_parametrosF(p):
   'parametrosF : parametro COMA parametrosF | parametro'

def p_parametro(p):
   'parametro : DATATYPES ID '

def p_funcion(p):
   'funcion : STATIC DATATYPES ID LPAREN parametrosF RPAREN CURLYBRACKETLEFT instruccionesMas CURLYBRACKETRIGHT | DATATYPES ID LPAREN parametrosF RPAREN CURLYBRACKETLEFT instruccionesMas CURLYBRACKETRIGHT | VOID ID LPAREN parametrosF RPAREN CURLYBRACKETLEFT instruccionesMas CURLYBRACKETRIGHT '


#If condicion
def p_operadorcondicion(p):
   'operadorcondicion : EQUALC | GREATER | LESS | DIFFERENT | GREATEREQ | LESSEQ '


def p_condiciones(p):
    'condicion : BOOLEAN | ID operadorcondicion ID '


def p_sentenciaIf(p):
   'sentenciaIf : IF LPAREN condicion RPAREN CURLYBRACKETLEFT instruccionesMas CURLYBRACKETRIGHT '

def p_sentenciaElse(p):
   'sentenciaElse : ELSE CURLYBRACKETLEFT instruccionesMas CURLYBRACKETRIGHT | ELSE sentenciaIf p_sentenciaElse | ELSE sentenciaIf'

def p_sentenciaIfElse(p):
   'sentenciaIfElse : sentenciaIf | sentenciaIf sentenciaElse'

#Sets

def p_set(p):
   'set : values Coma set | values '

def p_declarst(p):
   'declarset: SET ID EQUAL NEW SET LPAREN RPAREN SEMICOLON | SET ID EQUAL CURLYBRACKETLEFT set CURLYBRACKETRIGHT SEMICOLON'

def p_setadd(p):
   'setadd : ID DOT ADD LPAREN values RPAREN SEMICOLON'

def p_setclear(p):
   'setclear : ID DOT CLEAR LPAREN values RPAREN SEMICOLON'

def p_setcontains(p):
   'setcontains : ID DOT CONTAINS LPAREN values RPAREN SEMICOLON'


#Fin de Contribucion Viviana Velasco
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