# This is a program simulating an inventory.
# It will read from the text file inventory.txt 
# and perform the following methods and functions on the data, 
# to prepare for presentation.

#---------------------------------------------- Additional comment ---------------------------------------
# This program requires tabulate to work properly.
# Install tabulate: pip install tabulate
# Find more instructions on how to install tabulate in Python: https://pypi.org/project/tabulate/
#---------------------------------------------------------------------------------------------------------

from tabulate import tabulate

#========The beginning of the class==========
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        '''
        Initialises the following attributes:
        country: The country where the shoe is made
        code: Unique code for the shoe
        product: Name of the product
        cost: Cost of the shoe
        quantity: The number of shoes in stock
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        '''
        Returns the cost of the shoe.
        '''
        return self.cost

    def get_quantity(self):        
        '''
        Returns the quantity of the shoes.
        '''
        return self.quantity

    def __str__(self):
        pass
        '''
        Returns a string representation of the Shoe object.
        '''
        return f"Country: {self.country},  Code: {self.code},  Product: {self.product},  Cost: {self.cost},  Quantity: {self.quantity}"


#=============Shoe list===========

# List to store a list of Shoe objects.
shoe_list = []


#==========Functions outside the class==============
def read_shoes_data():
    '''
    Reads data from the "inventory.txt" file and creates a Shoe object with each line of data.
    Appends each Shoe object to the shoe_list.
    Uses try-except for error handling and skips the first line (header) of the file.
    '''
    try:
        with open("inventory.txt", 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if i == 0:
                    header = line.strip().split(",")
                    continue
                fields = line.strip().split(",")
                # If the number of fields in the header and the current line do not match, an exception is raised 
                # with an error message indicating the line number.
                if len(header) != len(fields):
                    raise Exception("Invalid format in line {}".format(i + 1))
                # The "zip" function is used to create a dictionary mapping the header fields 
                # to their corresponding values in the current line.
                data = dict(zip(header, fields))
                # The "get" method is used to extract the values for "Country", "Code", "Product", 
                # "Cost", and "Quantity" from the dictionary.
                country = data.get("Country")
                code = data.get("Code")
                product = data.get("Product")
                cost = float(data.get("Cost", 0))
                quantity = int(data.get("Quantity", 0))
                # A Shoe object is created using the extracted values.
                shoe = Shoe(country, code, product, cost, quantity)
                # The Shoe object is added to the "shoe_list".
                shoe_list.append(shoe)

            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
            print("\nData has been added.")
    # If an exception is raised while reading the file, it is caught and a message indicating the error is printed.
    except Exception as e:
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print(f"\nError reading the file: {e}")


def capture_shoes():
    '''
    Captures data about a shoe from user input, creates a Shoe object with this data
    and appends the object to the shoe_list.
    Prompts the user if they would like to add the data to the "inventory.txt" file.
    '''
    country = input("Enter the country of manufacture: ")
    code = input("Enter the code: ")
    product = input("Enter the product: ").title()

    inpt = False
    while inpt == False:
        try:
            cost = float(input("Enter the cost: "))
            inpt = True
        except ValueError:
            print("Incorrect input. Please use numbers.")
    inpt = False
    while inpt == False:
        try:
            quantity = int(input("Enter the quantity: "))
            inpt = True
        except ValueError:
            print("Incorrect input. Please use numbers.")

    # Create a Shoe object with the input data.
    shoe = Shoe(country, code, product, cost, quantity)
    # Append the Shoe object to the shoe_list.
    shoe_list.append(shoe)

    inpt = False
    # Loop to prompt the user if they would like to add the data to the "inventory.txt" file.
    while inpt == False:
        add_txt = input("Would you like to add this product details to 'inventory.txt' file? y/n: ").lower()
        if add_txt == "y":
            # Open the "inventory.txt" file in append mode and write the data to the file.
            with open("inventory.txt", "a") as f:
                f.write(f"\n{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}")
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
            print("\nProduct has been added.")
            inpt = True
        elif add_txt == "n":
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
            print("\nNo product details had been added to a txt file.")
            inpt = True
        else:
            print("Incorrect input. Please enter y or n.")


def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    # Check if there are any shoes in the shoe_list.
    if len(shoe_list) <= 0:
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print("\nNo products found.")
    else:
        # If there are shoes in the shoe_list, try to print them in a tabular format.
        try:
            # Compile a list of all the shoes, with their details as a nested list.
            data = [[shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity] for shoe in shoe_list]
            # Add headers to the data.
            headers = ["Country", "Code", "Product", "Cost", "Quantity"]
            data.insert(0, headers)
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
            print(tabulate(data, headers="firstrow"))
        except Exception as e:
            # If there is an error reading the file, print an error message.
            print(f"Error reading the file: {e}")


def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked.
    '''
    # Check if there are any shoes in the shoe_list.
    if len(shoe_list) > 0:
        # Set minimum quantity to a large value
        min_quantity = float("inf")
        # Set a placeholder for the shoe with the lowest quantity.
        min_quantity_shoe = None
        for shoe in shoe_list:
            # Check if the quantity of this shoe is less than the current minimum quantity.
            if shoe.get_quantity() < min_quantity:
                # Update the minimum quantity with the quantity of this shoe.
                min_quantity = shoe.get_quantity()
                # Set this shoe as the shoe with the lowest quantity.
                min_quantity_shoe = shoe
        # Check if a shoe with the lowest quantity was found.
        if min_quantity_shoe:
            inpt = False
            # Keep asking for user input until a valid response is receive.
            while inpt == False:
                add_quantity = input(f"{min_quantity_shoe.product} needs to be restocked, do you want to add quantity? (y/n): ").lower()
                if add_quantity == "y":
                    quant = False
                    # Keep asking for user input until a valid quantity is entered.
                    while quant == False:
                        try:
                            quantity = int(input("Enter the quantity: "))
                            # Add the quantity to the shoe with the lowest quantity.
                            min_quantity_shoe.quantity += quantity
                            with open("inventory.txt", "r") as f:
                                    lines = f.readlines()
                            with open("inventory.txt", "w") as f:
                                for line in lines:
                                    elements = line.split(",")
                                    # Check if this line is for the shoe with the lowest quantity.
                                    if elements[2] == min_quantity_shoe.product:
                                        # Update the quantity for this line.
                                        elements[4] = str((int(elements[4])) + quantity) + "\n"
                                        line = ','.join(elements)
                                    # Write the line back to the file.
                                    f.write(line)
                            inpt = True
                            quant = True
                        # If an invalid quantity was entered.
                        except ValueError:
                            # Inform the user of the error.
                            print("Incorrect input. Please enter the number of quantity.")
                    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                    print("\nProduct quantity has been updated.")
                # If the user does not want to add quantity.
                elif add_quantity == "n":
                    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                    print("\nNo quantity was updated.")
                    inpt = True
                    continue
                else:
                    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                    print("\nIncorrect input. Please enter y or n\n")
                    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                    continue
    else:
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print("\nNo products found.")


