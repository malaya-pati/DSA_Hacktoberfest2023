#include <iostream>

void printFibonacci(int n) {
    int first = 0, second = 1;

    std::cout << "Fibonacci Series up to " << n << " terms: ";
    std::cout << first << ", " << second << ", ";

    for (int i = 2; i < n; ++i) {
        int next = first + second;
        std::cout << next << ", ";
        first = second;
        second = next;
    }

    std::cout << std::endl;
}

int main() {
    int terms;

    std::cout << "Enter the number of terms for Fibonacci series: ";
    std::cin >> terms;

    if (terms < 1) {
        std::cout << "Number of terms should be at least 1." << std::endl;
        return 1;
    }

    printFibonacci(terms);

    return 0;
}
