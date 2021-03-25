from tkinter import *

#Create an empty tkinter window
window = Tk()

# Set the size if the window
window.geometry("600x200")

window.title("Grams converter")


# def km_to_miles():
#     miles= float(e1_value.get()) * 1.6
#     t1.insert(END, miles)
#
#
# b1=Button(window,text="Execute",command=km_to_miles)
#
# # To place button in window use pack or grid. It is preferable to use grid because it gives more control over the placement of the button
# b1.grid(row=0,column=0)
#
#
# e1_value=StringVar()
# e1=Entry(window, textvariable=e1_value)
# e1.grid(row=0,column=1)
#
# t1=Text(window, height=1, width=20,)
# t1.grid(row=0, column=2)
#
#
# window.mainloop()

# Create function for calculations
def kilo_grams():
    # Get user value from input box and multiply by 1000 to get grams
    grams = float(userinput_value.get()) * 1000

    # Get user value from input box and multiply by 2.20462 to get pounds
    pound = float(userinput_value.get()) * 2.20462

    # Get user value from input box and multiply by 35.274 to get ounces
    ounce = float(userinput_value.get()) * 35.274
    # Empty the Text boxes if they had text from the previous use and fill them again

    textbox.delete("1.0", END)  # Deletes the content of the Text box from start to END
    textbox.insert(END, grams)  # Fill in the text box with the value of gram variable
    textbox2.delete("1.0", END)
    textbox2.insert(END, pound)
    textbox3.delete("1.0", END)
    textbox3.insert(END, ounce)

# Create a Label widget with "Kg" as label
l1 = Label(window, height=1, width=20, text="Kg")
l1.grid(row=0, column=0) # The Label is placed in position 0, 0 in the window

# Create a button widget
# The kilo_grams() function is called when the button is pushed
b1 = Button(window, text="Convert", command=kilo_grams)
b1.grid(row=0, column=2)

userinput_value = StringVar() # Create a special StringVar object
userinput = Entry(window, textvariable=userinput_value) # Create an Entry box for users to enter the value
userinput.grid(row=0, column=1)

# Create 3 empty text boxes below
textbox = Text(window, height=1, width=15)
textbox.grid(row=1, column=0)

textbox2 = Text(window, height=1, width=15)
textbox2.grid(row=1, column=1)

textbox3 = Text(window, height=1, width=15,)
textbox3.grid(row=1, column=2)


# This keeps the windows open
window.mainloop()
