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
