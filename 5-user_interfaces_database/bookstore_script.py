from tkinter import *
from backend import Database

database=Database()

class Window:

    def __init__(self,window):

        self.window=window
        self.window.wm_title("Bookstore Database App")
        
        title_label=Label(window,text="Title")
        title_label.grid(row=0,column=0)
        self.title_value=StringVar()
        self.title_entry=Entry(window,textvariable=self.title_value)
        self.title_entry.grid(row=0,column=1)

        author_label=Label(window,text="Author")
        author_label.grid(row=0,column=2)
        self.author_value=StringVar()
        self.author_entry=Entry(window,textvariable=self.author_value)
        self.author_entry.grid(row=0,column=3)

        year_label=Label(window,text="Year")
        year_label.grid(row=1,column=0)
        self.year_value=StringVar()
        self.year_entry=Entry(window,textvariable=self.year_value)
        self.year_entry.grid(row=1,column=1)

        isbn_label=Label(window,text="ISBN")
        isbn_label.grid(row=1,column=2)
        self.isbn_value=StringVar()
        self.isbn_entry=Entry(window,textvariable=self.isbn_value)
        self.isbn_entry.grid(row=1,column=3)

        self.lb = Listbox(window,height=6,width=35)
        self.lb.grid(row=2,column=0,rowspan=6,columnspan=2)

        sb=Scrollbar(window)
        sb.grid(row=2,column=2, rowspan=6)

        self.lb.configure(yscrollcommand=sb.set)
        sb.configure(command=self.lb.yview)

        self.lb.bind('<<ListboxSelect>>',self.get_selected_row)

        viewall_button=Button(window,text="View All",width=12,command=self.view_db)
        viewall_button.grid(row=2,column=3)

        searchentry_button=Button(window,text="Search Entry",width=12,command=self.search_db)
        searchentry_button.grid(row=3,column=3)

        addentry_button=Button(window,text="Add Entry",width=12,command=self.add_db)
        addentry_button.grid(row=4,column=3)

        update_button=Button(window,text="Update",width=12,command=self.update_db)
        update_button.grid(row=5,column=3)

        delete_button=Button(window,text="Delete",width=12,command=self.delete_db)
        delete_button.grid(row=6,column=3)

        close_button=Button(window,text="Close",width=12,command=window.destroy)
        close_button.grid(row=7,column=3)

    def get_selected_row(self,event):
        if len(self.lb.curselection()) > 0:
            index=self.lb.curselection()
            self.selected_item=self.lb.get(index)
            self.title_entry.delete(0,END)
            self.title_entry.insert(END,self.selected_item[1])
            self.author_entry.delete(0,END)
            self.author_entry.insert(END,self.selected_item[2])
            self.year_entry.delete(0,END)
            self.year_entry.insert(END,self.selected_item[3])
            self.isbn_entry.delete(0,END)
            self.isbn_entry.insert(END,self.selected_item[4])


    def view_db(self):
        self.lb.delete(0,END)
        for row in database.view():
            self.lb.insert(END,row)

    def search_db(self):
        self.lb.delete(0,END)
        for row in database.search(self.title_value.get(),self.author_value.get(),self.year_value.get(),self.isbn_value.get()):
            self.lb.insert(END,row)

    def add_db(self):
        self.lb.delete(0,END)
        database.insert(self.title_value.get(),self.author_value.get(),self.year_value.get(),self.isbn_value.get())
        self.lb.insert(END,(self.title_value.get(),self.author_value.get(),self.year_value.get(),self.isbn_value.get()))

    def update_db(self):
        database.update(self.selected_item[0],self.title_value.get(),self.author_value.get(),self.year_value.get(),self.isbn_value.get())

    def delete_db(self):
        database.delete(self.selected_item[0])


window=Tk()
Window(window)
window.mainloop()