from tkinter import *
import backend

def get_selected_row(event):
    if len(lb.curselection()) > 0:
        global selected_item
        index=lb.curselection()
        selected_item=lb.get(index)
        title_entry.delete(0,END)
        title_entry.insert(END,selected_item[1])
        author_entry.delete(0,END)
        author_entry.insert(END,selected_item[2])
        year_entry.delete(0,END)
        year_entry.insert(END,selected_item[3])
        isbn_entry.delete(0,END)
        isbn_entry.insert(END,selected_item[4])


def view_db():
    lb.delete(0,END)
    for row in backend.view():
        lb.insert(END,row)

def search_db():
    lb.delete(0,END)
    for row in backend.search(title_value.get(),author_value.get(),year_value.get(),isbn_value.get()):
        lb.insert(END,row)

def add_db():
    lb.delete(0,END)
    backend.insert(title_value.get(),author_value.get(),year_value.get(),isbn_value.get())
    lb.insert(END,(title_value.get(),author_value.get(),year_value.get(),isbn_value.get()))

def update_db():
    backend.update(selected_item[0],title_value.get(),author_value.get(),year_value.get(),isbn_value.get())

def delete_db():
    backend.delete(selected_item[0])

window=Tk()

window.wm_title("Bookstore Database App")

title_label=Label(window,text="Title")
title_label.grid(row=0,column=0)
title_value=StringVar()
title_entry=Entry(window,textvariable=title_value)
title_entry.grid(row=0,column=1)

author_label=Label(window,text="Author")
author_label.grid(row=0,column=2)
author_value=StringVar()
author_entry=Entry(window,textvariable=author_value)
author_entry.grid(row=0,column=3)

year_label=Label(window,text="Year")
year_label.grid(row=1,column=0)
year_value=StringVar()
year_entry=Entry(window,textvariable=year_value)
year_entry.grid(row=1,column=1)

isbn_label=Label(window,text="ISBN")
isbn_label.grid(row=1,column=2)
isbn_value=StringVar()
isbn_entry=Entry(window,textvariable=isbn_value)
isbn_entry.grid(row=1,column=3)

lb = Listbox(window,height=6,width=35)
lb.grid(row=2,column=0,rowspan=6,columnspan=2)

sb=Scrollbar(window)
sb.grid(row=2,column=2, rowspan=6)

lb.configure(yscrollcommand=sb.set)
sb.configure(command=lb.yview)

lb.bind('<<ListboxSelect>>',get_selected_row)

viewall_button=Button(window,text="View All",width=12,command=view_db)
viewall_button.grid(row=2,column=3)

searchentry_button=Button(window,text="Search Entry",width=12,command=search_db)
searchentry_button.grid(row=3,column=3)

addentry_button=Button(window,text="Add Entry",width=12,command=add_db)
addentry_button.grid(row=4,column=3)

update_button=Button(window,text="Update",width=12,command=update_db)
update_button.grid(row=5,column=3)

delete_button=Button(window,text="Delete",width=12,command=delete_db)
delete_button.grid(row=6,column=3)

close_button=Button(window,text="Close",width=12,command=window.destroy)
close_button.grid(row=7,column=3)


window.mainloop()