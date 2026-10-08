
import tkinter as tk

def sum():
    print("Function has been called successfully")

root = tk.Tk(); 
root.title("Tkinter example")
root.geometry("400x200")  # Used to give height and width

label1 = tk.Label(root, text = "Enter first number : ")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

button1 = tk.Button(root, text = "Addition", command=sum)
button1.pack()


root.mainloop();
