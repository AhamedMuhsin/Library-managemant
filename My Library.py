# make class to make library
class Library:

#     add a contruter to construct the library
    def __init__(self, list , name):
        self.librarylist = list
        self.name = name
        self.lenddict = {}

# add display book function to display the book 
    def displaybook(self):
        print(f"We have following book in our library : {self.name}")
        for book in self.librarylist:
                print(book)

# make lend book function to lend the book 
    def lendboook(self, user , book):
        if book not in self.lenddict.keys():
            self.lenddict.update({book:user})
            print("Lender-book database as been updated .\nYou can now take the book")
        else:
            print(f"Book is already taken by {self.lenddict[book]}")

#  make add book function to add book
    def addbook(self, book):
        self.librarylist.append(book)
        print("Book has been added to the library list")

# make return book function to retrun book
    def returnbook(self, book):
        self.lenddict.pop(book)
        print("You were successfully return the book")

# add main function to run this program
if __name__ == '__main__':
    Ahamed = Library(['Harry Potter', 'Python basic', 'Quran', 'what is programing'],
                     "Ahamed Muhsin")

    while(True):
        print(f"Welcome to the {Ahamed.name} library .\nEnter your choice to continue : ")
        print("1.Display Book")
        print("2.Lend Book")
        print("3.Add Book")
        print("4.Return Book")
        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("Please Enter a valid input")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            Ahamed.displaybook()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to Lend : ")
            user = input("Enter your Name :")
            Ahamed.lendboook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to Add : ")
            Ahamed.addbook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to Return : ")
            Ahamed.returnbook(book)

        else:
            print("Not a valid input")

        print("Press q for quit and c for continue")
        user_choice2 = " "
        while(user_choice2!= "c" and user_choice2!= "q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()
            elif user_choice2 == "c":
                continue
