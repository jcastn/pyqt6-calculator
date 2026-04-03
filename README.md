# PyQt6 Calculator v2

A clean, functional, and object-oriented calculator built with **Python** and **PyQt6**. This project features standard arithmetic, square roots, factorials, and a dedicated mode for **Euclidean Division**.

## I. Key Features

* **OOP Architecture:** Fully written using Object-Oriented Programming (Classes/Self) for modularity and autonomy.
* **Euclidean Division Mode:** A specialized function (`┤`) that calculates the quotient and remainder, displaying the full mathematical formula ($a = b \times q + r$).
* **Advanced Math:** Support for Square Roots (`√`) and Factorials (`Π`) integrated with the `math` module. (More will come in a future update)
* **Interactive UI:** * **Tooltips:** Informative hover messages on buttons to guide the user.
    * **Responsive Grid:** Organized layout using `QGridLayout`.
    * **Error Handling:** Robust `try/except` blocks to prevent crashes on syntax or zero-division errors.

---

## II. Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/jcastn/pyqt6-calculator.git
   cd pyqt6-calculator
   ```

2. **Install dependencies:**
   Ensure you have Python 3.x installed, then install PyQt6:
   ```bash
   pip install PyQt6
   ```

3. **Run the application:**
   ```bash
   python __main__.py
   ```

---

## III. Usage & Controls

| Button | Description |
| :--- | :--- |
| `⌫` | "Delete the last character" |
| `AC` | "All Clear : Delete everything" |
| `┤` | "Euclidean division of two numbers (quotient and rest)" |
| `√` | "Square root\nNote : use it with parentheses : √(n)" |
| `Π` | "Factorial of a number\nNote : use it with parentheses : Π(n)" |
| `*` | "Multiplication of two numbers (a*b) and Power of a number (a\*\*b)" |
| `+` | "Addition of two numbers" |
| `-` | "Substraction of two numbers" |
| `/` | "Division of two numbers (a/b) and Quotient of two numbers (a//b)" |
| `%` | "Modulo of two numbers (rest of a division)" |

---

## IV. Contributing

Don't hesitate to contribute the project, any additions or reviews you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
