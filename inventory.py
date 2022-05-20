import sqlite3
import tkinter
from tkinter import Text



class Inventory:
    def __init__(self):
    
        self.window = tkinter.Tk()
        self.window.title("Your Company")
##        self.window.geometry('600x500')


        self.idNumberLabel = tkinter.Label(self.window, text="ID Number")
        self.idNumberLabel.grid(row = 1, column = 0)
        self.idNumberEntry = tkinter.Entry(self.window)
        self.idNumberEntry.grid(row = 1, column = 1)

        self.nameLabel = tkinter.Label(self.window, text="Name")
        self.nameLabel.grid(row = 2, column = 0)
        self.nameEntry = tkinter.Entry(self.window)
        self.nameEntry.grid(row = 2, column = 1)

        self.categoryLabel = tkinter.Label(self.window, text="Category")
        self.categoryLabel.grid(row = 3, column = 0)
        self.categoryEntry = tkinter.Entry(self.window)
        self.categoryEntry.grid(row = 3, column = 1)

        self.priceLabel = tkinter.Label(self.window, text="Price")
        self.priceLabel.grid(row = 4, column = 0)
        self.priceEntry = tkinter.Entry(self.window)
        self.priceEntry.grid(row = 4, column = 1)

        self.onHandLabel = tkinter.Label(self.window, text="On Hand")
        self.onHandLabel.grid(row = 5, column = 0)
        self.onHandEntry = tkinter.Entry(self.window)
        self.onHandEntry.grid(row = 5, column = 1)

        self.productLabel = tkinter.Label(self.window, text="Product Name")
        self.productLabel.grid(row = 3, column = 3)
        self.productEntry = tkinter.Entry(self.window)
        self.productEntry.grid(row = 3, column = 4)

        self.displayRecord = Text(self.window)
        self.displayRecord.grid(row = 1, column = 2, rowspan = 5)
        self.displayRecord.config(state='disabled')


        def ClearText():
            self.idNumberEntry.delete(0, tkinter.END)
            self.nameEntry.delete(0, tkinter.END)
            self.categoryEntry.delete(0, tkinter.END)
            self.priceEntry.delete(0, tkinter.END)
            self.onHandEntry.delete(0, tkinter.END)
            
        def Clear():
            self.productEntry.delete(0, tkinter.END)
            self.displayRecord.config(state='normal')
            self.displayRecord.delete(1.0, tkinter.END)
            self.displayRecord.config(state='disabled')

        def Save():
            conn = sqlite3.connect('products.db')
            c = conn.cursor()
            sql = "INSERT INTO PRODUCTS VALUES (?,?,?,?,?)"
            ID = self.idNumberEntry.get()
            PRODCATEGORY = self.categoryEntry.get()
            PRODNAME = self.nameEntry.get()
            PRICE = self.priceEntry.get()
            ONHAND = self.onHandEntry.get()
            c.execute(sql, (ID, PRODCATEGORY, PRODNAME, PRICE, ONHAND))
            conn.commit()
            conn.close()

        def Display():
            conn = sqlite3.connect('products.db')
            c = conn.cursor()
            PRODNAME = self.productEntry.get()
            sql = "SELECT ID, PRODCATEGORY, PRODNAME, PRICE, ONHAND FROM products WHERE PRODNAME = ?"
            c.execute(sql, (PRODNAME,))
            search = c.fetchall()
            total = "Current Inventory: \n" + "ID: " + str(search[0][0]) + ", " + "Category: " + str(search[0][1]) + ", "+ "Product: "+ str(search[0][2]) + ", " + "Price: " + str(search[0][3]) + ", " + "On Hand: " + str(search[0][4])+ "\n"
            conn.close()
            self.displayRecord.config(state='normal')
            self.displayRecord.insert(1.0, total)
            self.displayRecord.config(state='disabled')

                
        saveButton = tkinter.Button(self.window, text="Save", command=Save)
        saveButton.grid(row = 6, column = 0)

        clearButton = tkinter.Button(self.window, text="Clear Text", command=ClearText)
        clearButton.grid(row = 6, column = 1)
 
        displayButton = tkinter.Button(self.window, text="Display Record", command=Display)
        displayButton.grid(row = 4, column = 4)

        clearTextButton = tkinter.Button(self.window, text="Clear Text", command=Clear)
        clearTextButton.grid(row = 4, column = 5)






Inventory()







