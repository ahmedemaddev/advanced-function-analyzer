from tkinter import *
from sympy import *
import numpy as np
import matplotlib.pyplot as plt

# variable
x = symbols('x')


# رسم الجراف
def draw_graph(func, title_name):

    x_vals = np.linspace(-10, 10, 400)

    y_vals = []

    for val in x_vals:

        y = func.subs(x, val)

        y_vals.append(float(y))

    plt.plot(x_vals, y_vals)

    plt.title(title_name)

    plt.xlabel("x")
    plt.ylabel("y")

    plt.grid(True)

    plt.show()


# رسم الدالة الأصلية
def plot_function():

    func_str = entry.get()

    func = sympify(func_str)

    draw_graph(func, "Original Function")


# First Derivative
def first_derivative():

    func_str = entry.get()

    func = sympify(func_str)

    derivative = diff(func, x)

    result_label.config(
        text=f"First Derivative:\n{derivative}"
    )

    draw_graph(derivative, "First Derivative")


# Second Derivative
def second_derivative():

    func_str = entry.get()

    func = sympify(func_str)

    second = diff(func, x, 2)

    result_label.config(
        text=f"Second Derivative:\n{second}"
    )

    draw_graph(second, "Second Derivative")


# Integration
def integration():

    func_str = entry.get()

    func = sympify(func_str)

    integral = integrate(func, x)

    result_label.config(
        text=f"Integration:\n{integral}"
    )


# Max / Min
def max_min():

    func_str = entry.get()

    func = sympify(func_str)

    first = diff(func, x)

    critical_points = solve(first, x)

    result_label.config(
        text=f"Critical Points:\n{critical_points}"
    )


# Vertical Shift
def vertical_shift():

    func_str = entry.get()

    func = sympify(func_str)

    shifted = func + 2

    result_label.config(
        text="Vertical Translation Applied: f(x) + 2"
    )

    draw_graph(shifted, "Vertical Translation")


# Horizontal Shift
def horizontal_shift():

    func_str = entry.get()

    func = sympify(func_str)

    shifted = func.subs(x, x - 2)

    result_label.config(
        text="Horizontal Translation Applied: f(x - 2)"
    )

    draw_graph(shifted, "Horizontal Translation")


# Stretch
def stretch():

    func_str = entry.get()

    func = sympify(func_str)

    stretched = 2 * func

    result_label.config(
        text="Stretch Transformation Applied: 2f(x)"
    )

    draw_graph(stretched, "Stretch Transformation")


# ================= WINDOW =================

root = Tk()

root.title("Advanced Calculus Function Analyzer")

root.geometry("750x750")

root.configure(bg="black")


# ================= TITLE =================

title_label = Label(
    root,
    text="Advanced Function Analyzer Tool",
    font=("Arial", 22, "bold"),
    bg="black",
    fg="gold"
)

title_label.pack(pady=20)


# ================= INPUT LABEL =================

label = Label(
    root,
    text="Enter a Mathematical Function:",
    font=("Arial", 14),
    bg="black",
    fg="gold"
)

label.pack(pady=10)


# ================= ENTRY =================

entry = Entry(
    root,
    width=35,
    font=("Arial", 14),
    bg="#222222",
    fg="gold",
    insertbackground="gold"
)

entry.pack(pady=10)


# ================= BUTTON STYLE =================

button_style = {
    "font": ("Arial", 12, "bold"),
    "bg": "gold",
    "fg": "black",
    "activebackground": "#FFD700",
    "activeforeground": "black",
    "width": 32
}


# ================= BUTTONS =================

Button(
    root,
    text="Display Function Graph",
    command=plot_function,
    **button_style
).pack(pady=5)


Button(
    root,
    text="Compute First Derivative",
    command=first_derivative,
    **button_style
).pack(pady=5)


Button(
    root,
    text="Compute Second Derivative",
    command=second_derivative,
    **button_style
).pack(pady=5)


Button(
    root,
    text="Compute Indefinite Integral",
    command=integration,
    **button_style
).pack(pady=5)


Button(
    root,
    text="Detect Critical Points",
    command=max_min,
    **button_style
).pack(pady=5)


Button(
    root,
    text="Apply Vertical Translation",
    command=vertical_shift,
    **button_style
).pack(pady=5)


Button(
    root,
    text="Apply Horizontal Translation",
    command=horizontal_shift,
    **button_style
).pack(pady=5)


Button(
    root,
    text="Apply Stretch / Compression",
    command=stretch,
    **button_style
).pack(pady=5)


# ================= RESULT LABEL =================

result_label = Label(
    root,
    text="Analysis Results Will Appear Here",
    font=("Arial", 14, "bold"),
    wraplength=650,
    bg="black",
    fg="gold"
)

result_label.pack(pady=25)


# ================= RUN =================

root.mainloop()