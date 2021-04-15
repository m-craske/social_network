#
# File: cramy021_social.py
# Author: Marc Craske
# Student Id: 110305048
# Email Id: cramy021
# Date: 2020.06.02
# Description: Programming assignment 3B - Manage a simple social network.
#
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

# Import profile and list_function libraries.
import profile
import list_function


# Function read_file() - Read the file parameter and store entries as objects in a list. Return the list.
def read_file(filename, profile_list):
      
    # Open the text file and read the first line. Declare profile_list as a new modifiable list.
    infile = open(filename, 'r')
    line = infile.readline()  
    p_list = profile_list
    
    # Loop through until the end of file.    
    while line != '':
    
        # First line. Strip then split the string into a list. Create a new object with each list index passed in as parameters.
        profile_entry = line.strip()
        profile_entry = profile_entry.split()
        profile_obj = profile.Profile(profile_entry[0], profile_entry[1], profile_entry[2], profile_entry[3])
        
        # Read the second line. Strip the return carriage. Call class method to set the new status.
        line = infile.readline()    
        new_status = line.strip('\n')
        profile_obj.set_status(new_status)
        
        # Read the third line. Stip white space and convert to integer. Call class method to set the number of friends.
        line = infile.readline()
        no_friends = int(line.strip())
        profile_obj.set_number_friends(no_friends)
        
        # Read the fourth line. If they have friends (no_friends > 0), this is an email. Strip white space and append to 
        # friends_emails. Read the next line. Loop this until all emails are read. Then call class method to set as friends list.
        line = infile.readline()
        friends_emails = []
        
        if no_friends != 0:
            for count in range(no_friends):
                email = line.strip()
                friends_emails.append(email)
                line = infile.readline()
            
            profile_obj.set_friends_list(friends_emails)    

        # Append this new object to our profile list.
        p_list.append(profile_obj)  
    
    # Close the file    
    infile.close()

    # Return the profile list.    
    return p_list    
        

# Function display_summary() - Read the list parameter and display the formatted objects to screen.
def display_summary(profile_list):
    
    # Display the header formatting to screen.
    print('=' * 80)
    print('Profile Summary')
    print('=' * 80)
    print('-' * 80)
    
    # For each object in the list, call class methods to display the various details. Some strings included for formatting.
    for obj in range(len(profile_list)):
        print(profile_list[obj].get_given_name(), profile_list[obj].get_family_name(), '(', end = '')
        print(profile_list[obj].get_gender(), '|', profile_list[obj].get_email() + ')')
        print('-', profile_list[obj].get_status())
        
        # If the profile has no friends, display the text. Otherwise, display the number of friends with string formatting.
        if profile_list[obj].get_number_friends() == 0:
            print('No friends yet...')
        else:
            print('- Friends (' + str(profile_list[obj].get_number_friends()) + '):')
        
        # Store the friends list in a variable.
        friends = profile_list[obj].get_friends_list()
        
        # Search the profile_list for emails and compare to our friends list. If it's a match, display first and last name.
        if friends:                                     # If friends = TRUE. ie If friends != null (Tony no-friends...)
            for email in friends:                        # For each email address in the friends list
                for item in profile_list:                 # For each object in the profile_list
                    compare_email = item.get_email()       # Get the email and store in variable
                    if compare_email == email:              # If the email in the friends list matches the email in the profile list: 
                        print('   ', item.get_given_name(), item.get_family_name())
        
        # Complete the formatting.
        print('-' * 80)

    
# Function write_to_file() - Open a new text file. Write the list of profiles to it.
def write_to_file(filename, profile_list):
    
    # Open a text file with write access, and initialise index.
    outfile = open(filename, 'w')
    index = 0
    
    # Loop through each profile in the list, and write them to the file as a string. 
    while index < len(profile_list):
        outfile.write(str(profile_list[index]))
        index += 1
        
    # Close the file.
    outfile.close()    

    
# Function find_profile() - Find the position of a profile within the profile list. This will return the index of the profile, or
# retrun -1 if not found.
def find_profile(profile_list, email):
    
    # Declare a new list and initialise index.
    email_list = []
    index = 0
    
    # Loop through the supplied profile list, extracting the email and building a new list only of emails.
    while index < len(profile_list):
        email_compare = profile_list[index].get_email()
        email_list.append(email_compare)                       # Need to get rid of list method and find another way!!
        index += 1
    
    # Call the list_function.find method to find the index of the email.
    index_position = list_function.find(email_list, email)
    
    # Return the index position of the email.
    return index_position
    

