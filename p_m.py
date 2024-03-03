from tkinter import *
from cryptography.fernet import Fernet
import os
from tkinter import messagebox

def main_windows():
    windows = Tk()
    windows.title("Password Manager")
    windows.geometry("330x450")
    windows.configure(bg="#164863")
    label_wel=Label(windows,text="Hi Wlecome To Passmanger",
                    font=("Ahang BlackSharp",15),fg="#DDF2FD",bg="#164863")
    label_wel.pack(side="top",pady=(70,1))
    butto_add=Button(windows,text="Add",font=("Ahang BlackSharp",15),
           bg="#427D9D",fg="#DDF2FD",command=lambda:(add_1()))        
    butto_add.pack(side="left",padx=(100,2))

    butto_view=Button(windows,text="View",font=("Ahang BlackSharp",15),
           bg="#427D9D",fg="#DDF2FD",command=lambda:(view_1()))        
    butto_view.pack(side="left",padx=(1,2))

    def make_key():
        key = Fernet.generate_key()
        with open("G:\Coding\Python\password manager\key.key","wb") as file_key:
            file_key.write(key)


    def load_key():
        file=open("G:\Coding\Python\password manager\key.key","rb")
        key=file.read()
        file.close()
        return key


    if os.path.exists("G:\Coding\Python\password manager\key.key"):
        print("key exist")
        pass
    else:
        print("key made")
        make_key()


    key=load_key()
    fer = Fernet(key)
    def add_1():
        def add_distroy():
            windows_add.destroy()
        windows.destroy()
        windows_add = Tk()
        windows_add.title("Password Add")
        windows_add.configure(bg="#164863")
        windows_add.geometry("430x450")

        label_user=Label(windows_add,text="User Name:",font=("Ahang BlackSharp",15),
           bg="#164863",fg="#DDF2FD")
        label_user.grid(row=1,column=0,padx=10,pady=(50,5))

        entry_user=Entry(windows_add,bg="white",fg="black",font=("Ahang BlackSharp",15))
        entry_user.grid(row=1,column=1,padx=1,pady=(50,5))

        label_passw=Label(windows_add,text="Password:",font=("Ahang BlackSharp",15),
           bg="#164863",fg="#DDF2FD")
        label_passw.grid(row=2,column=0,padx=5,pady=5)


        entry_passw=Entry(windows_add,bg="white",fg="black",font=("Ahang BlackSharp",15))
        entry_passw.grid(row=2,column=1,padx=1,pady=5)
        def checker():
            if entry_passw.get()=="" or entry_user.get()=="":
                messagebox.showerror("Error","You Must Fill User And Password!!")
            else:
                add()
        butto_submit=Button(windows_add,text="Submit",font=("Ahang BlackSharp",15),width=18,
           bg="#427D9D",fg="#DDF2FD",command=lambda:(checker()))
        butto_submit.grid(row=4,column=1,padx=1,pady=5)

        butto_back=Button(windows_add,text="Back",font=("Ahang BlackSharp",13),
           bg="#427D9D",fg="#DDF2FD",command=lambda:(add_distroy(),main_windows()))
        butto_back.grid(row=0,column=0,padx=1,pady=1,ipadx=1)

        # label_submit=Label(windows_add,text="",font=("Ahang BlackSharp",15),
        #    bg="#164863",fg="#DDF2FD")
        # label_submit.grid(row=4,column=1,padx=10,pady=(5,5))


        # butto_exit=Button(windows_add,text="Exit",font=("Ahang BlackSharp",15),width=18,
        #    bg="#427D9D",fg="#DDF2FD",command=lambda:())
        # butto_exit.grid(row=4,column=1,padx=1,pady=5)
        def label_remove():
            butto_submit.config(text="Submit",
            bg="#427D9D",fg="#DDF2FD")
            entry_user.delete(0, END)
            entry_passw.delete(0,END)
        def add():
            name=entry_user.get()
            passw=entry_passw.get()

            with open("G:\Coding\Python\password manager\password.txt","a") as f :
                f.write(name + "|" + fer.encrypt(passw.encode()).decode() + "\n")
            butto_submit.config(text="Done!",
           bg="#9BCF53",fg="#DDF2FD")
            windows_add.after(1500,label_remove)
        windows_add.mainloop()



    def view_1():
        def view_distroy():
            windows_view.destroy()
        windows.destroy()
        if os.path.exists("G:\Coding\Python\password manager\password.txt"):
            print("pass.txt exist")
        else:
            print("pass.txt not exist")
            messagebox.showerror("Error 404","You Not Have Any Password File First Add New User")
            main_windows()
            return
        windows_view = Tk()
        windows_view.title("Password View")
        windows_view.geometry("430x450")
        windows_view.configure(bg="#164863")
        butto_back=Button(windows_view,text="Back",font=("Ahang BlackSharp",13),
           bg="#427D9D",fg="#DDF2FD",command=lambda:(view_distroy(),main_windows()))
        butto_back.pack(anchor="w")
        text=Text(windows_view,bg="#427D9D",fg="#F5F5F5",font=("Ahang BlackSharp",13))
        text.pack(fill="both",expand=True)
        with open("G:\Coding\Python\password manager\password.txt" , "r") as f:
            for line in f.readlines():
                data = line.rstrip()
                name, passw=data.split("|")
                result="User Name: {0} | Password: {1}\n".format(name,fer.decrypt(passw.encode()).decode())
                # text.delete(1.0, END)
                text.insert(END, result)
        
        windows_view.mainloop()





# # while True:
#     first_answer=input("Please Type What do you want do? (add , view) for quit type q\n answer: ").lower()
#     if first_answer=="q":
#         print("\n see you\U0001F44B ... \n ")
#         quit()
#     elif first_answer=="view":
#         view()
#     elif first_answer=="add":
#         add()
        
    windows.mainloop()
main_windows()