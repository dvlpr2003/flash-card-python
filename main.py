from tkinter import *
import time
from quiz import quiz
root = Tk()
root.geometry("800x500")
root.title("FLASH CARD")
myLabel = Label(text="",font=("Ariel",20,"bold"))
myLabel.pack()
canva = Canvas(root,width=200,height=200,bg="blue" )
canva.pack(pady=70)
check_condition = False
canvatxt = canva.create_text(100,100,text="Start")
Questionlvl = 0
def change_color():
    global Questionlvl
    global check_condition
    if not check_condition:
        canva.config(bg="red")
        canva.itemconfig(cavatxt,text =quiz[Questionlvl]["Question"])
        myLabel.config(text="Question")
        check_condition = True
    else:
        canva.config(bg="green")
        canva.itemconfig(cavatxt,text=quiz[Questionlvl]["Answer"])
        myLabel.config(text="Answer")

        if len(quiz)-1 >Questionlvl:
            Questionlvl+=1
            check_condition = False
        
btn = Button(root,text="click" ,command=change_color)
btn.pack()
root.mainloop()