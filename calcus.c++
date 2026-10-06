#include <iostream>
#include <string>

class Calculator {
public:
    Calculator() : display(""), current_num(""), operator_('\0') {}

    void append_to_display(char char) {
        if (char == '.' && display.find('.') == std::string::npos) {
            return;
        }
        else if (char == '=' || char == 'C') {
            calculate();
            return;
        }
        else if (char == '+' || char == '-' || char == '*' || char == '/') {
            if (operator_ != '\0') {
                calculate();
            }
            operator_ = char;
            current_num = "";
        } else {
            current_num += char;
            display += char;
        }
    }

    void calculate() {
        double num1, num2;
        if (operator_ == '+') {
            num1 = std::stod(current_num);
            num2 = std::stod(display);
            display = std::to_string(num1 + num2);
        }
        else if (operator_ == '-') {
            num1 = std::stod(current_num);
            num2 = std::stod(display);
            display = std::to_string(num1 - num2);
        }
        else if (operator_ == '*') {
            num1 = std::stod(current_num);
            num2 = std::stod(display);
            display = std::to_string(num1 * num2);
        }
        else if (operator_ == '/') {
            if (current_num == "0") {
                display = "Error";
            }
            else {
                num1 = std::stod(current_num);
                num2 = std::stod(display);
                display = std::to_string(num1 / num2);
            }
        }
    }

    std::string get_display() {
        return display;
    }

private:
    std::string display;
    std::string current_num;
    char operator_;
};