def search_shoe():
    '''
    This function will search for a shoe from the list
    using the shoe code and return this object so that it will be printed.
    '''
    # Check if there are any shoes in the shoe_list.
    if len(shoe_list) > 0:
        # Ask the user to enter the code of the shoe to be searched.
        code = input("Enter the code: ")
        # Iterate over the shoe_list to find the shoe with the matching code.
        for shoe in shoe_list:
            if shoe.code == code:
                # Return the shoe object if a match is found.
                return shoe
        # Return "No products found." if no match is found.
        return "No products found."
    else:
        # Return "No products found." if the shoe_list is empty.
        return "No products found."
    

def value_per_item():
    '''
    This function will calculate the total value for each item.
    It will also print this information on the console for all the shoes.
    '''
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n")
    # Initialize an empty list to store the value of each shoe.
    value_list = []
    # Iterate over the shoe_list and calculate the value of each shoe.
    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()
        value_list.append(value)
    # Create a 2D list with the product and its value.
    data = [[shoe.product, value] for shoe, value in zip(shoe_list, value_list)]
    # Define the headers for the data table.
    headers = ["Product", "Value"]
    # Insert the headers at the beginning of the data list.
    data.insert(0, headers)

    # Check if there are any values in the value_list.
    if len(value_list) > 0:
        print(tabulate(data, headers="firstrow"))
    else:
        # Print "No products found." if the value_list is empty
        print("No products found.")


def highest_qty():
    '''
    This function will determine the product with the highest quantity and
    print this shoe as being for sale or not, if no shoes are found.
    '''
    # Initialize a variable max_quantity to negative infinity to keep track 
    # of the maximum quantity found so far.
    max_quantity = float("-inf")
    # Initialize a variable max_quantity_shoe to None to keep track of the 
    # shoe object with the highest quantity.
    max_quantity_shoe = None
    # Loop through the shoe_list to find the shoe with the highest quantity.
    for shoe in shoe_list:
        # Check if the current shoe's quantity is greater than the stored maximum quantity.
        if shoe.get_quantity() > max_quantity:
            # If the current shoe's quantity is greater, update the stored maximum quantity.
            max_quantity = shoe.get_quantity()
            # Also, update the shoe with the maximum quantity.
            max_quantity_shoe = shoe
    if max_quantity_shoe:
        # If a shoe with the highest quantity is found, display its information.
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print(f"\nThe shoe with the highest quantity is: {shoe.product} with {max_quantity} units available for sale.")
    else:
        # If no shoe is found, display a message indicating that no shoes are available for sale.
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print("\nNo shoes available for sale.")


#==========Main Menu=============

usage_message = '''\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
Welcome to the Shoe Inventory System! What would you like to do?

1. Read Shoes Data
2. Add (Capture) Shoes
3. View All Shoes
4. Re-Stock Shoes
5. Search for a Shoe
6. Calculate Value per Item
7. Determine Product with Highest Quantity
8. Quit
'''

user_choice = ""
while True:
    # Ask the user to choose an option from the 'usage_message' menu. 
    user_choice = input(usage_message)
    if user_choice == '1':
        read_shoes_data()
    elif user_choice == '2':
        capture_shoes()
    elif user_choice == '3':
        view_all()
    elif user_choice == '4':
        re_stock()
    elif user_choice == '5':
        shoe = search_shoe()
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n")
        print(shoe)
    elif user_choice == '6':
        value_per_item()
    elif user_choice == '7':
        highest_qty()
    elif user_choice == '8':
        print("Goodbye")
        break
    else:
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print("\nOops - incorrect input")

