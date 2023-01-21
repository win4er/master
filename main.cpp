#include <iostream>
#include <time.h>
#include "main.hpp"

int main() {
    int size = 7;
    int arr[size];
    fillRandom(&arr[0], size);
        for (int i = 0; i < size; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
    InsertSort(&arr[0], size);
    for (int i = 0; i < size; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
    return 0;
}
