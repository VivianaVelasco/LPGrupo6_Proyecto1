/// Approximate definite integral of f in [a, b] interval
double simpson(double Function(double) f, double a, double b, int n) {
  if (n <= 0) {
    throw ArgumentError("n have to be greater than 0");
  }

  double step = (b - a) / n;
  double sum = f(a) + f(b);

  for (int i = 1; i < n; i++) {
    if (i % 2 == 0) {
      sum += 2 * f(a + i * step);
    } else {
      sum += 4 * f(a + i * step);
    }
  }

  return (step / 3) * sum;
}

double f(double x) {
  return x * x + 2 * x + 7;
}

void main() {
  print(simpson(f, 0, 10, 10));
}
// Algoritmo tomado de: https://github.com/TheAlgorithms/Dart/blob/master/maths/simpson_rule.dart
/*
void main() {
  int num1 = 5;
  int num2 = 8;
  Set saludo = {'Hola', 'Mundo','Ciao', 'Mondo'};
  var mascotas = ['perro','gato','conejo','pajaro'];
  int count = 0;
  if(num1>num2){
    count++;
    saludo.add('Bonjour');
    if(count>=10){
      num2 -= 2;
    }else{
      num2 += 2;
    }
    
  }else if(num1<num2){
    num1++;
    mascotas[1] = 'cat';
    count += 3;
  }else{
    num1--;
    num2++;
    count += 4;
  }
  print(count);
  print(mascotas[2]);
  print(mascotas);
  
}
*/