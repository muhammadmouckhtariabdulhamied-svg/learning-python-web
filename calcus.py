class Calculator:
    def __init__(self):
        self.display = ''
        self.current_num = ''
        self.operator = None

    def append_to_display(self, char):
        if char == '.' and '.' in self.display:
            return
        elif char == '=':
            self.calculate()
            return
        elif char == 'C':
            self.display = ''
            self.current_num = ''
            self.operator = None
            return
        elif char in '+-*/':
            if self.operator:
                self.calculate()
            self.operator = char
            self.current_num = ''
        else:
            self.current_num += char
            self.display += char

    def calculate(self):
        if self.operator == '+':
            self.display = str(float(self.current_num) + float(self.display))
        elif self.operator == '-':
            self.display = str(float(self.current_num) - float(self.display))
        elif self.operator == '*':
            self.display = str(float(self.current_num) * float(self.display))
        elif self.operator == '/':
            if float(self.current_num) == 0:
                self.display = 'Error'
            else:
                self.display = str(float(self.current_num) / float(self.display))

    def get_display(self):
        return self.display
