# Inventory-System

This program is written in Python to manage a list of shoes with their country, code, product, cost, and quantity. 
The program provides various functionalities to read and manipulate the data, and display the results to the user.

# Installation

To use this program, Python must be installed on your system. 
You can download and install the latest version of Python from the official website: https://www.python.org/downloads/

The following libraries must be installed to use this program:

tabulate: To display the shoe data in a table format.
To install these libraries, run the following commands:

pip install tabulate

Find more instructions on how to install tabulate in Python: https://pypi.org/project/tabulate/

# Usage

To use this program, download or clone the repository from Github. 
To run the program, simply execute the main.py file. 
You will be presented with a menu with the available options. Enter the number of the operation you would like to perform and follow the instructions.

python inventory.py

This will start the program and display the available options to the user.

# Program features

The program has the following functionalities:

1. Read Shoes Data: Reads data from the "inventory.txt" file and creates a Shoe object with each line of data. Appends each Shoe object to the shoe_list.
2. Add (Capture) Shoes: Captures data about a shoe from user input, creates a Shoe object with this data and appends the object to the shoe_list. Prompts the user if they would like to add the data to the "inventory.txt" file.
3. View All Shoes: This function will iterate over the shoes list and print the details of the shoes returned from the __str__ function. Optional: you can organize your data in a table format by using Python’s tabulate module.
4. Re-Stock Shoes: This function will find the shoe object with the lowest quantity, which is the shoes that need to be re-stocked.
5. Search for a Shoe: This function will search for a shoe from the list using the shoe code and return this object so that it will be printed.
6. Calculate Value per Item: This function will calculate the total value for each item. It will also print this information on the console for all the shoes.
7. Determine Product with Highest Quantity: This function will determine the product with the highest quantity and print this shoe as being for sale or not, if no shoes are found.
8. Quit: Exits the program.

https://github.com/filosoho/Inventory-System/blob/519762aa34d2ad7db90c48e7ca5097c7f9255656/Inventory%20System.png

# Contributing

If you would like to contribute to this program, feel free to submit a pull request. Please include a detailed description of the changes made and the reasons for the changes.

# License

Feel free to use and modify the code as per your requirements.

# Author

This program was written by Anna Stachowska.
