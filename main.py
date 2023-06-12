import ply.lex as lex

#Crear los tokens para la siguiente sintaxis

#SELECT * FROM Tabla
#select campo1, campo2 from Tabla1 where campo==1
#SELECT campo1 as cedula from Datos where provincia<>"7"
#print(consulta)
#DELETE FROM datos WHERE id>1000
#print("SELECT * FROM Tabla")

#Diccionario de palabras reservadas

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
  'PLUS', 'MINUS', 'TIMES', 'DIVIDE'
) + tuple(reserved.values())

#Exp Regulares para tokens de símbolos
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
"""Contribucion Viviana Velasco"""

#Contruir analizador
lexer = lex.lex()

#Testeando
data = '''
      List<int> moveZeroes(List<int> nums) {
  int lastNonZeroFoundAt = 0;

  for (int i = 0; i < nums.length; ++i) {
    if (nums[i] != 0) {
      nums[lastNonZeroFoundAt] = nums[i];
      lastNonZeroFoundAt += 1;
    }
  }

  for (int i = lastNonZeroFoundAt; i < nums.length; ++i) {
    nums[i] = 0;
  }
  return nums;
}
       '''

#Datos de entrada
lexer.input(data)

# Tokenizador
while True:
  tok = lexer.token()
  if not tok:
    break  #Rompe
  print(tok)