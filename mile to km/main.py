from tkinter import *

def converter():
    miles = float(mile_entry.get())
    km = 1.60934 * miles
    result.config(text=f'{km}')

window = Tk()
window.title("kilometer to Mile Converter")
window.minsize(width=200,height=100)
window.config(padx=50, pady=50)

#declaring
is_equal = Label(text="Is equal to")
mile_label = Label(text="Miles")
km_label = Label(text="Kms")
result = Label(text='0')
mile_entry = Entry(width=10)

calculate_button = Button(text="Calculate", command=converter)

#griding
mile_entry.grid(column=1,row=1)
mile_label.grid(column=2, row=1)
is_equal.grid(column=0,row=2)
result.grid(column=1,row=2)
km_label.grid(column=2,row=2)
calculate_button.grid(column=1,row=3)




window.mainloop()
