from lexico import tokens
import ply.yacc as yacc


def p_instruccionesMas(p):
    '''instruccionesMas : instruccion 
    | instruccion instruccionesMas
    '''


def p_instruccion(p):
    '''instruccion : funcion
    | sentenciaFor
    | sentenciaIf
    | asignacionesMas
    | estructuraMap
    | array
    | arrayChanges
    | declarset
    | sentenciaIfElse
    | sentenciaElse
    | foreach
    | listBuscar
    '''

# Inicio Contribucion Viviana Velasco
# Funcion


def p_parametrosF(p):
    '''parametrosF : parametro COMMA parametrosF
    | parametro
    '''


def p_parametro(p):
    'parametro : DATATYPES ID'


def p_funcion(p):
    '''funcion : STATIC DATATYPES ID LPAREN parametrosF RPAREN CURLYBRACKETLEFT instruccionesMas sentenciaReturn CURLYBRACKETRIGHT
    | DATATYPES ID LPAREN parametrosF RPAREN CURLYBRACKETLEFT instruccionesMas sentenciaReturn CURLYBRACKETRIGHT
    | VOID ID LPAREN parametrosF RPAREN CURLYBRACKETLEFT instruccionesMas sentenciaReturn CURLYBRACKETRIGHT
    '''

# Sentencia Return y Retornar Values hecho por David Terreros


def p_sentenciaReturn(p):
    'sentenciaReturn : RETURN LPAREN retornarValues RPAREN SEMICOLON'


def p_retornarValues(p):
    '''retornarValues : values
    | NULL
    '''


def p_sentenciaIf(p):
    'sentenciaIf : IF LPAREN comparacion RPAREN CURLYBRACKETLEFT instruccionesMas CURLYBRACKETRIGHT'


def p_sentenciaElse(p):
    '''sentenciaElse : ELSE CURLYBRACKETLEFT instruccionesMas CURLYBRACKETRIGHT
    | ELSE sentenciaIf sentenciaElse 
    | ELSE sentenciaIf
    '''


def p_sentenciaIfElse(p):
    '''sentenciaIfElse : sentenciaIf
    | sentenciaIf sentenciaElse
    '''


# Sets
def p_set(p):
    '''set : values COMMA set 
    | values
    '''


def p_declarset(p):
    '''declarset : SET ID EQUAL NEW SET LPAREN RPAREN SEMICOLON
    | SET ID EQUAL CURLYBRACKETLEFT set CURLYBRACKETRIGHT SEMICOLON
    | DATATYPES ID EQUAL LESS DATATYPES GREATER CURLYBRACKETLEFT set CURLYBRACKETRIGHT SEMICOLON
    | setadd
    | setclear
    | setcontains
    | setAddAll
    | setlengh
    | setremove
    '''


def p_setadd(p):
    '''setadd : ID DOT ADD LPAREN values RPAREN SEMICOLON'''


def p_setclear(p):
    'setclear : ID DOT CLEAR LPAREN values RPAREN SEMICOLON'


def p_setcontains(p):
    'setcontains : ID DOT CONTAINS LPAREN values RPAREN SEMICOLON'


def p_setAddAll(p):
    'setAddAll : ID DOT ADDALL LPAREN ID RPAREN SEMICOLON'


def p_setlengh(p):
    'setlengh : ID DOT LENGTH SEMICOLON'


def p_setremove(p):
    'setremove : ID DOT REMOVE LPAREN values RPAREN SEMICOLON'


# foreach
def p_foreach(p):
    'foreach : ID DOT FOREACH  LPAREN instruccionesMas RPAREN SEMICOLON'


# Array
def p_array(p):
    '''array :  ID EQUAL  arrayInicio SEMICOLON
    | arrayFunc SEMICOLON
    '''


def p_arrayInicio(p):
    '''arrayInicio :  SQUAREBRACKETLEFT SQUAREBRACKETRIGHT
    | SQUAREBRACKETLEFT set SQUAREBRACKETRIGHT
    | ID DOT subArray
    '''


def p_arrayFunc(p):
    '''arrayFunc : ID DOT subArray'''


def p_listBuscar(p):
    'listBuscar : ID DOT LENGTH SEMICOLON'


def p_arrayChanges(p):
    'arrayChanges : ID SQUAREBRACKETLEFT values SQUAREBRACKETRIGHT EQUAL values SEMICOLON'


def p_subArray(p):
    '''subArray :  SUBLIST LPAREN values RPAREN SEMICOLON
    | subArray DOT subArray
    '''

# Fin de Contribucion Viviana Velasco
# Contribuccion de David Terreros => Map, For y Funcion Normal.


def p_asignacion(p):
    '''asignacion : DATATYPES ID EQUAL values SEMICOLON
    | VARTYPE ID EQUAL values SEMICOLON
    | DATATYPES ID operadoresAsignacion values SEMICOLON
    '''


def p_asignacionesMas(p):
    '''asignacionesMas : asignacion
    | asignacion asignacionesMas'''


def p_values(p):
    '''values : INT
    | FLOAT
    | BOOLEAN
    | STR
    '''


