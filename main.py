import ply.lex as lex

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
  'DATATYPES',
  'PLUS', 
  'MINUS', 
  'TIMES', 
  'DIVIDE', 
  'INT', 
  'FLOAT', 
  'LPAREN', 
  'RPAREN', 
  'ID',
  'EQUAL', 
  'EQUALC', 
  'COMMA', 
  'DIFFERENT', 
  'STR', 
  'GREATER', 
  'LESS', 
  'SEMICOLON', 
  'AND', 
  'OR', 
  'NOT', 
  'LIST', 
  'MAP', 
  'INCREMENT', 
  'DECREMENT',
  'PLUSEQUAL',
  'MINUSEQUAL',
  'MULTIPLUS',
  'DIVIDEEQUAL',
  'MOD',
  'SQUAREBRACKETLEFT',
  'SQUAREBRACKETRIGHT',
  'CURLYBRACKETLEFT',
  'CURLYBRACKETRIGHT',
  'DOLLAR',
  'DOT',
  'QUESTIONMARK',
  'ARROW',
  'BOOLEAN',
  'MAPTYPE',
  'UNDERSCORE'
) + tuple(reserved.values())

#Exp Regulares para tokens de símbolos
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
"""Fin de Contribucion Viviana Velasco"""

# Contribuccion David Terreros
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_FLOAT = r'-?\d*\.\d+'
t_INT = r'-?\d+'
t_EQUAL = r'='
t_EQUALC = r'=='
t_COMMA = r','
t_DIFFERENT = r'!='
t_STR = r'("[^"]*"|\'[^\']*\')'
t_GREATER = r'>'
t_LESS = r'<'
t_SEMICOLON = r';'
t_AND = r'\&'
t_OR = r'\|'
t_NOT = r'\!'
t_LIST = r'\[\]'
t_MAP = r'\{\}'
t_INCREMENT = r'\+\+'
t_DECREMENT = r'--'
t_MOD = r'%'
t_PLUSEQUAL = r'\+='
t_MINUSEQUAL = r'-='
t_MULTIPLUS = r'\*='
t_DIVIDEEQUAL = r'\/='
t_CURLYBRACKETLEFT = r'\{'
t_CURLYBRACKETRIGHT = r'\}'
t_SQUAREBRACKETRIGHT = r'\]'
t_SQUAREBRACKETLEFT = r'\['
t_DOLLAR = r'\$'
t_DOT = r'\.'
t_QUESTIONMARK = r'\?'
t_ARROW = r'=>'
t_UNDERSCORE = r"_"

def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_DATATYPES(t):
  r"int|double|String|float|bool|num|var|dynamic"
  return t

def t_ID(t):
  r"[a-zA-Z][a-zA-Z0-9_]*"
  t.type = reserved.get(t.value.lower(), 'ID')
  return t

def t_MAPTYPE(t):
   r'<>\{\}'
   pass

t_ignore = ' \t'

def t_COMMENT_SIMPLE(t):
    r'\/\/.*'
    pass

def t_COMMENT_DOUBLE(t):
    r'\/\*.*\*\/'
    pass

def t_error(t):
  print("Componente léxico no reconocido '%s'" % t.value[0])
  t.lexer.skip(1)

def t_BOOLEAN(t):
  r"(True|False)"
  return t

# FIN de Contribuccion David Terreros.
lexer = lex.lex()

#Testeando
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

// Algoritmo tomado de: https://github.com/TheAlgorithms/Dart/blob/master/sort/tim_Sort.dart
       '''

lexer.input(data)

while True:
  tok = lexer.token()
  if not tok:
    break 
  print(tok)