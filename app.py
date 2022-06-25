import tkinter as tk
from PIL import ImageTk, Image

# Window configuration
window = tk.Tk()
window.title('Secure Password Generator')
window.geometry('620x350')
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
window.iconbitmap('C:\\Users\\danie\\Projects\\Python\\secure-pass-gui\\favicon.ico')

tkvar = tk.StringVar(window)

# Password Options menu
option_frame = tk.Frame(master=window, borderwidth=1)
option_frame.grid(row=0, column=0, padx=50, sticky='w')
options_label = tk.Label(master=option_frame, text='Password Options')
options_label.grid(padx=0, pady=10, sticky='w')

symbols_desc = tk.Checkbutton(master=option_frame, text='Include Symbols')
symbols_desc.grid(row=1, column=0, sticky='w')

numbers_desc = tk.Checkbutton(master=option_frame, text='Include Numbers')
numbers_desc.grid(row=2, column=0, sticky='w')

symbols_desc = tk.Checkbutton(master=option_frame, text='Include Uppercase Letters')
symbols_desc.grid(row=3, column=0, sticky='w')

symbols_desc = tk.Checkbutton(master=option_frame, text='Include Lowercase Letters')
symbols_desc.grid(row=4, column=0, sticky='w')

# Add lock image
lock_image = Image.open('C:\\Users\\danie\\Projects\\Python\\secure-pass-gui\\padlock.png')
lock_tk = ImageTk.PhotoImage(lock_image)

lock_label = tk.Label(image=lock_tk)
lock_label.image = lock_tk
lock_label.place(x=350, y=15)

# Create dropdown menu
numbers = list(range(20, 129)) 
tkvar.set(20) # Set default value

pop_menu = tk.OptionMenu(option_frame, tkvar, *numbers)
length_label = tk.Label(master=option_frame, text='Password Length')
length_label.grid(row=5, column=0, sticky='w')
pop_menu.grid(row=5, column=1)

# Password field
gen_frame = tk.Frame(master=window, borderwidth=1)
gen_frame.grid(row=1, column=0, padx=20, sticky='w')

# Buttons
gen_button = tk.Button(master=gen_frame, text='Generate')
copy_button = tk.Button(master=gen_frame, text='Copy to Clipboard')
export_button = tk.Button(master=gen_frame, text='Export to File')

gen_button.grid(row=2, column=1, sticky='w')
copy_button.grid(row=2, column=2, sticky='w')
export_button.grid(row=2, column=3, sticky='w')

field_entry = tk.Entry(master=gen_frame, width=50)
field_entry.grid(row=2, column=0, padx=10, pady=20)

window.mainloop()