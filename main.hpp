#include <iostream>
#include <time.h>

void InsertSort(int* ar, int size) {
    int i, j, digit;
    for (i = 1; i < size; i++) {
        digit = ar[i];
        j = i - 1;

        while (ar[j] < digit) {
            if (j < 0) {
                break;
            }
            *(ar + j + 1) = ar[j];
            j--;
        }
        *(ar + j + 1) = digit;
    }
}

void fillRandom(int* firstElementOfArray, int size) {
    srand(time(nullptr));
    for (int i = 0; i < size; i++) {
        *(firstElementOfArray + i) = rand() % 100;
    }
}