# Map David Terreros
def p_estructuraMap(p):
    '''estructuraMap : MAP ID EQUAL CURLYBRACKETLEFT itemsMaps CURLYBRACKETRIGHT SEMICOLON 
    | MAP LESS DATATYPES COMMA DATATYPES GREATER ID EQUAL CURLYBRACKETLEFT itemsMaps CURLYBRACKETRIGHT SEMICOLON 
    | VARTYPE ID EQUAL CURLYBRACKETLEFT itemsMaps CURLYBRACKETRIGHT SEMICOLON 
    | VARTYPE ID EQUAL NEW MAP LPAREN RPAREN SEMICOLON
    | VARTYPE ID EQUAL NEW MAP LESS DATATYPES COMMA DATATYPES GREATER LPAREN RPAREN SEMICOLON
    | metodoMapClear
    | metodoMapRemoveKey
    | metodoMapAddAll
    | metodoMapAdd
    '''


def p_itemsMaps(p):
    '''itemsMaps : values COLON values
    | values COLON values COMMA itemsMaps
    '''


# Estructura de Control David Terreros
def p_sentenciaFor(p):
    '''sentenciaFor : FOR LPAREN asignacion SEMICOLON comparacion SEMICOLON operadoresArimeticoId RPAREN CURLYBRACKETLEFT instruccionesMas CURLYBRACKETRIGHT'''


def p_comparacion(p):
    '''comparacion : ID comparador values 
    | ID comparador ID 
    | BOOLEAN
    | ID operadoresLogicos ID
    '''


def p_comparador(p):
    '''comparador : GREATER
    | LESS
    | GREATEREQ
    | LESSEQ
    | EQUALC
    | DIFFERENT
    '''


def p_operadoresLogicos(p):
    '''operadoresLogicos : AND
    | OR
    | NOT
    '''


def p_operadoresArimeticoId(p):
    '''operadoresArimeticoId : ID INCREMENT
    | ID DECREMENT
    | ID PLUSEQUAL values
    | ID MINUSEQUAL values
    | ID MULTIPLUS values
    | ID DIVIDEEQUAL values
    '''


def p_operadoresAsignacion(p):
    '''operadoresAsignacion : PLUSEQUAL 
    | MINUSEQUAL
    | MULTIPLUS
    | DIVIDEEQUAL
    '''


# INICIO Funciones David Terreros
def p_metodoMapClear(p):
    'metodoMapClear : ID DOT CLEAR LPAREN RPAREN SEMICOLON'


def p_metodoMapRemoveKey(p):
    'metodoMapRemoveKey : ID DOT CLEAR LPAREN values RPAREN SEMICOLON'


def p_metodoMapAddAll(p):
    'metodoMapAddAll : ID DOT CLEAR LPAREN CURLYBRACKETLEFT itemsMaps CURLYBRACKETRIGHT RPAREN SEMICOLON'


def p_metodoMapAdd(p):
    'metodoMapAdd : ID SQUAREBRACKETRIGHT values SQUAREBRACKETLEFT EQUAL values SEMICOLON'
# FIN Funciones David Terreros


def p_error(p):
    if p:
        print("Error de sintaxis en token", p.type)
    else:
        print("Syntax error at EOF")


# Testear Codigo
data = '''
import 'dart:math';

const int RUN = 32;
void insertionSort(List list, int left, int right) {
  for (int i = left + 1; i <= right; i++) {
    int temp = list[i];
    int j = i - 1;
    while (j >= left && list[j] > temp) {
      list[j + 1] = list[j];
      j--;
    }
    list[j + 1] = temp;
  }
}

void merge(List list, int left, int middle, int right) {
  int length1 = middle - left + 1, length2 = right - middle;
  List leftList = List.filled(length1, null),
      rightList = new List.filled(length2, null);

  for (int i = 0; i < length1; i++) {
    leftList[i] = list[left + i];
  }

  for (int i = 0; i < length2; i++) {
    rightList[i] = list[middle + 1 + i];
  }

  int i = 0, j = 0, k = 0;
  while (i < length1 && j < length2) {
    if (leftList[i] <= rightList[j]) {
      list[k] = leftList[i];
      i++;
    } else {
      list[k] = rightList[j];
      j++;
    }
    k++;
  }

  while (i < length1) {
    list[k] = leftList[i];
    i++;
    k++;
  }

  while (j < length2) {
    list[k] = rightList[j];
    k++;
    j++;
  }
}

void timSort(List list, int n) {
  for (int i = 0; i < n; i += RUN) {
    insertionSort(list, i, min((i + 31), n - 1));
  }

  for (int size = RUN; size < n; size = 2 * size) {
    for (int left = 0; left < n; left += 2 * size) {
      int middle = left + size - 1;
      int right = min((left + 2 * size - 1), (n - 1));
      merge(list, left, middle, right);
    }
  }
}

void main() {
  //Test 1
  List arr = [12, 213, 45, 9, 107];
  timSort(arr, arr.length);
  print(arr);

  //Test 2
  List arr2 = [];
  timSort(arr2, arr2.length);
  print(arr2);

  //Test 3
  List arr3 = [];
  timSort(arr3, arr3.length);
  print(arr3);
}
'''

# Correr
# for i, linea in data:
#     sintactico.parse(linea)

# Build the parser
sintactico = yacc.yacc()

while True:
    try:
        s = input('dart > ')
    except EOFError:
        break
    if not data:
        continue
    result = sintactico.parse(data)
    if result != None:
        print(result)
