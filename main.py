from lexico import tokens
import ply.yacc as yacc



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

while True:
  # try:
  #   s = input('dart > ')
  # except EOFError:
  #   break
  if not data: continue
  result = sintactico.parse(data)
  if result != None: print(result)