# Inventory-System

This program is written in Python to manage a list of shoes with their country, code, product, cost, and quantity.   
The program provides various functionalities to read and manipulate the data, and display the results to the user.

# Installation

To use this program, Python must be installed on your system.   
You can download and install the latest version of Python from the official website: 
~~~
https://www.python.org/downloads/  
~~~

The following libraries must be installed to use this program:  
~~~
tabulate
~~~ 
to display the shoe data in a table format.   

To install these libraries, run the following commands:
~~~
pip install tabulate
~~~  
Find more instructions on how to install tabulate in Python: 
~~~
https://pypi.org/project/tabulate/
~~~

# Usage

To use this program, download or clone the repository from Github.   
To run the program, simply execute:
~~~
inventory.py
~~~  
You will be presented with a menu with the available options.  
Enter the number of the operation you would like to perform and follow the instructions.    
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

~~~
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
Welcome to the Shoe Inventory System! What would you like to do?

1. Read Shoes Data
2. Add (Capture) Shoes
3. View All Shoes
4. Re-Stock Shoes
5. Search for a Shoe
6. Calculate Value per Item
7. Determine Product with Highest Quantity
8. Quit
1 
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

Data has been added.

▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
Welcome to the Shoe Inventory System! What would you like to do?

1. Read Shoes Data
2. Add (Capture) Shoes
3. View All Shoes
4. Re-Stock Shoes
5. Search for a Shoe
6. Calculate Value per Item
7. Determine Product with Highest Quantity
8. Quit
3
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
Country        Code      Product                Cost    Quantity
-------------  --------  -------------------  ------  ----------
South Africa   SKU44386  Air Max 90             2300          20
China          SKU90000  Jordan 1               3200          50
Vietnam        SKU63221  Blazer                 1700          19
United States  SKU29077  Cortez                  970          60
Russia         SKU89999  Air Force 1            2000          43
Australia      SKU57443  Waffle Racer           2700           4
Canada         SKU68677  Air Max 97             3600          13
Egypt          SKU19888  Dunk SB                1500          26
Britain        SKU76000  Kobe 4                 3400          32
France         SKU84500  Pegasus                2490          28
Zimbabwe       SKU20207  Air Presto             2999           7
Morocco        SKU77744  Challenge Court        1450          11
Israel         SKU29888  Air Zoom Generation    2680           6
Uganda         SKU33000  Flyknit Racer          4900           9
Pakistan       SKU77999  Air Yeezy 2            4389          67
Brazil         SKU44600  Air Jordan 11          3870          24
Columbia       SKU87500  Air Huarache           2683           8
India          SKU38773  Air Max 1              1900          29
Vietnam        SKU95000  Air Mag                2000           2
Israel         SKU79084  Air Foamposite         2430           4
China          SKU93222  Air Stab               1630          10
South Korea    SKU66734  Hyperdunk              1899           7
Australia      SKU71827  Zoom Hyperfuse         1400          15
France         SKU20394  Eric Koston 1          2322          17

▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
Welcome to the Shoe Inventory System! What would you like to do?

1. Read Shoes Data
2. Add (Capture) Shoes
3. View All Shoes
4. Re-Stock Shoes
5. Search for a Shoe
6. Calculate Value per Item
7. Determine Product with Highest Quantity
8. Quit
6
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

Product                Value
-------------------  -------
Air Max 90             46000
Jordan 1              160000
Blazer                 32300
Cortez                 58200
Air Force 1            86000
Waffle Racer           10800
Air Max 97             46800
Dunk SB                39000
Kobe 4                108800
Pegasus                69720
Air Presto             20993
Challenge Court        15950
Air Zoom Generation    16080
Flyknit Racer          44100
Air Yeezy 2           294063
Air Jordan 11          92880
Air Huarache           21464
Air Max 1              55100
Air Mag                 4000
Air Foamposite          9720
Air Stab               16300
Hyperdunk              13293
Zoom Hyperfuse         21000
Eric Koston 1          39474

▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
Welcome to the Shoe Inventory System! What would you like to do?

1. Read Shoes Data
2. Add (Capture) Shoes
3. View All Shoes
4. Re-Stock Shoes
5. Search for a Shoe
6. Calculate Value per Item
7. Determine Product with Highest Quantity
8. Quit
7
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

The shoe with the highest quantity is: Eric Koston 1 with 67 units available for sale.

▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
Welcome to the Shoe Inventory System! What would you like to do?

1. Read Shoes Data
2. Add (Capture) Shoes
3. View All Shoes
4. Re-Stock Shoes
5. Search for a Shoe
6. Calculate Value per Item
7. Determine Product with Highest Quantity
8. Quit
8
Goodbye
~~~
  
  

![alt text](https://github.com/filosoho/Inventory-System/blob/3305398eff5234ecdd270b5ac92fd451795285e1/Inventory%20System.png?raw=true)


# Contributing

If you would like to contribute to this program, feel free to submit a pull request. Please include a detailed description of the changes made and the reasons for the changes.

# License

Feel free to use and modify the code as per your requirements.
