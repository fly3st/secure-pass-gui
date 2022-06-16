from doctest import master
import tkinter as tk

window = tk.Tk()
window.title('Secure Password Generator')
window.geometry('500x350')
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

# Password Options menu
frame1 = tk.Frame(master=window, borderwidth=1)
frame1.grid(row=0, column=0, padx=50, pady=100, sticky='w')
label1 = tk.Label(master=frame1, text='Password Options')
label1.grid(padx=0, pady=10, sticky='nw')

symbols_desc = tk.Label(master=frame1, text='Include Symbols:')
symbols_desc.grid(row=1, column=0, sticky='w')

numbers_desc = tk.Label(master=frame1, text='Include Numbers:')
numbers_desc.grid(row=2, column=0, sticky='w')

symbols_desc = tk.Label(master=frame1, text='Include Uppercase Letters:')
symbols_desc.grid(row=3, column=0, sticky='w')

symbols_desc = tk.Label(master=frame1, text='Include Lowercase Letters:')
symbols_desc.grid(row=4, column=0, sticky='w')

pass_len = tk.Label(master=frame1, text='Password Length:')
pass_len.grid(row=5, column=0, sticky='w')


frame2 = tk.Frame(master=window, borderwidth=1)
frame2.grid(row=0, column=1, padx=50, pady= 100, sticky='e')
label2 = tk.Label(master=frame2)
label2.grid(padx=0, pady=10, sticky='nw')

symbols_check = tk.Checkbutton(master=frame2)
symbols_check.grid(row=1, column=0, sticky='w')

numbers_check = tk.Checkbutton(master=frame2)
numbers_check.grid(row=2, column=0, sticky='w')

upper_check = tk.Checkbutton(master=frame2)
upper_check.grid(row=3, column=0, sticky='w')

lower_check = tk.Checkbutton(master=frame2)
lower_check.grid(row=4, column=0, sticky='w')



window.mainloop()