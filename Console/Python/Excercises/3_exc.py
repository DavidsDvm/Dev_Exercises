"""
    a kind of calculator that print the contrary number example:
                                1 2 3
                                4 5 6
                                7 8 9
                                  0
    where if u type 1 the program will return 9 or if u type 9 the program
    will return 1
"""

number = input("Add the numbers that you want to transform: ")

numberlist = [int(x) for x in str(number)]

def calculator(a):
    """
        In this function we put the list of numbers and trasnform it
        with our dictionary on the for cicle after we transform this
        list into an int.
    """
    diccionary = {1:9,2:8,3:7,4:6,5:0,6:4,7:3,8:2,9:1,0:5}
    arraylist = []

    for x in a:
        arraylist.append(diccionary[x])

    strings = [str(integer) for integer in arraylist]
    a_string = "".join(strings)
    an_integer = int(a_string)

    print("Your number original number is:",number,"And in our conversion is: ",an_integer)
        
calculator(numberlist)