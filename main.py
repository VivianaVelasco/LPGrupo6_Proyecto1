from lexico import tokens
import ply.yacc as yacc

#Inicio Contribucion Viviana Velasco
def p_condiciones(p):
    'condicion : BOOLEAN | ID EQUALC ID | ID GREATER ID | ID LESS ID | ID DIFFERENT ID | ID GREATEREQ ID | ID LESSEQ ID'

def p_condicionif(p):
   'condicionif: IF LPAREN condicion RPAREN CURLYBRACKETLEFT CURLYBRACKETRIGHT'




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