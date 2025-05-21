import tkinter as tk
from tkinter import messagebox
from calculator import perform_operation
from timer import countdown_timer

def start_gui():
    window = tk.Tk()
    window.title("Countdown Timer & Calculator")

    tk.Label(window, text="Timer (sec):").grid(row=0, column=0)
    timer_entry = tk.Entry(window)
    timer_entry.grid(row=0, column=1)

    def start_timer():
        try:
            seconds = int(timer_entry.get())
            countdown_timer(seconds)
            messagebox.showinfo("Done", "Countdown finished!")
        except ValueError:
            messagebox.showerror("Error", "Enter valid number")

    tk.Button(window, text="Start Timer", command=start_timer).grid(row=0, column=2)

    tk.Label(window, text="Calc A:").grid(row=1, column=0)
    entry_a = tk.Entry(window)
    entry_a.grid(row=1, column=1)

    tk.Label(window, text="Op:").grid(row=2, column=0)
    entry_op = tk.Entry(window)
    entry_op.grid(row=2, column=1)

    tk.Label(window, text="Calc B:").grid(row=3, column=0)
    entry_b = tk.Entry(window)
    entry_b.grid(row=3, column=1)

    result_label = tk.Label(window, text="Result:")
    result_label.grid(row=4, column=0, columnspan=2)

    def calculate():
        a = entry_a.get()
        b = entry_b.get()
        op = entry_op.get()
        result = perform_operation(a, b, op)
        result_label.config(text=f"Result: {result}")

    tk.Button(window, text="Calculate", command=calculate).grid(row=3, column=2)

    window.mainloop()