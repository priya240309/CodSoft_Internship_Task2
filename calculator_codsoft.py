import tkinter as tk
from tkinter import messagebox

class SimpleCalculator:
    def __init__(self, window):
        self.window = window
        self.window.title("Simple Calculator")
        self.window.geometry("350x300")
        self.window.configure(bg= "#f9f9f9")
        
        #input field
        self.label1 = tk.Label(window, text="First Numbers:", bg= "#f9f9f9", font=("Arial",12))
        self.label1.pack(pady=5)
        self.first_input = tk.Entry(window, font =("Arial",12))
        self.first_input.pack(pady=5)
        
        self.label2 = tk.Label(window,text="Second Number:", bg="#f9f9f9", font=("Arial",12))
        self.label2.pack(pady=5)
        self.second_input = tk.Entry(window, font =("Arial",12))
        self.second_input.pack(pady=5)
        
        self.label3 = tk.Label(window, text="Operation(+  -  *  /):", bg= "#f9f9f9", font=("Arial",12))
        self.label3.pack(pady=5)
        self.operator_input = tk.Entry(window, font=("Arial",12))
        self.operator_input.pack(pady=5)
        
        self.calculate_button = tk.Button(window, text = "calculate", command=self.perform_calculation, bg="#4CAF50", fg= "white", width=15)
        self.calculate_button.pack(pady=10)
        
        self.output_label = tk.Label(window, text="", bg="#f9f9f9", font=("Arial", 12, "bold"))
        self.output_label.pack(pady=10)
    
    def perform_calculation(self):
        try:
            number1 = float(self.first_input.get())
            number2 = float(self.second_input.get())
            operator = self.operator_input.get().strip()

            if operator == '+':
                result = number1 + number2
            elif operator == '-':
                result = number1 - number2
            elif operator == '*':
                result = number1 * number2
            elif operator == '/':
                if number2 == 0:
                    raise ZeroDivisionError
                result = number1 / number2
            else:
                self.output_label.config(text="Invalid operator.")
                return
            self.output_label.config(text=f"Result: {result}")

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")
        except ZeroDivisionError:
            messagebox.showerror("Math Error", "Cannot divide by zero.")

# Start the app
if __name__ == "__main__":
    main_window = tk.Tk()
    app = SimpleCalculator(main_window)
    main_window.mainloop()
            