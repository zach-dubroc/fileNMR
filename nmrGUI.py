
import customtkinter as ctk
from CTkListbox import *
from customtkinter import filedialog    

#open file dialog, store path
def select_folder():
    foldername=filedialog.askdirectory()
    print(foldername)

 #init window
window = ctk.CTk()
window.title("nmr")
window.geometry("650x450")
window.minsize(width=350, height=250)

#define grid
window.columnconfigure((0,1,2), weight=1)
window.rowconfigure((0,1,2), weight=1)


#header label
head_label = ctk.CTkLabel(master=window, text="file-nmr", font=("monospace", 20))
head_label.grid(row=0,column=1, sticky="nesw")

#listbox for old filenames
listbox = CTkListbox(master=window)
listbox.insert(0,"test 1")
listbox.insert(1,"test 2")
listbox.insert(2,"test 3")
listbox.insert(3,"test 4")
listbox.insert(4,"test 5")
listbox.grid(row=1, columnspan=3, sticky="nsew", padx=15)

#select file button should open file dialog and accept a folder to get filenames from
file_select_btn = ctk.CTkButton(master=window, text="select files", command=select_folder)
file_select_btn.grid(row=0, column=0, padx=5, sticky="w")

#should run rename function on selected folder
file_convert_btn = ctk.CTkButton(master=window, text="convert files")
file_convert_btn.grid(row=2, column=0, padx=5, sticky="w")

window.mainloop()