import tkinter
from tkinter import *

root = Tk()
root.title("Sahil ")
root.geometry("570x500")

root.resizable(False, False)
root.configure(bg="blue")
result = Label(root, width=35, height=2, text="", font=("Verdana", 20), bg= "red")
result.pack()
equation = ""
def show(value):
    global equation 
    equation = equation+value
    result.config(text = equation)
def clear():
    global equation 
    equation = ""
    result.config(text = equation)
def equal():
    global equation
    res = ""
    if equation != "":
        try:
            res = eval(equation)
        except:
            res= "error"
            equation = ""
    result.config(text = res)
            
        
Button(root, text= "/", width= 4, height= 1, font= ("Verdana", 30, "bold"), bd= 2, fg= "white", bg= "red", command = lambda: show("/")).place(x=10, y=75)
Button(root, text= "-", width= 4, height= 1, font= ("Verdana", 30, "bold"), bd= 2, fg= "white", bg= "red", command = lambda: show("-")).place(x=150, y=75)
Button(root, text= "+", width= 4, height= 1, font= ("Verdana", 30, "bold"), bd= 2, fg= "white", bg= "red", command = lambda: show("+")).place(x=290, y=75)
Button(root, text= "x", width= 4, height= 1, font= ("Verdana", 30, "bold"), bd= 2, fg= "white", bg= "red", command = lambda: show("*")).place(x=430, y=75)

Button(root, text= "1", width= 4, height= 1, font= ("Verdana", 30, "bold"), bd= 2, bg= "black", fg= "white", command = lambda: show("1")).place(x=10, y=200)
Button(root, text= "2", width= 4, height= 1, font= ("Verdana", 30, "bold"), bd= 2, bg= "black", fg= "white", command = lambda: show("2")).place(x=150, y=200)
Button(root, text= "3", width= 4, height= 1, font= ("Verdana", 30, "bold"), bd= 2, bg= "black", fg= "white", command = lambda: show("3")).place(x=290, y=200)
Button(root, text= "4", width= 4, height= 1, font= ("Verdana", 30, "bold"), bd= 2, bg= "black", fg= "white", command = lambda: show("4")).place(x=430, y=200)

Button(root, text= "5", width= 4, height= 1, font= ("Verdana", 30, "bold"), bd= 2, bg= "black", fg= "white", command = lambda: show("5")).place(x=10, y=300)
Button(root, text= "6", width= 4, height= 1, font= ("Verdana", 30, "bold"), bd= 2, bg= "black", fg= "white", command = lambda: show("6")).place(x=150, y=300)
Button(root, text= "7", width= 4, height= 1, font= ("Verdana", 30, "bold"), bd= 2, bg= "black", fg= "white", command = lambda: show("7")).place(x=290, y=300)
Button(root, text= "8", width= 4, height= 1, font= ("Verdana", 30, "bold"), bd= 2, bg= "black", fg= "white", command = lambda: show("8")).place(x=430, y=300)

Button(root, text= "9", width= 4, height= 1, font= ("Verdana", 30, "bold"), bd= 2, bg= "black", fg= "white", command = lambda: show("9")).place(x=10, y=400)
Button(root, text= "0", width= 4, height= 1, font= ("Verdana", 30, "bold"), bd= 2, bg= "black", fg= "white", command = lambda: show("0")).place(x=150, y=400)
Button(root, text= "=", width= 4, height= 1, font= ("Verdana", 30, "bold"), bd= 2, bg= "black", fg= "white", command = lambda: equal()).place(x=290, y=400)
Button(root, text= "clear   ", width= 4, height= 1, font= ("Verdana", 30, "bold"), bd= 2, bg= "black", fg= "white", command = lambda: clear()).place(x=430, y=400)


