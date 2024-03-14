
import customtkinter as ctk
from CTkListbox import *
from customtkinter import filedialog    
import os
from nmr import rename_files




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
#listbox for renamed
listbox2 = CTkListbox(master=window)


def get_folder():
    folder_name = filedialog.askdirectory()
    path = folder_name
    files = os.listdir(folder_name)
    counter = 0
    for file in files:
        counter += 1
        listbox.insert(counter, file)



listbox.grid(row=1, columnspan=2, sticky="nsw", padx=15)
listbox2.grid(row=1, columnspan=2, sticky="nse", padx=15)

#select file button should open file dialog and accept a folder to get filenames from
file_select_btn = ctk.CTkButton(master=window, text="select files", command=get_folder)
file_select_btn.grid(row=0, column=0, padx=5, sticky="w")

#should run rename function on selected folder
file_convert_btn = ctk.CTkButton(master=window, text="rename files")
file_convert_btn.grid(row=2, column=0, padx=5, sticky="w")

window.mainloop()