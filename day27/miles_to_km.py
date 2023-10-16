"""
A Simple miles to KM converter GUI program
"""

import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=30, pady=30)


def mile_converter():
    """
    Converts units from miles to kilometres
    """
    miles = int(entry.get())
    in_km = round(float(miles * 1.60934), 2)
    answer.config(text="{}".format(in_km))


entry = tkinter.Entry(width=5)
entry.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = tkinter.Label(text="is equal to")
equal_label.grid(column=0, row=1)

answer = tkinter.Label(text="0")
answer.grid(column=1, row=1)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)

calc_button = tkinter.Button(text="Calculate", command=mile_converter)
calc_button.grid(column=1, row=2)

window.mainloop()
