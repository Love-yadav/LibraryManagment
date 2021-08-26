#create a library class
#display book
# lend book - who owns the book if book is not present
# add book
#return book

# harry library=Library(listofbooks ,libraryname)
# dirctionary=(books-nameoftheowner)

# create main function and run an infinte while loop asking
# user for their input

class Library:

    def __init__(self,list,name):
        self.listofbooks=list
        self.name=name
        self.lendDict={}

    def DisplayBook(self):
        for book in self.listofbooks:
            print(book)

    def lendbook(self,user,book):
        if  book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            # self.listofbooks.remove(book)
            print("Dictionary Database is updated successfully")
        else:
            print(f"Book is already being used {self.lendDict[book]}")

    def addbook(self,book):
        self.listofbooks.append(book)
        print("BOok is added successfully")

    def returnbook(self,book):
        self.lendDict.pop(book)
        


if __name__ == '__main__':
    love=Library(['hindi',"english","mathes","chemistry","social"],"Nobal")

    while(True):
        print(f"Welcome to the {love.name} library")
        print("Choose the option from below")
        print("1.DisplayBook")
        print("2.lendBook")
        print("3.addbook")
        print("4.return book")
        option=int(input("enter  your choice:"))


        if option == 1:
            love.DisplayBook()
        
        elif option == 2:
            user=input("Enter your name")
            book=input("enter the book name|which you want to lend")
            love.lendbook(user,book)

        elif option== 3:
            book=input("enter the bookname you want to add")
            love.addbook(book)    

        elif option == 4:
            book=input("Enter the book name you want to return")
            love.returnbook(book)
        
        else:
            print("please Choose the valid options form above")

        print("press q to quit and press c to continue")
        option1=''
        while(option1!='c' and option1!='q'):
         option1=input()
         if option1 == "q":
             exit()
         elif option1 =="c":
            continue
         