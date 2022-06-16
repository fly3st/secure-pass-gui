import tkinter as tk

window = tk.Tk()

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

# Password Options menu
frame1 = tk.Frame(master=window, borderwidth=1)
frame1.grid(padx=50, pady=100, sticky='w')
label1 = tk.Label(master=frame1, text='Password Options')
label1.grid(padx=0, pady=0, sticky='n')

symbols_check = tk.Checkbutton(master=frame1, text='Use Symbols')
symbols_check.grid(row=1, column=0, padx=5, pady=5, sticky='s')

numbers_check = tk.Checkbutton(master=frame1, text='Use Numbers')
numbers_check.grid(row=2, column=0, padx=5, pady=5, sticky='s')

upper_check = tk.Checkbutton(master=frame1, text='Use Uppercase Letters')
upper_check.grid(row=3, column=0, padx=5, pady=5, sticky='s')

lower_check = tk.Checkbutton(master=frame1, text='Use Lowercase Letters')
lower_check.grid(row=4, column=0, padx=5, pady=5, sticky='s')

window.mainloop()