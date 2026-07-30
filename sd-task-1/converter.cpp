#include <iostream>
#include <iomanip>

int main() {
    double celsius;
    std::cout << "Enter temperature in Celsius: ";
    if (std::cin >> celsius) {
        double fahrenheit = (celsius * 9.0 / 5.0) + 32.0;
        double kelvin = celsius + 273.15;
        
        std::cout << std::fixed << std::setprecision(2);
        std::cout << "Fahrenheit: " << fahrenheit << " °F\n";
        std::cout << "Kelvin:     " << kelvin << " K\n";
    }
    return 0;
}
