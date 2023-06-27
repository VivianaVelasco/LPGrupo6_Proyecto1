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
    | importsDart
    | listMethods
    | sentenciaWhile
    | palabraBreak
    | funcionPrint
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
    'foreach : ID DOT FOREACH LPAREN instruccionesMas RPAREN SEMICOLON'


# Array
def p_array(p):
    '''array : ID EQUAL arrayInicio SEMICOLON
    | arrayFunc SEMICOLON
    | DATATYPES ID EQUAL SQUAREBRACKETLEFT arrayValues SQUAREBRACKETRIGHT SEMICOLON
    | LIST ID EQUAL SQUAREBRACKETLEFT arrayValues SQUAREBRACKETRIGHT SEMICOLON
    '''


def p_arrayInicio(p):
    '''arrayInicio : SQUAREBRACKETLEFT SQUAREBRACKETRIGHT
    | SQUAREBRACKETLEFT set SQUAREBRACKETRIGHT
    | ID DOT subArray
    '''


def p_arrayValues(p):
    '''arrayValues : values
    | values COMMA arrayValues'''


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


def p_sentenciaWhile(p):
    '''sentenciaWhile : WHILE LPAREN comparacion RPAREN CURLYBRACKETLEFT instruccionesMas CURLYBRACKETRIGHT'''


def p_funcionPrint(p):
    '''funcionPrint : PRINT LPAREN printValues RPAREN SEMICOLON'''


def p_printValues(p):
    '''printValues : ID
    | values'''


def p_palabraBreak(p):
    '''palabraBreak : BREAK SEMICOLON'''


def p_comparacion(p):
    '''comparacion : ID comparador values 
    | ID comparador ID 
    | BOOLEAN
    | ID operadoresLogicos ID
    | BOOLEAN operadoresLogicos ID
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


def p_importsDart(p):
    'importsDart : IMPORT STR SEMICOLON'


def p_error(p):
    if p:
        print("Error de sintaxis en token", p.type)
    else:
        print("Syntax error at EOF")


def p_listMethods(p):
    '''listMethods : metodoListFilled'''


def p_metodoListFilled(p):
    '''metodoListFilled : LIST DOT FILLED LPAREN arrayValues RPAREN SEMICOLON'''


# Testear Codigo
data = '''
void main() {
    List myArr = [1,2,3,4,5,6];
    print(myArr);
    myArr.clear();
}
'''


# Build the parser
sintactico = yacc.yacc()

# Correr
sintactico.parse(data)    

# while True:
#     try:
#         s = input('dart > ')
#     except EOFError:
#         break
#     if not data:
#         continue
#     result = sintactico.parse(data)
#     if result != None:
#         print(result)
