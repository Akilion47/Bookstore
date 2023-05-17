import mysql.connector
db = mysql.connector.connect(host="localhost",user="root",passwd="***********",database="BookStore")
mc = db.cursor()

class Books:
    def Addbook(self):
        print()
        a = input("Enter the Title of Book:")
        mc.execute("SELECT * FROM BookData ORDER BY Bookid DESC")
        res = mc.fetchall()
        flag = 0
        for y in res:
            if (a == y[1]):
                flag = 1
                break
        if (flag == 1):
            print("Record already present.")
            mc.execute("UPDATE BookData SET Copies=Copies+1 WHERE Title = '"+ str(a) +"'")
            print("Number of copies increased.")
            print("Record saved.")

        else:
            bid=0
            if(len(res)==0):
                bid=1001
            else:
                bid=int(res[0][0])+1
            b = input("Enter the Name of Author of Book:")
            e = input("Enter the Name of A Publisher of Book:")
            c = int(input("Enter the Number of pages in Book:"))
            d = int(input("Enter the Price of Book:"))
            f = input("Enter the subject of Book:")
            g = input("Enter the Number of copies:")
            mc.execute("INSERT INTO BookData VALUES(" + str(bid) + ",'" + str(a)
                      + "','" + str(b) + "'," + str(c) + "," + str(d) + "," + str(g)
                      + ",'" + str(e) + "','" + str(f) + "'" + ")")
            db.commit()

    def Display(self):
        print()
        print()
        mc.execute("SELECT * FROM BookData")
        res = mc.fetchall()
        print("=========================================================================================================")
        print("Number of records are:", len(res))
        print("=========================================================================================================")
        for x in res:
            print("Book ID:",x[0])
            print("Title:", x[1])
            print("Author Name:", x[2])
            print("No. of Pages:", x[3])
            print("Book Publisher:", x[6])
            print("No. of Copies:", x[5])
            print("Book Price:", x[4])
            print("Subject:", x[7])
            print("-----------------------------------------------------------------------------------------------------")
        print("=========================================================================================================")

    def Search(self):
        print()
        print()
        print("Press 1 to Search Book by Book Id.")
        print("Press 2 to Search Book by Title.")
        print("Press 3 to Search Book by Author.")
        print("Press 4 to Search Book by Publisher.")
        print("Press 5 to Search Book by Subject.")
        print("Press 0 to Return to Main Menu.")
        x = int(input("Press any Key:"))
        mc.execute("SELECT * FROM BookData")
        res = mc.fetchall()
        if(x == 1):
            i=int(input("Enter Book's ID:"))
            mc.execute("SELECT * FROM BookData")
            res = mc.fetchall()
            for y in res:
                if(i == int(y[0])):
                    print("Book ID:", y[0])
                    print("Title:", y[1])
                    print("Author Name:", y[2])
                    print("No. of Pages:", y[3])
                    print("Book Publisher:", y[6])
                    print("No. of Copies:", y[5])
                    print("Book Price:", y[4])
                    print("Subject:", y[7])
                    break
                else:
                        print("Record Unavailable.")

        elif(x == 2):
            i = input("Book's TItle:")
            mc.execute("SELECT * FROM BookData")
            res = mc.fetchall()
            for y in res:
                if (i == y[1]):
                    print("Book ID:", y[0])
                    print("Title:", y[1])
                    print("Author Name:", y[2])
                    print("No. of Pages:", y[3])
                    print("Book Publisher:", y[6])
                    print("No. of Copies:", y[5])
                    print("Book Price:", y[4])
                    print("Subject:", y[7])
                    break
                else:
                    print("Record Unavailable.")

        elif (x == 3):
            i = input("Name of the Author:")
            mc.execute("SELECT * FROM BookData")
            res = mc.fetchall()
            for y in res:
                if (i == y[2]):
                    print("Book ID:", y[0])
                    print("Title:", y[1])
                    print("Author Name:", y[2])
                    print("No. of Pages:", y[3])
                    print("Book Publisher:", y[6])
                    print("No. of Copies:", y[5])
                    print("Book Price:", y[4])
                    print("Subject:", y[7])
                    break
                else:
                    print("Record Unavailable.")



        elif (x == 4):
            i = input("Book's Publisher:")

            mc.execute("SELECT * FROM BookData")
            res = mc.fetchall()
            for y in res:
                if (i == y[6]):
                    print("Book ID:", y[0])
                    print("Title:", y[1])
                    print("Author Name:", y[2])
                    print("No. of Pages:", y[3])
                    print("Book Publisher:", y[6])
                    print("No. of Copies:", y[5])
                    print("Book Price:", y[4])
                    print("Subject:", y[7])
                    break
                else:
                    print("Record Unavailable.")
        elif (x == 5):
            i = input("Book's Subject:")
            mc.execute("SELECT * FROM BookData")
            res = mc.fetchall()
            for y in res:
                if (i == y[7]):
                    print("Book ID:", y[0])
                    print("Title:", y[1])
                    print("Author Name:", y[2])
                    print("No. of Pages:", y[3])
                    print("Book Publisher:", y[6])
                    print("No. of Copies:", y[5])
                    print("Book Price:", y[4])
                    print("Subject:", y[7])
                    print("=================================================================================================")
                else:
                    print("Record Unavailable.")
        elif (x == 0):

            b = int(input("Press any key: "))

        else:
             print("Wrong Input!!")
             print()
             print()
             print("Press 1 to Search by Book Id.")
             print("Press 2 to Search by Title.")
             print("Press 3 to Search by Author.")
             print("Press 4 to Search by Publisher.")
             print("Press 5 to Subject")
             print("Press 0 to Return to Main Menu.")

             x = int(input("Press any Key:"))

    def Delete(self):
        print()
        print()
        bid= int(input("Enter Book id:"))
        mc.execute("SELECT * FROM BookData")
        res = mc.fetchall()
        print("Book details:-")
        bookfound = 0
        for y in res:
            if(bid == int(y[0])):
                print("Book ID:", y[0])
                print("Title:", y[1])
                print("Author Name:", y[2])
                print("No. of Pages:", y[3])
                print("Book Publisher:", y[6])
                print("No. of Copies:", y[5])
                print("Book Price:", y[4])
                print("Subject:", y[7])
                bookfound = 1
                break
        if(bookfound==1):
            yn = input("Want to Purchase or not(yes/no)")
            if (yn == "yes"):
                mc.execute("DELETE FROM BookData WHERE Bookid = '" + str(bid) + "'")
                db.commit()
            else:
                print()
                print("Back to Main Menu.")
                print()

        else:
           print("Record is not present.")
           bid = int(input("Enter Book id:"))

    def purchase(self):
        bid=int(input("Enter book id(Starting from 100000)."))
        mc.execute("SELECT * FROM BookData")
        res = mc.fetchall()
        print("Book details:-")
        bookfound=0
        for y in res:
            if(bid == int(y[0])):
                print("Book ID:", y[0])
                print("Title:", y[1])
                print("Author Name:", y[2])
                print("No. of Pages:", y[3])
                print("Book Publisher:", y[6])
                print("No. of Copies:", y[5])
                print("Book Price:", y[4])
                print("Subject:", y[7])
                bookfound = 1
                break
        if(bookfound==1):
            yn = input("Want to Purchase or not(yes/no)")
            if (yn == "yes"):
                mc.execute("UPDATE BookData SET Copies=Copies-1 WHERE Bookid = '" + str(bid) + "'")
                db.commit()
            else:
                print()
                print("Back to Main Menu.")
                print()
        else:
            print("Record is not present.")
            bid = int(input("Enter book id(Starting from 100000)."))

    def out_of_stock(self):
        print()
        print()
        mc.execute("select * from BookData where Copies <= 10")
        for x in mc:
            print("Book ID:", x[0])
            print("Title:", x[1])
            print("Author Name:", x[2])
            print("No. of Pages:", x[3])
            print("Book Publisher:", x[6])
            print("No. of Copies:", x[5])
            print("Book Price:", x[4])
            print("Subject:", x[7])
            print("-----------------------------------------------------------------------------------------------------")

    print("______________________________________________________________________________________________________________________")

    def sell(self):
        a = input("Enter the Title of Book:")
        b = input("Enter the Name of Author of Book:")
        e = input("Enter the Name of A Publisher of Book:")
        c = int(input("Enter the Number of pages in Book:"))
        d = int(input("Enter the Price of Book:"))
        f = input("Enter the subject of Book:")
        g = input("Enter the Number of copies:")
        mc.execute("SELECT * FROM BookData ORDER BY Bookid DESC")
        res = mc.fetchall()
        bid = 0
        if (len(res) == 0):
            bid = 1001
        else:
            bid = int(res[0][0]) + 1
        mc.execute("INSERT INTO BookData VALUES(" + str(bid) + ",'" + str(a) + "','" + str(b) + "'," + str(c) + "," + str(d) + "," + str(g) + ",'" + str(e) + "','" + str(f) + "'" + ")")
        db.commit()
        print("Data has been stored. ")
        print("Please wait for 7 days you will receive an message after the verification process.")
        print()
        print()

c = Books()
option=1
while(option!=0):
    print("Press 1 to Add New Book")
    print("Press 2 to Display all")
    print("Press 3 to Search Book")
    print("Press 4 to Delete book")
    print("Press 5 to Purchase Book")
    print("Press 6 to sell Book")
    print("Press 7 to Out of stock")
    print("Press 0 to Quit")

    b = int(input("Press any key: "))

    if(b == 1):
        c.Addbook()
    elif(b == 2):
        c.Display()
    elif (b == 3):
        c.Search()
    elif (b == 4):
        c.Delete()
    elif (b == 5):
        c.purchase()
    elif (b == 6):
        c.sell()
    elif (b == 7):
        c.out_of_stock()
    elif(b==0):
        option=0
    else:
        print("Invalid entry")
