import tkinter as tk

root = tk.Tk()
root.title("Example 1")
root.geometry("300x300")

button = tk.Button(root, text="Click me", command=lambda: print("You clicked me!"))
button.pack()

root.mainloop()
