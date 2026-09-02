"""A simple GUI calculator built with tkinter."""

import tkinter as tk


class CalculatorGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.resizable(False, False)
        self.expression = ""

        self.display_var = tk.StringVar(value="0")
        display = tk.Entry(
            self,
            textvariable=self.display_var,
            font=("Segoe UI", 24),
            justify="right",
            bd=8,
            relief=tk.FLAT,
            state="readonly",
            readonlybackground="white",
        )
        display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=8, pady=8)

        buttons = [
            ("C", 1, 0), ("(", 1, 1), (")", 1, 2), ("/", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
            ("0", 5, 0), (".", 5, 1), ("⌫", 5, 2), ("=", 5, 3),
        ]

        for (text, row, col) in buttons:
            btn = tk.Button(
                self,
                text=text,
                font=("Segoe UI", 16),
                width=4,
                height=2,
                command=lambda t=text: self.on_button(t),
            )
            btn.grid(row=row, column=col, padx=2, pady=2)

        self.bind("<Return>", lambda e: self.on_button("="))
        self.bind("<BackSpace>", lambda e: self.on_button("⌫"))

    def on_button(self, char):
        if char == "C":
            self.expression = ""
        elif char == "⌫":
            self.expression = self.expression[:-1]
        elif char == "=":
            self.evaluate()
            return
        else:
            self.expression += char
        self.display_var.set(self.expression if self.expression else "0")

    def evaluate(self):
        # Only allow characters valid in a basic arithmetic expression.
        allowed = set("0123456789.+-*/() ")
        if not self.expression or any(c not in allowed for c in self.expression):
            self.display_var.set("Error")
            self.expression = ""
            return
        try:
            result = eval(self.expression, {"__builtins__": {}}, {})
        except ZeroDivisionError:
            self.display_var.set("Error: div by 0")
            self.expression = ""
            return
        except Exception:
            self.display_var.set("Error")
            self.expression = ""
            return
        self.expression = str(result)
        self.display_var.set(self.expression)


if __name__ == "__main__":
    app = CalculatorGUI()
    app.mainloop()
