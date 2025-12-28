import tkinter as tk
import random

def show_popup():
    popup = tk.Toplevel(root)
    popup.title("Popup")
    tk.Label(popup, text="Thanks for Accepting!", font=("Arial", 12)).pack(padx=20, pady=20)

def move_no_button(event):
    # Get window and button dimensions dynamically
    window_width = root.winfo_width()
    window_height = root.winfo_height()

    btn_width = no_button.winfo_width()
    btn_height = no_button.winfo_height()

    # Calculate safe bounds
    max_x = window_width - btn_width
    max_y = window_height - btn_height

    x = random.randint(0, max_x)
    y = random.randint(50, max_y)  # leave space for the question label

    no_button.place(x=x, y=y)

    # Randomly change color
    COLORS = ["#FF6F61", "#F5E001", "#88B04B", "#F7CAC9", "#0D5DF1", "#955251", 
              "#B565A7", "#009B77", "#DD4124", "#45B8AC", "#EFC050", "#5B5EA6", "#9B2335", "#DFCFBE"]
    no_button.config(bg=random.choice(COLORS))

root = tk.Tk()
root.title("Abdul Hanan, Python Developer")
root.geometry("400x400")

question_label = tk.Label(root, text="Do you Like me?", font=("Arial", 14))
question_label.pack(pady=20)

yes_button = tk.Button(root, text="Yes", font=("Arial", 12), bg="#4CAF50", fg="white", command=show_popup)
yes_button.place(x=150, y=80)

no_button = tk.Button(root, text="No", font=("Arial", 12), bg="#F44336", fg="white")
no_button.place(x=150, y=130)
no_button.bind("<Enter>", move_no_button)

root.mainloop()