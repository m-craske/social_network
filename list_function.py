#
# PSP Assignment 3 - Provided file (Part A - list_function.py).
# Author: Marc Craske
# Student Id: 110305048
# Email Id: cramy021
# Date: 2020.05.19
# Description: Assignment3A.
#
# This is my own work as defined by the University's
# Academic Misconduct policy.
#
#  Modify this file to include your code solution.
#
#
# Write your function definitions in this file.
# Place your own comments in this file also.
#


# Function length() - Takes a list parameter and returns its' length. For each item in my_list, add to the count. Return the count.
def length(my_list):

    # Declare a counter variable.
    count = 0
    
    # For each value in the list, add to the counter.
    for x in my_list:
        count += 1        
    
    # Return the counter value.    
    return count


# Function to_string() - Takes a list and seperater value and returns a string of the list (using the seperator value)
def to_string(my_list, sep=', '):

    # Declare a string variable.
    string = ''
    
    # For each value in the list, convert to a string and add to the variable.
    for x in my_list:
        
        # Only add the seperater if the list is not empty. This removes seperater at the start.
        if string != '':
            string = string + sep
            
        string = string + str(x)
    
    # Return the string value.
    return string


# Function count() - Searches for the value in the list, and returns how many times that value appears.
def count(my_list, value):
    
    # Declare a counter variable.
    counter = 0
    
    # Use a loop to search for the value parameter. If found, add to the counter.
    for x in my_list:
        
        if value == x:
            counter += 1
            
    # Return the counter value.
    return counter


# Function find() - Searches for the value in the list, and returns the first index in which the value occured.
def find(my_list, value):
    
    # Declare position count variable.
    position = 0
    
    # Loop through the list, adding to the counter for each list item checked. Once the value is found, return the position.
    # If no value is found, return -1.
    for index in my_list:
        
        if value == index:
            return position
        else:
            position += 1
            
    if value != index:
        return -1


# Function insert_value() - Return a copy of the list with the value inserted into it at the specified position.
def insert_value(my_list, value, insert_position):

    # Declare the variables.
    new_list = []                                 # Empty list variable.
    list_index = 0                                # Counter to track the list index position.

    list_length = length(my_list)                 # Call function to determine the length of the list and store as a variable.
    value_position = insert_position              # Declare the specified position as a variable.

    # If the specified position is outside (greater) the list range, then set it at the end of the list.
    if value_position > list_length:
        value_position = list_length + 1
    
    # If the specified position is less than zero, then set it at the beginning of the list.
    if value_position <= 0:
        value_position = 0

    # Loop through all and check the items in the list.
    while list_index < list_length:
        
        # Build up the new list until the insert position is reached.
        if list_index < value_position:
            new_list.append(my_list[list_index])
            list_index += 1
        
        # Once the insert position is reached, add the provided value parameter.    
        elif list_index == value_position:
            new_list.append(value)
            new_list.append(my_list[list_index])
            list_index += 1
        
        # Complete building the remainer of list.
        else:
            new_list.append(my_list[list_index])
            list_index += 1

    # If the insert position is at the end of the list, add the provided value parameter now.        
    if value_position > list_index:
        new_list.append(value)

    # Return the completed list.
    return new_list


# Function remove_value() - Remove the value at the specified position within a list.
def remove_value(my_list, remove_position):

    # Declare the variables.
    new_list = []                                # Empty list variable.
    list_length = length(my_list)                # Call function to determine the length of the list and store as a variable.
    value_position = remove_position             # Declare the position provided as a variable.
    
    # If the remove position provided is outside (greater) than the list length, set it to the last value in the list.
    if value_position > list_length:
        value_position = list_length - 1
    
    # If the remove position provided is less than 0, set it to the first value in the list.
    if value_position <= 0:
        value_position = 0
    
    # Use a loop to rebuild the list without the value of the remove position.
    for index in range(0, list_length):
        if index != value_position:
            new_list.append(my_list[index])

    # Return the completed list.
    return new_list            
            


# Function reverse() - Reverse the numbers in a list. If a number is provided, it will reverse only the first number
# of numbers provided. If a number is not provided, it will reverse the entire list. If the number provided is less than 2, it 
# will not reverse the list.
def reverse(my_list, number=-1):
    
    # Declare a new empty list and the optional number as variables.
    new_list = []
    r_num = number
    
    # If the optional number provided exceeds the boundaries of the list, then set the number as the list length. Use a loop to
    # reverse all numbers.
    if r_num >= length(my_list):
        r_num = length(my_list)
        
        for index in range(-1, -r_num - 1, -1):
            new_list.append(my_list[index])
    
    # If the number provided is between 2 and the list length, use loops to 1. Reverse the list up to the value provided, then
    # 2. Add the remaining numbers in the list unreversed.
    if 2 <= r_num <= length(my_list) - 1:
        
        for index in range((-r_num - 1), -length(my_list) - 1, -1):
            new_list.append(my_list[index])

        for index in range(-r_num, 0, 1):
            new_list.append(my_list[index])
            
    # If the number provided is less than 2 (and greater than 0), return the list unreversed.
    if r_num < 2 and r_num >= 0:
        
        for index in range(0, length(my_list)):
            new_list.append(my_list[index])
    
    # If no number is provided, use a loop to reverse the list.
    if r_num == -1:
        
        for index in range(-1, -length(my_list) - 1, -1):
            new_list.append(my_list[index])

    # Return the generated list.
    return new_list
