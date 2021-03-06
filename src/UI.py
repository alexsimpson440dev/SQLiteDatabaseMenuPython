__author__ = 'Alex'
from src.CreateDatabaseTable import Create
from src.AddTableRow import AddRow
from src.UpdateTableRow import UpdateRow
from src.DeleteTableRow import DeleteRow
from src.DisplayTableRows import DisplayRows
class UI:
    def __init__(self):
        pass

    def Interface(self):
        # gets instance for classes
        database = Create
        add = AddRow
        update = UpdateRow
        delete = DeleteRow
        display = DisplayRows

        # variable to get file connection
        file = database.Create_Database(database)
        connection = database.Connect(database, file)
        cursor = database.get_cursor(database, connection)
        userOption = 7

        # loops until user enters in a 0
        while userOption != 0:
            # calls option method
            UI.Options(UI)
            userOption = int(input("Which option would you like to select? "))

            if userOption == 1:
                print("-----OPTION 1-------------------------------------------\n")

                # gets connection to database
                database.Create_Table(database, cursor)

            if userOption == 2:
                print("-----OPTION 2-------------------------------------------\n")

                #variables to add to Table row
                id = int(input("Enter in a RowID: "))
                productID = int(input("Enter in the ProductID: "))
                productName = input("Enter in the Product Name: ")
                quantity = int(input("Enter in the Quantity: "))
                price = float(input("Enter in the Price: "))
                description = str(input("Enter in a Product Description: "))

                # sent information to class to add
                add.row(add, cursor, connection, id, productID, productName, quantity, price, description)

            if userOption == 3:
                print("-----OPTION 3-------------------------------------------\n")

                # variables and parameters to update a row in the Products table
                columnUpdate = input("Which Table Column do you wish to update? ")
                newInput = input("What would you like to change " + columnUpdate + " to? ")
                viaRowID = input("Which row would you like to update via RowID? ")

                # sends information to class to update
                update.row(update, cursor, connection, columnUpdate, newInput, viaRowID)

            if userOption == 4:
                print("-----OPTION 4-------------------------------------------\n")

                # variables and parameters to update a row in the Products table
                deleteRow = input("Enter RowID of row you would like to delete: ")

                # sends information to class to update
                delete.row(delete, cursor, connection, deleteRow)

            if userOption == 5:
                print("-----OPTION 5-------------------------------------------\n")
                display.allRows(display, connection)

            if userOption == 6:
                print("-----OPTION 6-------------------------------------------\n")

                selectedID = input("Enter in a RowID to view: ")
                display.singleRow(display, connection, selectedID)

        # closes connection to database
        connection.close()
        print()
        print("Connection to " + file + " closed!")





    # method that displays
    def Options(self):
        option1 = "1): Create a new Database and Database Table"
        option2 = "2): Add a row of data to Table"
        option3 = "3): Update a row of data"
        option4 = "4): Delete a row of data"
        option5 = "5): Display all rows"
        option6 = "6): Display a single row of data"
        option7 = "0): EXIT PROGRAM"

        print("OPTIONS:\n"
              ,option1+"\n"
              ,option2+"\n"
              ,option3+"\n"
              ,option4+"\n"
              ,option5+"\n"
              ,option6+"\n"
              ,option7+"\n")
