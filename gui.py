# https://www.youtube.com/watch?v=vusUfPBsggw&ab_channel=CodeFirstwithHala
# https://github.com/codefirstio/tkinter-data-entry
# https://aesl.ces.uga.edu/soil/fertcalc/

import tkinter as tk
from tkinter import ttk

from db import fertilizer_db

window = tk.Tk()
window.title("fertili Lab")

frame = tk.Frame(window)
frame.pack(padx=10, pady=20)

def get_client_info():
    fname = fname_entry.get()
    lname = lname_entry.get()
    address = address_entry.get()
    contact = contact_entry.get()
    email = email_entry.get()
    parish = parish_entry.get()
    print(fname)


def generate_report():
    for checked in checked_fertilizers:
        if checked is not None:
            print(checked.get())
    get_client_info()

# saving user information
client_info_frame = tk.LabelFrame(frame, text='Client Information')
client_info_frame.grid(row=0, column=0, padx=10, pady=20, sticky="w")

fname_label = tk.Label(client_info_frame, text='First Name :')
fname_entry= tk.Entry(client_info_frame)
fname_label.grid(row=0, column=0, sticky="e")
fname_entry.grid(row=0, column=2)

lname_label = tk.Label(client_info_frame, text='Last Name :')
lname_entry= tk.Entry(client_info_frame)
lname_label.grid(row=1, column=0, sticky="e")
lname_entry.grid(row=1, column=2)

address_label = tk.Label(client_info_frame, text='Address :')
address_entry= tk.Entry(client_info_frame)
address_label.grid(row=2, column=0, sticky="e")
address_entry.grid(row=2, column=2)

parish_list = ["Kingston", "St. Andrew", "St. Catherine", "Clarendon", "Manchester", "St. Elizabeth",
          "Westmoreland", "Hanover", "St. James", "Trelawny", "St. Ann", "St. Mary", "Portland",
          "St. Thomas"]

parish = tk.StringVar()
parish_label = tk.Label(client_info_frame, text='Parish :')
parish_entry= ttk.Combobox(client_info_frame, value=parish_list)
parish_label.grid(row=3, column=0, sticky="e")
parish_entry.grid(row=3, column=2)

email_label = tk.Label(client_info_frame, text=' Email :')
email_entry= tk.Entry(client_info_frame)
email_label.grid(row=4, column=0, sticky="e")
email_entry.grid(row=4, column=2)

contact_label = tk.Label(client_info_frame, text='Contact :')
contact_entry= tk.Entry(client_info_frame)
contact_label.grid(row=5, column=0, sticky="e")
contact_entry.grid(row=5, column=2)

for widget in client_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# ---------------------------------------------------------------------- End of personal section -----------------------


# ------------------------------------------------------------------------ Fertilizer Section
# ------
fertilizer_frame = tk.LabelFrame(frame, text='Step 2 select available Blend')
fertilizer_frame.grid(row=1, column=0, padx=10, pady=10, sticky='w', ipadx=10, ipady=10)

col1_row = 0
col2_row = 0
checked_fertilizers = []
#https://9to5answer.com/how-do-i-create-multiple-checkboxes-from-a-list-in-a-for-loop-in-python-tkinter
for index, fertilizer in enumerate(fertilizer_db.fertilizer_collections):
    lenght = len(fertilizer_db.fertilizer_collections)
    if index < lenght / 2:
        checked_fertilizers.append(tk.StringVar(value=1))
        l = len(checked_fertilizers)
        tk.Checkbutton(fertilizer_frame, text=fertilizer['formation'],
                       variable=checked_fertilizers[l-1], onvalue=fertilizer['formation']).grid(sticky="w", column=0, row=col1_row)
        tk.Label(fertilizer_frame, text=fertilizer["name"],  font=("Arial", 8), ).grid(column=1, row=col1_row, sticky="w")
        col1_row += 1
    else:
        checked_fertilizers.append(tk.StringVar(value=1))
        l=len(checked_fertilizers)
        tk.Checkbutton(fertilizer_frame, text=fertilizer['formation'],
                       variable=checked_fertilizers[l-1], onvalue=fertilizer['formation']).grid(sticky="w", column=2, row=col2_row)
        tk.Label(fertilizer_frame, text=fertilizer["name"], font=("Arial", 8)).grid(column=3, row=col2_row, sticky="w")
        col2_row += 1

for widget in fertilizer_frame.winfo_children():
    widget.grid_configure(padx=5, pady=5)


# ------------------------------------------------------------------- Analysis Input -----------------------


soil_text_frame = tk.Frame(frame) # --------------------- Frame for data from soil Text--------------
soil_text_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nw")

input_frame = tk.LabelFrame(soil_text_frame, text="MO & pH")
input_frame.grid(row=0, column=0, sticky="nw")

tk.Label(input_frame, text='pH').grid(row=0, column=0, sticky="w", padx=10)
ph_entry = tk.Spinbox(input_frame, width=15, increment=0.1, from_=0, to=14)
ph_entry.grid(row=1, column=0, padx=10, pady=10)

tk.Label(input_frame, text='MO').grid(row=0, column=1, sticky="w", padx=10)
ph_entry = tk.Entry(input_frame, width=15)
ph_entry.grid(row=1, column=1, padx=10, pady=10)


# -------------------------------------------------------------------------------------------
parameters = ["N", "P2O5", "K2O"]
parameters_frame = tk.LabelFrame(soil_text_frame, text="Soil Test Result")
parameters_frame.grid(row=1, column=0, pady=10, ipadx=10, ipady=10)

for index, param in enumerate(parameters):
    tk.Label(parameters_frame, text=param).grid(row=0, column=index, padx=10, sticky="w")
    tk.Entry(parameters_frame, width=15).grid(row=1, column=index, padx=10, )


generate_report_button = tk.Button(soil_text_frame, text="Generate Report", command=generate_report)  # Button for report generation
generate_report_button.grid(row=2, column=0, sticky="w")


window.mainloop()

















#from tkinter import ttk
# https://www.youtube.com/watch?v=unSu-n5VIL4
# https://www.youtube.com/watch?v=9sBiX-idksc
# Todo: use the third link above





# class Ui:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Fertilizer Generater")
#         self.root.minsize(width=1000, height=500)
#         self.GUI()
#
#
#     def GUI(self):
#         entry_style = ttk.Style()
#         entry_style.configure(
#             'style.TEntry',
#             Entry="red",
#             foreground="red"
#         )
#         frame = ttk.Labelframe(self.root, text="SOIL TEXT RESULT", padding=10)
#         #frame.grid(row=0, column=0)
#         frame.place(relx=0.2, rely=0.2, anchor="w")
#
#         n_label = ttk.Label(frame, text="N")
#         n_label.grid(row=1, column=0, pady=3)
#         n_input = ttk.Entry(frame, text="N", style="style.TEntry")
#         n_input.grid(row=1, column=1, pady=3)
#
#         P_label = ttk.Label(frame, text="P2O5")
#         P_label.grid(row=2, column=0, pady=3)
#         P_input = ttk.Entry(frame, text="P")
#         P_input.grid(row=2, column=1, pady=3)
#
#         K_label = ttk.Label(frame, text="K20")
#         K_label.grid(row=3, column=0, pady=3)
#         K_input = ttk.Entry(frame, text="K")
#         K_input.grid(row=3, column=1, pady=3)
#
#
# root = tk.Tk()
# window = Ui(root)
# root.mainloop()
#
#