# Function add_profile() - Prompt user to add their email and details to the profile_list.
def add_profile(profile_list):
    
    # Prompt user for the email, then call the find_profile method to search for the email. 
    email = input('Please enter email address: ')
    index = find_profile(profile_list, email)
    
    # If the email already exists, display text. Otherwise, prompt the user for the rest of their details.
    if index != -1:
        print(email, 'already exists in profiles.')
    else:
        first_name = input('Please enter given name: ')
        surname = input('Please enter family name: ')
        gender = input('Please enter gender: ')
        status = input('Please enter current status: ')
        
        # Build the new profile oject.
        new_profile = profile.Profile(first_name, surname, email, gender, status)
        
        # Append the profile object to the end of the profile list. Display text showing success.
        profile_list.append(new_profile)
        print('Successfully added', email, 'to profiles.')
    
    # Return the new profile list.
    return profile_list
    

# Function remove_profile() - place your own comments here...  : )
def remove_profile(profile_list):
    
    email = input('Please enter email address: ')


# Main funtion.
def main():
    ### Define a list to store Profile objects
    profile_list = []
    
    # Call funtion to read the text file and store the entries as objects in the list.
    read_file('profiles.txt', profile_list)
    
    # Prompt user for their choice.
    menu_choice = input('Please enter choice [summary|add|remove|search|update|quit]: ')
    
    # Loop through all the menu choices unless 'quit' is chosen.
    while menu_choice != 'quit':
        
        # If one of the menu items is not chosen, display an error.
        while menu_choice != 'summary' and menu_choice != 'add' and menu_choice != 'remove' and menu_choice != 'search' and menu_choice != 'update' and menu_choice != 'quit':
            
            print('Not a valid command - please try again.')
            menu_choice = input('Please enter choice [summary|add|remove|search|update|quit]: ')
        
        # If summary is selected, call the appropriate function.    
        if menu_choice == 'summary':
            
            display_summary(profile_list)
            menu_choice = input('Please enter choice [summary|add|remove|search|update|quit]: ')
        
        # If add is selected, call the appropriate function.    
        elif menu_choice == 'add':   
            
            add_profile(profile_list)           
            menu_choice = input('Please enter choice [summary|add|remove|search|update|quit]: ')
        
        # If remove is selected... tbc
        elif menu_choice == 'remove':
            
            print('In remove command')                  # Used for debugging.
            menu_choice = input('Please enter choice [summary|add|remove|search|update|quit]: ')
        
        # If search is selected, prompt for an email and find it in the profile list. If present, display details to screen.    
        elif menu_choice == 'search':

            # Prompt for email, then call the find function. Assign the position index to variable.
            email = input('Please enter email address: ')
            index = find_profile(profile_list, email)
            
            # If the email exists, call summary function to display the object details. Otherwise display an error.
            if index >= 0:
                display_summary(profile_list[index])            ## Need to fix this formatting!!
            else:
                print(email, 'is not found in profiles.')
            
            menu_choice = input('Please enter choice [summary|add|remove|search|update|quit]: ')
        
        # If update is selected... tbc    
        elif menu_choice == 'update':

            # Prompt user for the email, then call the find_profile method to search for the email. 
            email = input('Please enter email address: ')
            index = find_profile(profile_list, email)

            # If the email is not found, display text. Otherwise, prompt the user for the next menu choice.
            if index == -1:
                print(email, 'is not found in profiles.')
            else:
                first_name = profile_list[index].get_given_name()
                surname = profile_list[index].get_family_name()    
                print('Update', first_name, surname, end = '')
                update_choice = input('[status|add_friend|remove_friend]: ')
                
                # The code below isn't working as yet. I've run out of time and need to submit what I have....
                # if update_choice == 'status':
                #     status_update = input('Please enter status update: ')
                #     profile_list[index].set_status(status_update)
                #     display_summary(profile_list[index]
                
            menu_choice = input('Please enter choice [summary|add|remove|search|update|quit]: ')
    
    # If quit is selected, output the profile list to a new text file.
    if menu_choice == 'quit':
        write_to_file('new_profile.txt', profile_list)


    ### Terminating message 
    print("\n\n-- Program terminating --\n")

# Get the main function to work.
if __name__ == '__main__':
    main()




