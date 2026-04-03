from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFrame, QGridLayout
from math import sqrt, factorial
import sys

#At each entry of the user, the value is added at the end of the calculation string.
# If the user add a special character (= ; ┤ ; AC ; ⌫), the programm will run differently. 

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        
        self.showed_calcul = ""
        self.calcul = ""
        self.result = ""        
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle('PyQt6 Calculator')
        # self.setWindowIcon(QIcon('app-icon.png'))
        self.setFixedSize(400, 325)

        layout = QVBoxLayout()
        self.label_render_text = QLabel("\n")
        self.label_render_text.setFrameStyle(QFrame.Shape.Box | QFrame.Shadow.Raised)
        self.label_render_text.setFixedHeight(60)
        layout.addWidget(self.label_render_text)
        
        grid = QGridLayout()
        
        symbols = ["⌫","AC","=","+",
                   "7","8","9","-",
                   "4","5","6","*",
                   "1","2","3","/",
                   ".","0","Π","%",
                   "(",")","√","┤"]

        tooltips = {
            "⌫": "Delete the last character",
            "AC": "All Delete everything",
            "=": "Show the result",
            "┤": "Euclidian division of two numbers (quotient and rest)\nNote : Only one ┤ is allowed per calcul.",
            "√": "Square root\nNote : use it with parentheses : √(n)",
            "Π": "Factorial of a number\nNote : use it with parentheses : Π(n)",
            "*": "Multiplication of two numbers (a*b)\nPower of a number (a**b)",
            "+": "Addition of two numbers",
            "-": "Substraction of two numbers",
            "/": "Division of two numbers (a/b)\nQuotient of two numbers (a//b)",
            ".": "Dot for float numbers",
            "%": "Modulo of two numbers (rest of a division)"
        }
        
        # Buttons loop 
        cols = 4
        for index, symbol in enumerate(symbols):
            button = QPushButton(symbol)
            
            if symbol in tooltips:
                button.setToolTip(tooltips[symbol])
        
            button.clicked.connect(lambda _, s=symbol: self.ft_addToCalcul(s))
            row = index // cols
            col = index % cols
            grid.addWidget(button, row, col)   
        
        layout.addLayout(grid)
        self.setLayout(layout)
    
    def ft_euclidean_division(self, calcul):
        operator = calcul.index("┤")
        # Calculation of the two parts of the calcul string and adding them in a list
        nb_a = int(eval(calcul[:operator]))
        nb_b = int(eval(calcul[operator+1:]))

        # Adding the quotient and the rest
        nb_q = nb_a // nb_b
        nb_r = nb_a % nb_b

        formula = f"{nb_a} = {nb_b} * {nb_q} + {nb_r}"
        quotient = f"Quotient : {nb_q}"
        rest = f"Rest : {nb_r}"
        result = f"{calcul}"+"\n"+f"{formula}\n"+quotient+"     ;     "+ rest
        return result

    def ft_addToCalcul(self, value):
        if value == "=":
            self.calcul = self.showed_calcul
            try :
                if "√" in self.calcul : 
                    while ("√" in self.calcul) : 
                        self.calcul = self.calcul.replace("√", "sqrt")
                if "Π" in self.calcul : 
                    while ("Π" in self.calcul) : 
                        self.calcul = self.calcul.replace("Π", "factorial")
                if "┤" in self.calcul:
                    self.result = self.ft_euclidean_division(self.calcul)
                else :
                    self.result = f"{self.showed_calcul} \n = {str(eval(self.calcul))}" 
                    print(f"calcul  : {self.calcul} | showed_calcul : {self.showed_calcul} | result : {str(eval(self.calcul))}")
            except Exception as e :
                self.result = f"⚠︎ Error : {e}"
            self.label_render_text.setText(self.result)
            self.calcul = self.showed_calcul = ""

        # AC : Erase everyting 
        elif value == "AC":
            self.showed_calcul = ""
            self.label_render_text.setText(f" \n")
            print("AC")

        # ⌫ : Erase the last character
        elif value == "⌫":
            self.showed_calcul = self.showed_calcul[:-1]
            self.label_render_text.setText(self.showed_calcul +  "\n" )
            print(f"{self.showed_calcul}⌫")

        # If there's alerady a "┤" in the string, we don't allow it again
        elif (value == "┤" and ("┤" in self.showed_calcul)) : 
            pass
        
        # We add the pressed character at the end of the string
        else : 
            self.showed_calcul += str(value)
            self.label_render_text.setText(self.showed_calcul +  "\n" )
            print(f"{self.showed_calcul}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
