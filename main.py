from lexico import tokens
import ply.yacc as yacc



# Inicio Contribucion Viviana Velasco
# Funcion


def p_parametrosF(p):
    'parametrosF : parametro COMMA parametrosF | parametro'


def p_parametro(p):
    'parametro : DATATYPES ID '


def p_funcion(p):
    'funcion : STATIC DATATYPES ID LPAREN parametrosF RPAREN CURLYBRACKETLEFT instruccionesMas CURLYBRACKETRIGHT | DATATYPES ID LPAREN parametrosF RPAREN CURLYBRACKETLEFT instruccionesMas CURLYBRACKETRIGHT | VOID ID LPAREN parametrosF RPAREN CURLYBRACKETLEFT instruccionesMas CURLYBRACKETRIGHT '
#Sentencia Return y Retornar Values hecho por David Terreros
def p_sentenciaReturn(p):
    '''sentenciaReturn : RETURN LPAREN retornarValues RPAREN SEMICOLON'''


def p_retornarValues(p):
    '''retornarValues : values
    | NULL'''

# If condicion
def p_operadorcondicion(p):
    'operadorcondicion : EQUALC | GREATER | LESS | DIFFERENT | GREATEREQ | LESSEQ '



def p_sentenciaIf(p):
    'sentenciaIf : IF LPAREN comparacion RPAREN CURLYBRACKETLEFT instruccionesMas CURLYBRACKETRIGHT '


def p_sentenciaElse(p):
    'sentenciaElse : ELSE CURLYBRACKETLEFT instruccionesMas CURLYBRACKETRIGHT | ELSE sentenciaIf p_sentenciaElse | ELSE sentenciaIf'


def p_sentenciaIfElse(p):
    'sentenciaIfElse : sentenciaIf | sentenciaIf sentenciaElse'

# Sets


def p_set(p):
    '''set : values COMMA set 
    | values'''


def p_declarset(p):
    '''declarset : SET ID EQUAL NEW SET LPAREN RPAREN SEMICOLON
    | SET ID EQUAL CURLYBRACKETLEFT set CURLYBRACKETRIGHT SEMICOLON
    | DATATYPES ID EQUAL LESS DATATYPES GREATER CURLYBRACKETLEFT set CURLYBRACKETRIGHT SEMICOLON
    | setadd
    | setclear
    | setcontains
    | setAddAll
    | setlengh
    | setremove'''


def p_setadd(p):
    'setadd : ID DOT ADD LPAREN values RPAREN SEMICOLON'


def p_setclear(p):
    '''setclear : ID DOT CLEAR LPAREN values RPAREN SEMICOLON'''


def p_setcontains(p):
    '''setcontains : ID DOT CONTAINS LPAREN values RPAREN SEMICOLON'''


def p_setAddAll(p):
    '''setAddAll : ID DOT ADDALL LPAREN ID RPAREN SEMICOLON'''

def p_setlengh(p):
    '''setlengh : ID DOT LENGTH SEMICOLON'''

def p_setremove(p):
    '''setremove : ID DOT REMOVE LPAREN values RPAREN SEMICOLON'''

#foreach
def p_foreach(p):
    '''foreach : ID DOT FOREACH  LPAREN instruccionesMas RPAREN SEMICOLON'''

#List

def p_array(p):
    '''array :  ID EQUAL  arrayInicio SEMICOLON
    | ID EQUAL  arrayInicio SEMICOLON
    | arrayFunc SEMICOLON'''

def p_arrayInicio(p):
    '''arrayInicio :  SQUAREBRACKETLEFT SQUAREBRACKETRIGHT
    | SQUAREBRACKETLEFT set SQUAREBRACKETRIGHT
    | ID DOT subArray'''

def p_arrayFunc(p):
    '''arrayFunc : ID POINT subArray'''

def p_listBuscar(p):
    '''listBuscar : ID DOT LENGTH SEMICOLON'''

def p_arrayChanges(p):
    '''arrayChanges : ID SQUAREBRACKETLEFT value SQUAREBRACKETRIGHT EQUAL value SEMICOLON'''

def p_subArray(p):
    '''subArray :  SUBLIST LPAREN values RPAREN
    | subArray POINT subArray'''

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
    '''comparacion: ID comparador values 
    | ID  comparador ID 
    | BOOLEAN'''


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
