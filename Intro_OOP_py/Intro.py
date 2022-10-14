"""
Python Assessment 3
Created by: Toton Liantoro
created on: 22 May 2022
last edited: 24 May 2022
"""

import linecache

# Calculate how many lines in the file
file = open("books.txt", "r")
for count, line in enumerate(file):
    pass
    numberLine = count + 1 #numberLine is number lines in the text file ("books.txt)
file.close()



# Create list line_number to get index line of the text
line_number = []
for i in range(1, numberLine + 1):
    line_number.append(i)


#Creating list to initialise the inventory
fileBookTitle = []
fileBookAuthor = []
fileBookISBN = []
fileBookCallNumber = []
fileBookStock = []
fileBookLoaned = []
Available = 0
fileBookAvailable = []

#Creating element to put in the list to iniate the inventory
for i in line_number:
    x = linecache.getline(r"books.txt", i).strip()
    bookTitles = x.split(';')[0]
    bookAuthor = x.split(';')[1]
    bookISBNs = x.split(';')[2]
    bookCallNumbers = x.split(';')[3]
    bookStocks = int(x.split(";")[4])
    bookLoaneds = int(x.split(';')[5])
    fileBookTitle.append(bookTitles)
    fileBookAuthor.append(bookAuthor)
    fileBookISBN.append(bookISBNs)
    fileBookCallNumber.append(bookCallNumbers)
    fileBookStock.append(bookStocks)
    fileBookLoaned.append(bookLoaneds)
for i in range(0, len(fileBookStock)):
    fileBookAvailable.append(fileBookStock[i] - fileBookLoaned[i])



#inventory in the list
inventTitle = fileBookTitle
inventAuthor = fileBookAuthor
inventISBNs = fileBookISBN
invetCallNumber = fileBookCallNumber
inventStock = fileBookStock
inventLoaned = fileBookLoaned
inventAvailable = fileBookAvailable


#Class Books to collect all elements in to display according the requirements
class Books:
    def __init__(self, Title, Author, ISBN, CallNumber, Stock, Loaned, Available):
        self.Title = Title
        self.Author = Author
        self.ISBN = ISBN
        self.CallNumber = CallNumber
        self.Stock = Stock
        self.Loaned = Loaned
        self.Available = Available

    def get_information(self):
        print(f'{self.Title :<70} {self.Author :<20} {self.ISBN :<17} {self.CallNumber :<15} {self.Stock :<10} {self.Loaned :<10} {self.Available}')



#Function display that will display all inventory
def display():
    print("\nDisplaying Westlands Books Inventory")
    print("")
    print(f'{"Name":<70} {"Author":<20} {"ISBN":<17} {"Call Number":<15} {"Stock":<10} {"Loaned":<10} {"Available":<10}')
    for i in range(0, len(fileBookTitle)):
        books = [Books(fileBookTitle[i], fileBookAuthor[i], fileBookISBN[i], fileBookCallNumber[i], fileBookStock[i],
                       fileBookLoaned[i], fileBookAvailable[i])]
        for book in books:
            book.get_information()


# addingBook() --> Function to add book(s) in the inventory
def addingBook():
    Title = input("Title> ")
    Author = input("Author> ")
    ISBN = input("ISBN> ")
    CallNumber = input("Call Number>")
    Stock = int (input("Stock> "))
    Loaned = int (input("Loaned> "))

    inventTitle.append(Title)
    inventAuthor.append(Author)
    inventISBNs.append(ISBN)
    invetCallNumber.append(CallNumber)
    inventStock.append(Stock)
    inventLoaned.append(Loaned)
    for i in range(0, len(inventTitle)):
        inventAvailable.append(inventStock[i] - inventLoaned[i])
        inventAvailable[i] = inventStock[i] - inventLoaned[i]

    print("The book has been add in the inventory")



# removeBook() --> function to remove books from inventory
def removeBook():
    print("Removing a Book")
    Author = input("Author>")
    CallNumber = input("Call Number>")
    for i in range (0,len(fileBookStock)):
        if Author == inventAuthor[i]:
            if CallNumber == invetCallNumber[i]:
                del inventTitle[i]
                del inventAuthor[i]
                del inventISBNs[i]
                del invetCallNumber[i]
                del inventStock[i]
                del inventLoaned[i]
                del inventAvailable[i]
                print("The book in inventory has been deleted ")
            else:
                print("The book doesn't exist in the inventory")


# exportInventory() --> Function to save all changes of inventory to database ("books.txt")
def exportInventory():
    print ("\nExporting Inventory")
    with open ("books.txt",'w') as file:
        for i in range(0,len(fileBookAuthor)):
            file.write(inventTitle[i])
            file.write(";")
            file.write(inventAuthor[i])
            file.write(";")
            file.write(inventISBNs[i])
            file.write(";")
            file.write(invetCallNumber[i])
            file.write(";")
            strinventStock = [str(x) for x in inventStock]
            file.write(strinventStock[i])
            file.write(";")
            strinventLoaned = [str(x) for x in inventLoaned]
            file.write(strinventLoaned[i])
            file.write(";")
            strinventAvailable = [str(x) for x in inventAvailable]
            file.write(strinventAvailable[i])
            file.write(";\n")
        file.close()
    print("\nExport Complete")


#start() --> function to intialise the program
def start ():
    print ("\nWestlands Books Inventory Management Subsystem")
    print ("1. Display Inventory")
    print ("2. Add a Book")
    print ("3. Remove Book")
    print ("4. Export Inventory")
    print ("5. Quit IMS")
    choice = int (input ("Select an option from the menu> "))
    if choice == 1:
        display()
        start()
    if choice == 2:
        addingBook()
        start()
    if choice == 3:
        removeBook()
        start()
    if choice == 4:
        exportInventory()
        start()
    print("")
    if choice == 5:
        print("Bye...")
        quit()
    else:
        print("Your choice is not available in this program please choose another choice option")
        print ("")
        start()

if __name__ == '__main__':
    start()

