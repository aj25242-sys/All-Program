from tkinter import *

def ATM():
    card_type = txt1.get()
    card_number = txt2.get()
    name = txt3.get()
    cvv = txt4.get()
    pin = txt5.get()


    if name == "Amit" and pin == "12345" and card_number == "12345678" and cvv == "123" and card_type =="Debit" or card_type == "Credit":
     label.config(text="Login Successful", fg="Green")
    else:
        label.config(text = "Invalid Credentials", fg = "red")

root = Tk(); 
root.title("Welcome to ATM")
root.geometry("800x800")  # Used to give height and width


label = Label(root, text = "Welcome to the ATM : ", font=("Helvetica", 16))
label.pack(pady = 10)

label1 = Label(root, text = "Enter your card type : ", font=("Helvetica", 16))
label1.pack(pady = 10)
txt1 = Entry(root, font= ("Helvetica", 16))
txt1.pack(pady = 10)

label2 = Label(root, text = "Enter your card Number : ", font=("Helvetica", 16))
label2.pack(pady = 10)
txt2 = Entry(root, font= ("Helvetica", 16))
txt2.pack(pady = 10)

label3 = Label(root, text = "Enter your Name : ", font=("Helvetica", 16))
label3.pack(pady = 10)
txt3 = Entry(root, font= ("Helvetica", 16))
txt3.pack(pady = 10)

label4 = Label(root, text = "Enter your cvv : ", font=("Helvetica", 16))
label4.pack(pady = 10)
txt4 = Entry(root, font= ("Helvetica", 16))
txt4.pack(pady = 10)

label5 = Label(root, text = "Enter your pin : ", font=("Helvetica", 16))
label5.pack(pady = 10)
txt5 = Entry(root, font= ("Helvetica", 16))
txt5.pack(pady = 10)

label = Label(root, text="", font=("Helvetica", 16))
label.pack(pady=10)
button1 = Button(root, text = "Login", font= ("Helvetica", 16), command=ATM)
button1.pack()


root.mainloop();