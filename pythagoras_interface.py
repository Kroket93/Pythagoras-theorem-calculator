from tkinter import *
import math

running = True

welcome_message_1 = "Pythagoras' theorem!"
welcome_message_2 = "Calculate the hypotenuse of a right-angled triangle!"
welcome_message_3 = "A right-angled triangle is a triangle in which one angle is 90 degrees"
welcome_message_4 = "The two sides which make up the 90 degree angle are called the 'legs'"
input_message_a = "Enter the length of the first leg: "
input_message_b = "Enter the length of the second leg: "
empty_string = " "
hypotenuse_message = "The length of the hypotenuse is: "
credits_message = "Made by Luuk van Wolferen"


### main
window = Tk()
window.title("Pythagoras' Theorem Calculator")
c = StringVar()
c.set("0")

errormessage = StringVar()
errormessage.set(" ")

#labels
Label(window, text=welcome_message_1, fg="black", font="none 12 bold").grid(row=1, column=0, sticky=W)
Label(window, text=welcome_message_2, fg="black", font="none 12 bold").grid(row=2, column=0, sticky=W)
Label(window, text=welcome_message_3, fg="black", font="none 12 bold").grid(row=3, column=0, sticky=W)
Label(window, text=welcome_message_4, fg="black", font="none 12 bold").grid(row=4, column=0, sticky=W)

Label(window, text=empty_string, fg="black", font="none 12 bold").grid(row=5, column=0, sticky=W)

Label(window, text=input_message_a, fg="black", font="none 12 bold").grid(row=6, column=0) #
Label(window, text=input_message_b, fg="black", font="none 12 bold").grid(row=8, column=0) #

Label(window, text=empty_string, fg="black", font="none 12 bold").grid(row=10, column=0, sticky=W)

Label(window, text=hypotenuse_message, fg="black", font="none 12 bold").grid(row=11, column=0) #
Label(window, textvariable=c, fg="black", font="none 12 bold").grid(row=12, column=0) #

errorlabel = Label(window, textvariable=errormessage, fg="black", font="none 12 bold").grid(row=13, column=0, sticky=W)

Label(window, text=empty_string, fg="black", font="none 12 bold").grid(row=14, column=0, sticky=W)
Label(window, text=empty_string, fg="black", font="none 12 bold").grid(row=15, column=0, sticky=W)
Label(window, text=credits_message, fg="black", font="none 12 bold").grid(row=16, column=0, sticky=W)
#text entry
textentry_a = Entry(window, width=20, bg="grey")
textentry_a.grid(row=7, column=0)

textentry_b = Entry(window, width=20, bg="grey")
textentry_b.grid(row=9, column=0)

#result


#run main loop

while running:
	

	window.update_idletasks()
	window.update()

	if len(textentry_a.get()) > 0 and len(textentry_b.get()) > 0:
		try:
			val_a = float(textentry_a.get())
			val_b = float(textentry_b.get())

			errormessage.set(" ")
			hypotenuse = math.sqrt(float(textentry_a.get())**2 + float(textentry_b.get())**2)	
			c.set(str(hypotenuse))
		except ValueError:
			errormessage.set("Please enter numbers only!")
#window.mainloop()