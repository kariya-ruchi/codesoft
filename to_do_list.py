from tkinter import *
from tkinter import ttk

class task1:
    def __init__(self,root):
        self.root=root
        self.root.title("To-do List")
        self.root.geometry('600x600+400+200')
        self.label=Label(self.root,text='TO DO LIST',
                         font="cursive, 30 italic bold",width=20,bd=15,fg='black')
        self.label.pack(side='top',fill=BOTH)


        self.label2=Label(self.root,text='Add Your Task',
                         font='cursive,20',width=20,bd=10,bg='black',fg='yellow')
        self.label2.place(x=20,y=90)


        self.label3=Label(self.root,text='Tasks to do',
                         font='cursive,20',width=20,bd=10,bg='black',fg='yellow')
        self.label3.place(x=320,y=90)


        self.main_text=Listbox(self.root,height=11,bd=5,width=24,font="cursive,25")
        self.main_text.place(x=300,y=170)


        self.text=Text(self.root,bd=5,height=8,width=17,font="ariel, 20 bold")
        self.text.place(x=10,y=170)



        def add():
            content=self.text.get(1.0,END)
            self.main_text.insert(END,content)
            result = open("tasks.txt","a")
            print(result.read())
            #with open('tasks.txt','a') as file:
            result.write(content)
            result.seek(0)
            result.close()
            self.text.delete(1.0,END)

        def delete():
            delete_= self.main_text.curselection()
            look=self.main_text.get(delete_)
            with open('tasks.txt','r+') as f:
                new_f=f.readlines()
                f.seek(0)
                for line in new_f:
                    item=str(look)
                    if item not in line:
                        f.write(line)
                f.truncate()
            self.main_text.delete(delete_)


            result = open("tasks.txt","r")
            print(result.read())
        # with open("tasks.txt","r") as file:
            read=result.readlines()
            for i in read():
                ready=i.split()
                self.main_text.insert(END,ready)
            result.close()


        self.button=Button(self.root,text="ADD",font="sarif, 20 bold",
                           width=8,bd=5,bg='black',fg='yellow',command=add)
        self.button.place(x=100,y=500)

        self.button1=Button(self.root,text="REMOVE",font="sarif, 20 bold",
                           width=8,bd=5,bg='black',fg='yellow',command=delete)
        self.button1.place(x=320,y=500)


def main():
    root=Tk()
    ui=task1(root)
    root.mainloop()

if __name__ == "__main__":
    main()