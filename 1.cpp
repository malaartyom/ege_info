#include <stdio.h>
#include <cmath>
#include <iostream>
using namespace std;

long long int f(long long int x) {
    if (x < 9) {
        return x;
    } 
    if (x >= 9) {
        return f(x / 9) + f(x % 9);
    }
}

int main() {
    long long int c = 0;
    cout << 4 * pow(6, 20) << endl;
    cout << 5 * pow(6, 20) << endl;
    cout << f(4 * pow(6, 20)) << endl;
    // cout << ((i - 5 * pow(6, 20)) / (5 * pow(6, 20) - 4 * pow(6, 20))) * 100 << "%" << endl;
    for (long long int i = 80008888888888888; i <= 88888888888888810; i++) {
        if (i % 10000000 == 0) {
            cout << ((i - 80008888888888888) / (88888888888888810 - 80008888888888888)) * 100 << "%" << endl;
        }

        if (f(i) == 121) {
            c++;
        }
    }
    cout << c << endl;
}