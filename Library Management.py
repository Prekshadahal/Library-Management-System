from datetime import datetime

#for reading the dictionary file
def bookDictionary():
    bookDict={}
    file= open("lib.txt","r")
    i=0
    for line in file:
        i=i+1
        line= line.replace("\n","")
        bookDict[i]=line.split(",")
    #print(bookDict)
    return(bookDict)
    file.close()
    
#for displaying list of books and its attributes
def display_book():
    print("--------------------------------------------------------------------------------")
    print(" Book ID","Book_Name","Author","Quantity","Price")
    print("--------------------------------------------------------------------------------")
    file=open("lib.txt","r")
    i=1
    for line in file:
        line= line.replace("\n","")
        line= line.split(",")
        ID= i
        name= line[0]
        author= line[1]
        quantity= line[2]
        price= line[3]
        i= i+1
        print( ID, name, author , quantity ,price)
    file.close()
         
#function for borrowing book
def borrowBook():
    display_book()
    bookID=int(input("Please enter the ID of book you want to lend: "))
    containsBook = checkQuantity(bookID)
    if containsBook== True:
        bookToBorrow(bookID)

#checking if book avilable or not
def checkQuantity(bookID):
    bookDict= bookDictionary()
    while bookID> len(bookDict):
        print("\n***************************************************************************")
        print("The book ID is invalid. Please enter a valid book ID")
        print("***************************************************************************\n")
        display_book()
        bookID=int(input("Enter the ID of book you want to lend: "))
    book= bookDict[bookID]
    bookQuantity = int(book[2])
    if (bookQuantity==0):
        print("\n***************************************************************************")
        print("Sorry! The book you want is not available.")
        print("***************************************************************************\n")
    else:
        print("\n***************************************************************************")
        print("The book you want is available to borrow.")
        print("***************************************************************************\n")
        
        return True

#to ask user their information for borrowing
def bookToBorrow(bookID):
    bookBorrowed=[]
    addBook = "y"
    bookDict= bookDictionary()
    bookBorrowed.append(bookID)
    dateTime= datetime.now()
    borrowedMoment= dateTime.strftime("%d-%m-%y %H:%M:%S")
    name= input("Enter your name: ")
    choosenBook=  bookDict[bookID]
    updateQuantity(bookID)
    while addBook=="y" or addBook=="Y":
        display_book()
        addBook= input("Do you have another book you want to lend (Y/N)? ")
        if addBook== "y" or addBook== "Y":
            display_book()
            bookID=int(input("Please enter the ID of book you want to lend: "))
            containsBook = checkQuantity(bookID)
            if containsBook== True:
                choosenBook= bookDict[bookID]
                booksBorrowed.append(bookID)
                updateQuantity(bookID)
                
    borrowReceipt(name, borrowedMoment, bookBorrowed)

    
#function to update books
def updateQuantity(bookID):
    bookDict= bookDictionary()
    file= open("lib.txt","w")
    for i in bookDict.keys():
        bookName=bookDict[i][0]
        author=bookDict[i][1]
        quantity=bookDict[i][2]
        price= bookDict[i][3]
        if i==bookID:
            updatedQuantity= str(int(quantity)-1)
            fileLine= (bookName+", "+author+",  "+updatedQuantity+", "+price+"\n")
            file.write(fileLine)
        else:
            fileLine= (bookName+", "+author+", "+quantity+", "+price+"\n")
            #print(fileLine)
            file.write(fileLine)
    file.close

#to print reciept of the books borrowed by customer
def borrowReceipt(name, borrowedMoment, booksBorrowed):
    book_dict= bookDictionary()
    print("\n***************************************************************************")
    print("Reciept")
    print("***************************************************************************\n")
    print("Name : ",name)
    print("List of Books Borrowed: ")
    i=0
    totalAmount=0
    for bookID in booksBorrowed:
        i=i+1
        book= book_dict[bookID]
        bookPrice = book[3].replace("$","")
        totalAmount =totalAmount+ int(bookPrice)
        
        print("                    ",book[0])
    print("Total items  : ",i)
    print("Total Price  : $"+str(totalAmount))
    print("***************************************************************************\n")
        

#to ask user their information for returning
def bookToReturn(bookID):
    bookReturned=[]
    addBook = "y"
    bookDict= bookDictionary()
    bookReturned.append(bookID)
    name= input("Enter your name: ")
    choosenBook=  bookDict[bookID]
    dateTime= datetime.now()
    returnedMoment= dateTime.strftime("%d-%m-%y %H:%M:%S")
    updateQuantityAfterReturn(bookID)
    while addBook=="y" or addBook=="Y":
        display_book()
        addBook= input("Do you have another book you want to return(Y/N)? ")
        if addBook== "y" or addBook== "Y":
            display_book()
            bookID = checkBookID(bookID)
            choosenBook= bookDict[bookID]
            bookReturned.append(bookID)
            updateQuantityAfterReturn(bookID)
    returnReceipt(name, returnedMoment, bookReturned)

#function to update books
def updateQuantityAfterReturn(bookID):
    bookDict= bookDictionary()
    file= open("lib.txt","w")
    for i in bookDict.keys():
        bookName=bookDict[i][0]
        author=bookDict[i][1]
        quantity=bookDict[i][2]
        price= bookDict[i][3]
        if i==bookID:
            updatedQuantity= str(int(quantity)+1)
            fileLine= (bookName+","+author+","+updatedQuantity+","+price+"\n")
            file.write(fileLine)
        else:
            fileLine= (bookName+","+author+","+quantity+","+price+"\n")
            #print(fileLine)
            file.write(fileLine)
    file.close
    
def returnReceipt(name, returnedMoment, booksReturned):
    book_dict= bookDictionary()
    print("\n***************************************************************************")
    print("Library Reciept")
    print("***************************************************************************\n")
    print("Name         : ",name)
    print("Date and Time: ",returnedMoment)
    print("List of Books Returned: ")
    totalAmount= 0
    for bookID in booksReturned:
        book= book_dict[bookID]
        bookPrice = book[3].replace("$","")
        totalAmount =totalAmount+ float(bookPrice)
        
        print("                    ",book[0])
        print("Total Price  : $"+str(totalAmount))
    print("***************************************************************************\n")


#function for returning book
def returnBook():
    print("\n***************************************************************************\n")
    print("You will now return the book ")
    print("\n***************************************************************************\n")
    display_book()
    bookID=int(input("Enter the ID of book you want to return:"))
    bookToReturn(bookID)
    
#function for taking the input from user
def start():
    exitApp= False

    while exitApp == False:
        print("Enter '1' to borrow a book")
        print("Enter '2' to return a book")
        print("Enter '3' to exit")
        ansOption=int(input("Please enter a value: "))
        if ansOption==1:
            borrowBook()

        elif ansOption==2:
            returnBook()

        elif ansOption==3:
            print("\n***************************************************************************")
            print("Thank You For Using Library Management System")
            print("***************************************************************************\n")
            exitApp= True
            
        #for invalid input
        else:
            print("\n***************************************************************************")
            print("INVALID INPUT!!!!")
            print("Please provide value as 1,2 or 3.")
            print("***************************************************************************\n")   
            
#introduction
print("***************************************************************************")
print("WELCOME TO OUR LIBRARY MANAGEMENT SYSTEM")
print("***************************************************************************\n")

start()

