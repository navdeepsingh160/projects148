from tkinter import *
import random

root=Tk()
root.title("picnic bag List")
root.geometry("400x400")

random_number_list = Label(root)
list_of_items = Label(root)

list1 = ["bottle", "tiffin", "ID Card", "chocolates", "chips", "titkets", "hancky"]
list_of_items["text"] = "listed items " +str(list1)

def randomlist():
    randomlist = random.sample(range(0,8),1)
    random_number_list["text"] = "put item number : " + str(randomlist) +" in bag"
   
    
btn=Button(root, text="put item ", command=randomlist)
btn.place(relx=0.5,rely=0.4,anchor=CENTER)


random_number_list.place(relx=0.5,rely=0.5,anchor=CENTER)
list_of_items.place(relx=0.5,rely=0.6,anchor=CENTER)
    


root.mainloop()