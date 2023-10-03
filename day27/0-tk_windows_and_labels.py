#!/usr/bin/env python3
"""
Creating a window in Tkinter and using labels(titles etc)
"""
import tkinter

# Create a window instance
window = tkinter.Tk()

# Add a title to the window GUI
window.title("My First GUI Program")

# Specifying dimensions for the window
window.minsize(width=500, height=400)

"""
LABELS - Working with the Label method
"""

my_label = tkinter.Label(text="I am a label", font=("Arial", 23, "bold"))
my_label.pack()

# Setting options
my_label["text"] = "Some New Text"  # Option 1
my_label.config(text="New Text")    # Option 2


"""
BUTTONS
"""


def button_clicked():
    """
    Triggers an event when the button is clicked
    """
    new_text = entry.get()
    my_label.config(text="Ouch! 🤕  {}".format(new_text))


button = tkinter.Button(
    text="Don't poke me!",
    command=button_clicked
)
button.pack()


"""
ENTRY BOXES
"""
entry = tkinter.Entry(width=12)
entry.pack()


# Get the screen to show up
window.mainloop()
