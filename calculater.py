import tkinter as tk

def num1(x):
    global k1
    global k2
    if(k1==0):
        v1.set(x)
        k1=1
    else:
        n1=str(v1.get())
        v1.set(n1+x)
    k2=0

def opr1(y):
    global k2
    global k3
    global k1
    if(k2==0):
        n2=str(v1.get())
        v1.set(n2+y)
        k2=1
    else:
        back()
        n2=str(v1.get())
        v1.set(n2+y)
        k2=1
    k3=0
    k1=1


def dot1(z):
    global k3
    global k2
    if(k3==0):
        n3=str(v1.get())
        v1.set(n3+z)
        k3=1
    else:
        print("nothing")
    k2=1


    
def equal1():
    global k1
    global k2
    global k3
    n4=str(v1.get())
    a2=eval(n4)
    v1.set(a2)
    k2=0
    k1=0
    k3=1


def back():
    global k2
    global k3
    global k1
    n5=str(v1.get())
    a3=n5[0:len(n5)-1]
    v1.set(a3)
    




frame=tk.Tk()
frame.title("CALCULATER")
v1=tk.StringVar()
k1=0
k2=0
k3=0
v1.set("0")
tk.Entry(frame,font=("arral",20,"bold"),bd=30,bg="powder blue",justify="right",textvariable=v1).grid(columnspan=4)
tk.Button(frame,padx=16,font=("arral",20,"bold"),bd=10,text="1",command=lambda:num1('1')).grid(row=2,column=0)
tk.Button(frame,padx=16,font=("arral",20,"bold"),bd=10,text="2",command=lambda:num1('2')).grid(row=2,column=1)
tk.Button(frame,padx=16,font=("arral",20,"bold"),bd=10,text="3",command=lambda:num1('3')).grid(row=2,column=2)
tk.Button(frame,padx=16,font=("arral",20,"bold"),bd=10,text="+",command=lambda:opr1('+'),bg="black",fg="white").grid(row=2,column=3)


tk.Button(frame,padx=16,font=("arral",20,"bold"),bd=10,text="4",command=lambda:num1('4')).grid(row=3,column=0)
tk.Button(frame,padx=16,font=("arral",20,"bold"),bd=10,text="5",command=lambda:num1('5')).grid(row=3,column=1)
tk.Button(frame,padx=16,font=("arral",20,"bold"),bd=10,text="6",command=lambda:num1('6')).grid(row=3,column=2)
tk.Button(frame,padx=16,font=("arral",20,"bold"),bd=10,text="-",command=lambda:opr1('-'),bg="black",fg="white").grid(row=3,column=3)

    

tk.Button(frame,padx=16,font=("arral",20,"bold"),bd=10,text="7",command=lambda:num1('7')).grid(row=4,column=0)
tk.Button(frame,padx=16,font=("arral",20,"bold"),bd=10,text="8",command=lambda:num1('8')).grid(row=4,column=1)
tk.Button(frame,padx=16,font=("arral",20,"bold"),bd=10,text="9",command=lambda:num1('9')).grid(row=4,column=2)
tk.Button(frame,padx=16,font=("arral",20,"bold"),bd=10,text="*",command=lambda:opr1('*'),bg="black",fg="white").grid(row=4,column=3)



tk.Button(frame,padx=16,font=("arral",20,"bold"),bd=10,text=".",command=lambda:dot1('.'),bg="black",fg="white").grid(row=5,column=0)
tk.Button(frame,padx=16,font=("arral",20,"bold"),bd=10,text="0",command=lambda:num1('0')).grid(row=5,column=1)
tk.Button(frame,padx=16,font=("arral",20,"bold"),bd=10,text="=",command=equal1,bg="red",fg="white").grid(row=5,column=2)
tk.Button(frame,padx=16,font=("arral",20,"bold"),bd=10,text="/",command=lambda:opr1('/'),bg="black",fg="white").grid(row=5,column=3)


tk.Button(frame,padx=16,font=("arral",20,"bold"),bd=10,text="<",command=back,bg="orange",fg="black").grid(row=1,column=3)



frame.mainloop()
        
