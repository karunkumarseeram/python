from tkinter import *
root = Tk()
root.title("calculator")
#width and height , and background color of the calci
root.geometry("570x600+100+200")
root.resizable(False,False)
root.configure(bg="#1a0000")

#giving a commaand to the buttons

equation = ""

def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)

#giving response to the clear
def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

#giving the response to the operations on values
def calculate():
    global equation
    res = ""
    if equation!="":
        try:
            res=eval(equation)
        except:
            res = "error"
            equation=""
    label_result.config(text=res)

#divide the calci screen and operations workplace
label_result = Label(root,width=25,height=2,text="",font=("arial",30))
label_result.pack()

#divide the each button its width and styling to it
Button(root,width=5,height=1,text="C",font=("arial",30,"bold"),bd=2,fg="#fff",bg="#51449D",command=lambda :clear()).place(x=10,y=100)
Button(root,width=5,height=1,text="/",font=("arial",30,"bold"),bd=2,fg="#fff",bg="#2a2d36",command=lambda :show("/")).place(x=150,y=100)
Button(root,width=5,height=1,text="%",font=("arial",30,"bold"),bd=2,fg="#fff",bg="#2a2d36",command=lambda :show("%")).place(x=290,y=100)
Button(root,width=5,height=1,text="*",font=("arial",30,"bold"),bd=2,fg="#fff",bg="#2a2d36",command=lambda :show("*")).place(x=430,y=100)

Button(root,width=5,height=1,text="7",font=("arial",30,"bold"),bd=2,fg="#fff",bg="#2a2d36",command=lambda :show("7")).place(x=10,y=200)
Button(root,width=5,height=1,text="8",font=("arial",30,"bold"),bd=2,fg="#fff",bg="#2a2d36",command=lambda :show("8")).place(x=150,y=200)
Button(root,width=5,height=1,text="9",font=("arial",30,"bold"),bd=2,fg="#fff",bg="#2a2d36",command=lambda :show("9")).place(x=290,y=200)
Button(root,width=5,height=1,text="-",font=("arial",30,"bold"),bd=2,fg="#fff",bg="#2a2d36",command=lambda :show("-")).place(x=430,y=200)


Button(root,width=5,height=1,text="4",font=("arial",30,"bold"),bd=2,fg="#fff",bg="#2a2d36",command=lambda :show("4")).place(x=10,y=300)
Button(root,width=5,height=1,text="5",font=("arial",30,"bold"),bd=2,fg="#fff",bg="#2a2d36",command=lambda :show("5")).place(x=150,y=300)
Button(root,width=5,height=1,text="6",font=("arial",30,"bold"),bd=2,fg="#fff",bg="#2a2d36",command=lambda :show("6")).place(x=290,y=300)
Button(root,width=5,height=1,text="+",font=("arial",30,"bold"),bd=2,fg="#fff",bg="#2a2d36",command=lambda :show("+")).place(x=430,y=300)


Button(root,width=5,height=1,text="1",font=("arial",30,"bold"),bd=2,fg="#fff",bg="#2a2d36",command=lambda :show("1")).place(x=10,y=400)
Button(root,width=5,height=1,text="2",font=("arial",30,"bold"),bd=2,fg="#fff",bg="#2a2d36",command=lambda :show("2")).place(x=150,y=400)
Button(root,width=5,height=1,text="3",font=("arial",30,"bold"),bd=2,fg="#fff",bg="#2a2d36",command=lambda :show("3")).place(x=290,y=400)
Button(root,width=11,height=1,text="0",font=("arial",30,"bold"),bd=2,fg="#fff",bg="#2a2d36",command=lambda :show("0")).place(x=10,y=500)

Button(root,width=5,height=1,text=".",font=("arial",30,"bold"),bd=2,fg="#fff",bg="#2a2d36",command=lambda :show(".")).place(x=290,y=500)
Button(root,width=5,height=3,text="=",font=("arial",30,"bold"),bd=2,fg="#fff",bg="#fe9037",command=lambda :calculate()).place(x=430,y=400)
root.mainloop()