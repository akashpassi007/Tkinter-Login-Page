from tkinter import*
from tkinter import messagebox
from PIL import ImageTk

class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")

        ############## All Images ######################
        self.bg_icon=ImageTk.PhotoImage(file=r"I:\JavaScript\Images/bg.jpg")
        self.logo_icon=ImageTk.PhotoImage(file=r"I:\JavaScript\Images\logo.jpg")
        self.user_icon=ImageTk.PhotoImage(file=r"I:\JavaScript\Images\user.png")
        self.password_icon=ImageTk.PhotoImage(file=r"I:\JavaScript\Images\password.png")

        ############## Variable ###########
        self.uname=StringVar()
        self.pass_=StringVar()
        
        bg_lbl=Label(self.root,image=self.bg_icon).pack()
        
        Title=Label(self.root,text="Login System",font=("times new roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
        Title.place(x=0,y=0,relwidth=1)

        Login_Frame=Frame(self.root,bg="white")
        Login_Frame.place(x=80,y=90)

        logolbl=Label(Login_Frame,image=self.logo_icon,bd=0).grid(row=0,columnspan=2,pady=0)

        userlbl=Label(Login_Frame,text="Username",image=self.user_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(row=1,column=0,padx=10,pady=10)
        usertxt=Entry(Login_Frame,bd=5,textvariable=self.uname,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)

        
        passowrdlbl=Label(Login_Frame,text="Password",image=self.password_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(row=2,column=0,padx=20,pady=10)
        passwordtxt=Entry(Login_Frame,bd=5,relief=GROOVE,textvariable=self.pass_,font=("",15)).grid(row=2,column=1,padx=20)

        btn_log=Button(Login_Frame,command=self.Login,text="Login",width=15,font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=3,column=1,pady=10)

    def Login(self):
        if self.uname.get()==" " or self.pass_.get()==" ":
            messagebox.showinfo("Error","All fields are required!!")
        elif self.uname.get()=="Akash" and self.pass_.get()=="12345":
            messagebox.showinfo("Successful")
        else: 
            messagebox.showerror("Error","Invalid Username or Password")
            

root=Tk()
obj=Login_System(root)
root.mainloop()
