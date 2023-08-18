from tkinter import *
from tkinter.ttk import Combobox
import string,random

root=Tk()
root.geometry("600x500")
root.title("Password Generator")
root.config(bg="beige")
root.resizable(False,False)


def pass_gen():
    length_password=numbers.get()
    small=string.ascii_lowercase
    capital=string.ascii_uppercase
    digits=string.digits
    special_char=string.punctuation
    all_lists=[]
    all_lists.extend(list(small))
    all_lists.extend(list(capital))
    all_lists.extend(list(digits))
    all_lists.extend(list(special_char))
    random.shuffle(all_lists)
    password.set("".join(all_lists[0:length_password]))


all_no={"6":"6","7":"7","8":"8","9":"9","10":"10","11":"11","12":"12","13":"13","14":"14","15":"15"}


Title=Label(root,text="RANDOM PASSWORD GENERATOR",bg="beige",fg="red",font=("algerian",20,"bold"))
Title.pack(anchor="center",pady="25px")

length=Label(root,text="Length:-",fg="green",bg="beige",font=("futura",15))
length.place(x="70px",y="75px")

strength=Label(root,text="Strength:-",fg="green",bg="beige",font=("futura",15))
strength.place(x="70px",y="120px")

numbers=IntVar()
selector=Combobox(root,textvariable=numbers,state="readonly")
selector['value']=[l for l in all_no]
selector.current(2)
selector.place(x="150px",y="77px")


def sel():
    sel=choice.get()

choice=IntVar()
R1=Radiobutton(root,text="POOR",variable=choice,value=1,command=sel).place(x="180px",y="120px")
R2=Radiobutton(root,text="AVERAGE",variable=choice,value=2,command=sel).place(x="180px",y="140px")
R3=Radiobutton(root,text="ADVANCE",variable=choice,value=3,command=sel).place(x="180px",y="160px")


gen_btn=Button(root,text="Generate",command=pass_gen,bg="orange",fg="black",font=("ubuntu",10),cursor="hand2")
gen_btn.place(x="180px",y="200px")

result=Label(root,text="Generated password :-",bg="beige",fg="darkgreen",font=("futura",15))
result.place(x="60px",y="250px")

password=StringVar()
password_final=Entry(root,textvariable=password,state="readonly",fg="blue",font=("futura",15))
password_final.place(x="230px",y="250px")
root.mainloop()
'''
from turtle import *
color("red")
begin_fill()
pensize(3)
left(50)
forward(133)
circle(50,200)
forward(133)
end_fill()'''
