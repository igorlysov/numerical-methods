#include <iostream>
#include <limits>

int main() {
    int k = 0;
    float num_a = 1;
    double num_b = 1;
    long double num_c = 1;

    std::cout << "------------------------------------" << std::endl;
    while (num_a != 0) {
        num_a /= 2;
        k++;
    }
    std::cout << "float machine zero = 2^(" << -k << ")" << std::endl;

    k = 0;
    num_a = 1;
    while (num_a < std::numeric_limits<float>::max()) {
        num_a *= 2;
        k++;
    }
    std::cout << "float machine infinity = 2^" << k << std::endl;

    k = 0;
    num_a = 1;
    while (1 + num_a > 1) {
        num_a /= 2;
        k++;
    }
    std::cout << "float machine epsilon = 2^(" << -k << ")" << std::endl;
    std::cout << "------------------------------------" << std::endl;
    while (num_b != 0) {
        num_b /= 2;
        k++;
    }
    std::cout << "double machine zero = 2^(" << -k << ")" << std::endl;

    k = 0;
    num_b = 1;
    while (num_b < std::numeric_limits<double>::max()) {
        num_b *= 2;
        k++;
    }
    std::cout << "double machine infinity = 2^" << k  << std::endl;

    k = 0;
    num_b = 1;
    while (1 + num_b > 1) {
        num_b /= 2;
        k++;
    }
    std::cout << "double machine epsilon = 2^(" << -k << ")" << std::endl;
    std::cout << "------------------------------------" << std::endl;
    while (num_c != 0) {
        num_c /= 2;
        k++;
    }
    std::cout << "long double machine zero = 2^(" << -k << ")" << std::endl;

    k = 0;
    num_c = 1;
    while (num_c < std::numeric_limits<long double>::max()) {
        num_c *= 2;
        k++;
    }
    std::cout << "long double machine infinity = 2^" << k << std::endl;

    k = 0;
    num_c = 1;
    while (1 + num_c > 1) {
        num_c /= 2;
        k++;
    }
    std::cout << "long double machine epsilon = 2^(" << -k << ")" << std::endl;



    return 0;
}
