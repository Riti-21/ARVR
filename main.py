from tkinter import*
from PIL import Image, ImageTk
from tkinter import messagebox
import os

from Air_canvas import canvas
from Harry_Potter_cloak import cloak
from ar import animal

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x720+0+0")
        self.root.title("Game Zone")
        img=Image.open(r"img/header.png")
        img=img.resize((1366,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1366,height=130)

        img3=Image.open(r"img/banner.jpg")
        img3=img3.resize((1365,620),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1365,height=620)

        title_lbl=Label(bg_img,text="Game Zone", font=("time new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1365,height=45)

        img4=Image.open(r"img/pic1.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,cursor="hand2",command=self.air_canvas)
        b1.place(x=100,y=60,width=220,height=220)

        b1_1=Button(bg_img,text="Air Canvas",cursor="hand2", font=("time new roman",15,"bold"),bg="darkblue",fg="white",command=self.air_canvas)
        b1_1.place(x=100,y=260,width=220,height=40)

        img7=Image.open(r"img/pic2.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.hp)
        b1.place(x=400,y=60,width=220,height=220)

        b1_1=Button(bg_img,text="Harry Potter Cloak",cursor="hand2", font=("time new roman",15,"bold"),bg="darkblue",fg="white",command=self.hp)
        b1_1.place(x=400,y=260,width=220,height=40)

        img5=Image.open(r"img/pic3.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.ar)
        b1.place(x=700,y=60,width=220,height=220)

        b1_1=Button(bg_img,text="AR Animal",cursor="hand2", font=("time new roman",15,"bold"),bg="darkblue",fg="white",command=self.ar)
        b1_1.place(x=700,y=260,width=220,height=40)

        img9=Image.open(r"img/exit.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,command=self.exit,image=self.photoimg9,cursor="hand2")
        b1.place(x=1000,y=60,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",command=self.exit,cursor="hand2", font=("time new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=260,width=220,height=40)


    def air_canvas(self):
        self.new_window=Toplevel(self.root)
        self.app=canvas(self.new_window)

    def hp(self):
        self.new_window=Toplevel(self.root)
        self.app=cloak(self.new_window)

    def ar(self):
        self.new_window=Toplevel(self.root)
        self.app=animal(self.new_window)


    def open_img(self):
        os.startfile("data")



    def exit(self):
        self.exit=messagebox.askyesno("Face Recognition","Are you sure you want to exit?",parent=self.root)
        if self.exit >0:
            self.root.destroy()
        else:
            return










if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()