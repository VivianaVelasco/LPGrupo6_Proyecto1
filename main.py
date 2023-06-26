from lexico import tokens
import ply.yacc as yacc

# Inicio Contribucion Viviana Velasco


def p_condiciones(p):
    'condicion : BOOLEAN | ID EQUALC ID | ID GREATER ID | ID LESS ID | ID DIFFERENT ID | ID GREATEREQ ID | ID LESSEQ ID'


def p_condicionif(p):
    'condicionif: IF LPAREN condicion RPAREN CURLYBRACKETLEFT CURLYBRACKETRIGHT'
# Inicio Contribucion Viviana Velasco
# Funcion


def p_parametrosF(p):
    'parametrosF : parametro COMA parametrosF | parametro'


def p_parametro(p):
    'parametro : DATATYPES ID '


def p_funcion(p):
    'funcion : STATIC DATATYPES ID LPAREN parametrosF RPAREN CURLYBRACKETLEFT instruccionesMas CURLYBRACKETRIGHT | DATATYPES ID LPAREN parametrosF RPAREN CURLYBRACKETLEFT instruccionesMas CURLYBRACKETRIGHT | VOID ID LPAREN parametrosF RPAREN CURLYBRACKETLEFT instruccionesMas CURLYBRACKETRIGHT '


# If condicion
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

# Sets


def p_set(p):
    'set : values Coma set | values '


def p_declarst(p):
    'declarset: SET ID EQUAL NEW SET LPAREN RPAREN SEMICOLON | SET ID EQUAL CURLYBRACKETLEFT set CURLYBRACKETRIGHT SEMICOLON | DATATYPES ID EQUAL'


def p_setadd(p):
    'setadd : ID DOT ADD LPAREN values RPAREN SEMICOLON'


def p_setclear(p):
    'setclear : ID DOT CLEAR LPAREN values RPAREN SEMICOLON'


def p_setcontains(p):
    'setcontains : ID DOT CONTAINS LPAREN values RPAREN SEMICOLON'


def p_setAddAll(p):
    "setAddAll : ID DOT ADDALL LPAREN id RPAREN SEMICOLON"

# Fin de Contribucion Viviana Velasco
# Contribuccion de David Terreros => Map, For y Funcion Normal.


def p_instruccionesMas(p):
    '''instruccionesMas : instruccion 
    | instruccion instruccionesMas
    '''


def p_instruccion(p):
    '''instruccion : asignacion
    | sentenciaFor
    | condicionif
    | funcion
    '''


def p_asignacion(p):
    '''asignacion : DATATYPES ID EQUAL VALUES SEMICOLON
    | VARTYPE ID EQUAL VALUES SEMICOLON
    | DATATYPES ID operadoresAsignacion VALUES SEMICOLON
    '''


def p_values(p):
    '''values : INT
    | FLOAT
    | BOOLEAN
    | STR
    '''


def p_setenciaReturn(p):
    '''setenciaReturn : RETURN LPAREN retornarValues RPAREN SEMICOLON'''


def p_retornarValues(p):
    '''retornarValues : values
    | NULL'''
# Map David Terreros


def p_estructuraMap(p):
    '''estructuraMap : MAP ID EQUAL CURLYBRACKETLEFT p_itemsMaps CURLYBRACKETRIGHT SEMICOLON 
    | MAP LESS DATATYPES COMMA DATATYPES GREATER ID EQUAL CURLYBRACKETLEFT p_itemsMaps CURLYBRACKETRIGHT SEMICOLON 
    | VARTPE ID EQUAL CURLYBRACKETLEFT p_itemsMaps CURLYBRACKETRIGHT SEMICOLON 
    | VARTPE ID EQUAL NEW MAP LPAREN RPAREN SEMICOLON
    | VARTPE ID EQUAL NEW MAP LESS DATATYPES COMMA DATATYPES GREATER LPAREN RPAREN SEMICOLON'''


def p_itemsMaps(p):
    '''itemsMaps : values COLON values
    | values COLON values COMMA itemsMaps'''


# Estructura de Control David Terreros


def p_sentenciaFor(p):
    '''sentenciaFor : FOR LPAREN asignacion SEMICOLON p_comparacion SEMICOLON operadoresArimeticoId RPAREN CURLYBRACKETLEFT instruccionesMas CURLYBRACKETRIGHT'''


def p_comparacion(p):
    '''comparacion: ID comparador values'''


def comparador(p):
    '''comparador: GREATER
    | LESS
    | GREATEREQ
    | LESSEQ
    | EQUALC
    | DIFFERENT'''


def p_operadoresLogicos(p):
    '''operadoresLogicos : AND
    | OR
    | NOT'''


def p_operadoresArimeticoId(p):
    '''operadoresArimeticoId : ID INCREMENT
    | ID DECREMENT
    | ID MULTIPLUS values
    | ID MULTIPLUS values
    | ID DIVIDEEQUAL values'''


def p_operadoresAsignacion(p):
    '''operadoresAsignacion : PLUSEQUAL 
    | MINUSEQUAL
    | MULTIPLUS
    | DIVIDEEQUAL'''


# INICIO Funciones David Terreros
def p_metodoMapClear(p):
    '''metodoMapClear : ID DOT CLEAR LPAREN RPAREN SEMICOLON'''


def p_metodoMapRemoveKey(p):
    '''metodoMapClear : ID DOT CLEAR LPAREN VALUES RPAREN SEMICOLON'''


def p_metodoMapAddAll(p):
    '''metodoMapClear : ID DOT CLEAR LPAREN CURLYBRACKETLEFT itemsMaps CURLYBRACKETRIGHT RPAREN SEMICOLON'''


def p_metodoMapAdd(p):
    '''metodoMapAdd : ID SQUAREBRACKETRIGHT values SQUAREBRACKETLEFT EQUAL values SEMICOLON'''
# FIN Funciones David Terreros


def p_error(p):
    if p:
        print("Error de sintaxis en token:", p.type)
    else:
        print("Syntax error at EOF")


# Build the parser
sintactico = yacc.yacc()

# Testear Codigo
data = '''
void combSort(List list) {
  int gpVal = list.length;
  double shrink = 1.3;
  bool sortedBool = false;

  while (!sortedBool) {
    gpVal = (gpVal / shrink).floor();
    if (gpVal > 1) {
      sortedBool = false;
    } else {
      gpVal = 1;
      sortedBool = true;
    }

    int i = 0;
    while (i + gpVal < list.length) {
      if (list[i] > list[i + gpVal]) {
        swap(list, i, gpVal);
        sortedBool = false;
      }
      i++;
    }
  }
}

// function to swap the values
void swap(List list, int i, int gpVal) {
  int temp = list[i];
  list[i] = list[i + gpVal];
  list[i + gpVal] = temp;
}

void main() {
  //Get the dummy array
  List arr = [1, 451, 562, 2, 99, 78, 5];
  // for printing the array before sorting
  print("Before sorting the array: $arr\n");
  // applying combSort function
  combSort(arr);
  // printing the sortedBool value
  print("After sorting the array: $arr");
}
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
