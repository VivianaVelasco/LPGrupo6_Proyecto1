from lexico import tokens
import ply.yacc as yacc


def p_instruccionesMas(p):
    '''instruccionesMas : instruccion 
    | instruccion instruccionesMas
    '''


def p_instruccion(p):
    '''instruccion : funcion
    | sentenciaFor
    | funcionPrint
    | estructuraMap
    | array
    | arrayChanges
    | declarset
    | sentenciaIfElse
    | foreach
    | listBuscar
    | importsDart
    | listMethods
    | sentenciaWhile
    | palabraBreak
    | asignacionesMas
    '''

# Inicio Contribucion Viviana Velasco
# Funcion


def p_funcion(p):
    '''funcion : STATIC DATATYPES ID LPAREN parametrosF RPAREN CURLYBRACKETLEFT instruccionesMas sentenciaReturn CURLYBRACKETRIGHT
    | DATATYPES ID LPAREN parametrosF RPAREN CURLYBRACKETLEFT instruccionesMas sentenciaReturn CURLYBRACKETRIGHT
    | VOID ID LPAREN parametrosF RPAREN CURLYBRACKETLEFT instruccionesMas CURLYBRACKETRIGHT
    | VOID ID LPAREN RPAREN CURLYBRACKETLEFT instruccionesMas CURLYBRACKETRIGHT
    | VOID ID LPAREN RPAREN CURLYBRACKETLEFT CURLYBRACKETRIGHT
    '''


def p_parametrosF(p):
    '''parametrosF : parametro
    | parametro COMMA parametrosF
    '''


def p_parametro(p):
    'parametro : DATATYPES ID'


def p_sentenciaReturn(p):
    '''sentenciaReturn : RETURN LPAREN retornarValues RPAREN SEMICOLON
    | RETURN retornarValues SEMICOLON'''


def p_retornarValues(p):
    '''retornarValues : values
    | NULL
    '''


def p_sentenciaIf(p):
    'sentenciaIf : IF LPAREN comparacion RPAREN CURLYBRACKETLEFT instruccionesMas CURLYBRACKETRIGHT'


def p_sentenciaElse(p):
    '''sentenciaElse : ELSE CURLYBRACKETLEFT instruccionesMas CURLYBRACKETRIGHT
    | ELSE sentenciaIf sentenciaElse
    '''


def p_sentenciaIfElse(p):
    '''sentenciaIfElse : sentenciaIf
    | sentenciaIf sentenciaElse
    '''


# Sets
def p_set(p):
    '''set : values
    | values COMMA set
    '''


def p_declarset(p):
    '''declarset : SET ID EQUAL NEW SET LPAREN RPAREN SEMICOLON
    | SET ID EQUAL CURLYBRACKETLEFT set CURLYBRACKETRIGHT SEMICOLON
    | VARTYPE ID EQUAL LESS DATATYPES GREATER CURLYBRACKETLEFT set CURLYBRACKETRIGHT SEMICOLON
    | setadd
    | setclear
    | setcontains
    | setAddAll
    | setlengh
    | setremove
    '''


def p_condicionesPlus(p):
    '''condicionesPlus : comparacion
    | comparacion operadoresLogicos condicionesPlus'''

# Metodos de Sets


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
    | LIST ID EQUAL LISTEMPTY SEMICOLON
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
    'listBuscar : ID DOT WHERE LPAREN instruccionesMas RPAREN SEMICOLON'


def p_arrayChanges(p):
    'arrayChanges : ID SQUAREBRACKETLEFT values SQUAREBRACKETRIGHT EQUAL values SEMICOLON'


def p_subArray(p):
    '''subArray : SUBLIST LPAREN values RPAREN SEMICOLON
    | subArray DOT subArray
    '''
# Fin de Contribucion Viviana Velasco


# Contribuccion de David Terreros => Map, For y Funcion Normal.
def p_asignacion(p):
    '''asignacion : DATATYPES ID EQUAL values SEMICOLON
    | VARTYPE ID EQUAL values SEMICOLON
    | DATATYPES ID operadoresAsignacion values SEMICOLON
    | DATATYPES ID EQUAL condicionesPlus SEMICOLON
    | ID EQUAL condicionesPlus SEMICOLON
    | ID EQUAL values SEMICOLON
    | operadoresArimeticoId
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
    | values
    | ID operadoresLogicos ID
    | BOOLEAN operadoresLogicos BOOLEAN
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
    '''operadoresArimeticoId : ID INCREMENT SEMICOLON
    | ID DECREMENT SEMICOLON
    | ID PLUSEQUAL values SEMICOLON
    | ID MINUSEQUAL values SEMICOLON
    | ID MULTIPLUS values SEMICOLON
    | ID DIVIDEEQUAL values SEMICOLON
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
    'metodoMapRemoveKey : ID DOT CLEAR LPAREN arrayValues RPAREN SEMICOLON'


def p_metodoMapAddAll(p):
    'metodoMapAddAll : ID DOT CLEAR LPAREN CURLYBRACKETLEFT itemsMaps CURLYBRACKETRIGHT RPAREN SEMICOLON'


def p_metodoMapAdd(p):
    'metodoMapAdd : ID SQUAREBRACKETRIGHT values SQUAREBRACKETLEFT EQUAL values SEMICOLON'
# FIN Funciones David Terreros


def p_importsDart(p):
    'importsDart : IMPORT STR SEMICOLON'


def p_listMethods(p):
    '''listMethods : metodoListFilled'''


def p_metodoListFilled(p):
    '''metodoListFilled : LIST DOT FILLED LPAREN arrayValues RPAREN SEMICOLON'''


def p_error(p):
    if p:
        print("Error de sintaxis en token", p.type)
        # stack_state_str = ' '.join(
        #     [symbol.type for symbol in sintactico.symstack][1:])

        # print('Syntax error in input! Parser State:{} {} . {}'
        #       .format(sintactico.state,
        #               stack_state_str,
        #               p))
    else:
        print("Syntax error at EOF")


# Testear Codigo
data = '''int x = 2;
x++;
x--;
String sayHello(String name){ return "${name}"; }
Set conjunto = new Set();
var name = 'Voyager I';
final year = 1977;
String palabra = 'BNHA';
bool res = 4 > 5;
bool res = 4 >= 5;
bool res = 4 != 5;
bool res = 4 < 5;
bool res = a >= b && 5 == 6 || a <= 3;
a += 4;
a -= 4;
a *= 4;
a /= 4;
final estudiante = {'nombre':'Tom','edad':23};
Map<string,int> estudiante = {'nombre':'1', 'edad':'23', 'año':'33'};
estudiante.clear('nombre');
estudiante.add({'nombre':'Anthony', 'Nota': 1});
estudiante["Peso"] = '23.4kg';
for(int i = 0; i < 3; i++){ print("$i"); }
var animes = new Map();
var animes = new Map <String,int>();
colors.clear();
final lista = [];
var lista = [];
lista = [3,-5,7,5,9];
var lista = ['aaa','eee','iii','ooo','uuu'];
for(int x = 4; x > 3; x++){ for(int y = y; x > 0; x--){x += 2; } }
int contador = 0;
while(cond == true){if (true) {cond = false; contador++;} else{contador--;} break;}
double twoSum(double x, double y) { final suma = x + y; return suma; }
double twoSum() { var suma = x + y; return suma; }
static int twoSum(double x, double y) { var suma = x + y; return suma; }'''


# Build the parser
sintactico = yacc.yacc()

# sintactico.parse(data)


def analizador_sintactico(data):
    result = sintactico.parse(data)
    if result != None:
        return result
    return ""
# Correr

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
