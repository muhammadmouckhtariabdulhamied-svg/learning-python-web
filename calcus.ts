class Calculator {
    private display: string;
    private currentNum: string;
    private operator: string;

    constructor() {
        this.display = "";
        this.currentNum = "";
        this.operator = '';
    }

    appendToDisplay(char: string): void {
        if (char === '.' && !this.display.includes('.')) {
            return;
        }
        else if (char === '=' || char === 'C') {
            this.calculate();
            return;
        }
        else if (char === '+' || char === '-' || char === '*' || char === '/') {
            if (this.operator !== '') {
                this.calculate();
            }
            this.operator = char;
            this.currentNum = '';
        } else {
            this.currentNum += char;
            this.display += char;
        }
    }

    calculate(): void {
        if (this.operator === '+') {
            this.display = ( parseFloat(this.currentNum) + parseFloat(this.display) ).toString();
        }
        else if (this.operator === '-') {
            this.display = ( parseFloat(this.currentNum) - parseFloat(this.display) ).toString();
        }
        else if (this.operator === '*') {
            this.display = ( parseFloat(this.currentNum) * parseFloat(this.display) ).toString();
        }
        else if (this.operator === '/') {
            if (this.currentNum === "0") {
                this.display = "Error";
            }
            else {
                this.display = ( parseFloat(this.currentNum) / parseFloat(this.display) ).toString();
            }
        }
    }

    getDisplay(): string {
        return this.display;
    }
}
