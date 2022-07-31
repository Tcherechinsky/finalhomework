from tkinter import *
from tkinter import ttk
#Part 1. Setting everything Up#
#Creating the main loop/window
pizza = Tk()
#Setting the size of the windows
pizza.geometry("800x800")
pizza.title("Pizza Order")
#Adding some PNG's to display Images on the window
canvas = Canvas(
    pizza,
    width = 120,
    height = 120,
    )
canvas.grid(row=1, column=3)
img = PhotoImage(file=r'C:\finalhomework\pizza-slice.png')
canvas.create_image(
    10,
    10,
    anchor=NW,
    image=img
    )



#Adding an Icon to the window, to  the main window
pizza.iconbitmap(r'C:\finalhomework\pizza.ico')

#Prompting to input the name, then formatting the label of the prompt
name_label = Label(pizza, text= "Enter your Name: ")
name_label.grid(row=0, column=0)
#Allows the user to enter their name
#Format to create the size of the data entry box
name_entry = Entry(pizza, width=30)
name_entry.grid(row=0, column=1)




#Prompting to input their address, then formatting the label of the prompt
address_label = Label(pizza, text= "Enter your Address: ")
address_label.grid(row=1, column=0)
#Allows the user to enter their address
#Format to create the size of the data entry box
address_entry = Entry(pizza, width=30)
address_entry.grid(row=1, column=1)

#Prompting to input their phone number, then formatting the label of the prompt
phone_label = Label(pizza, text= "Enter your phone number, Ex. (5555555555) - : ")
phone_label.grid(row=2, column=0)
#Allows the user to enter their name
#Format to create the size of the data entry box
phone_entry = Entry(pizza, width=30)
phone_entry.grid(row=2, column=1)


#Showing the different types of pre made pizzas

my_pizza_list = ["Pepperoni", "Jalapeno", "Sausage", "Bacon", "Four Cheese"]

topping_label = Label(pizza, text= "Choose which Toppings you would like: ")
topping_label.grid(row=4, column=1)
#Creating a list for different toppings that the User can select
pizza_list = Listbox(pizza, selectmode=MULTIPLE, bg="blue", fg="white")
pizza_list.grid(row=5, column=1)

for item in my_pizza_list:
    pizza_list.insert(0, item)
#Defining a function that will take all of the selected toppings, and display them to the user
def add_pizza():
    result = ""
    for item in pizza_list.curselection():
        result = result + str(pizza_list.get(item)) + "\n"

        add_lbl.config(text="Your Selection: " + "\n" + result)


add_lbl = Label(pizza, text="")
add_lbl.grid(row=10, column=1)

#Part 2. Adding the "Add to cart" Button#
#Adding the button to add pizza to your cart
add_button = Button(pizza, text="Add the selected toppings to your pizza", command = add_pizza)
add_button.grid(row=5, column=0)
#Adding the button to remove pizzas from your cart
del_button = Button(pizza, text="Remove your selection")
del_button.grid(row=6, column= 0)


#Creating a function that opens a new window to display the user's inputs when they are finished,
#And to confirm that your order is correct


def openWindow():

    #Validating Data Entry
    if len(name_entry.get()) in range(1, 25):
        if len (phone_entry.get()) == 10:
            if len(address_entry.get()) in range(3, 25):
                windowNew = Toplevel(pizza)
                windowNew.title("Confirmation")
                windowNew.geometry("400x400")
                # adding an Icon to the New Window
                windowNew.iconbitmap(r'C:\finalhomework\shopping_cart.ico')
                # Adding an image to the New window for checkout
                canvas = Canvas(
                    windowNew,
                    width=220,
                    height=220,
                )
                canvas.grid(row=20, column=2)
                img = PhotoImage(file=r'C:\finalhomework\delivery.png')
                canvas.create_image(
                    10,
                    10,
                    anchor=NW,
                    image=img
                )

                #Adding a label to confirm
                Label(windowNew, text ="Does everything look right?").grid(row =2, column = 1)
                # this part is to display the persons name
                customer_info = name_entry.get()
                new_label = Label(windowNew, text="Delivering to: " + customer_info)
                new_label.grid(row=7, column=2)
                # this part is to display the callback number
                customer_info2 = phone_entry.get()
                new_label2 = Label(windowNew, text="Contact Number: " + customer_info2)
                new_label2.grid(row=8, column=2)
                # this part is to display address
                customer_info3 = address_entry.get()
                new_label3 = Label(windowNew, text="Delivery Address: " + customer_info3)
                new_label3.grid(row=9, column=2)
                # adding a button to close the program
                quitButton = ttk.Button(windowNew, text="Click here to send your order on its way!", command=exit)
                quitButton.grid(row=12, column=2)
                quitButton = ttk.Button(windowNew, text="Information doesn't look right? Click here!", command=exitConfirmation)
                quitButton.grid(row=13, column=2)
                windowNew.mainloop()
                pizza.mainloop()
            else:
                phoneLabelEntry = Label(pizza, text="Make sure to enter your phone number!")
                phoneLabelEntry.grid(row=0, column=3)
        else:
                phoneLabelEntry = Label(pizza, text="Make sure to enter your address")
                phoneLabelEntry.grid(row=0, column=3)
    else:
        phoneLabelEntry = Label(pizza, text = "Make sure to enter your name!")
        phoneLabelEntry.grid( row = 0, column = 3)

#Definiing a function to close the program
def exit():
    pizza.quit()
def exitConfirmation():
    windowNew.quit()

#Part 3. Opening a new window, for customer confirmation#
# Opening up a new window to for the user to confirm the information
finalizeButton = ttk.Button(pizza, text="Click here to Finalize your Order", command=openWindow)
finalizeButton.grid(row=11, column = 1)




pizza.mainloop()



##Credits for Images
#flaticon.com/free-sticker/pizza-slice_4910034# - Image of Pizza in top right corner
#https://iconarchive.com/show/swarm-icons-by-sonya/Pizza-icon.html Pizza Icon
#Shopping Cart Icon https://findicons.com/icon/download/50149/shopping_cart/128/ico
#https://www.pngitem.com/middle/ihRwTJR_pizza-delivery-car-png-transparent-png/ Delivery truck image
