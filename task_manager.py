#Displaying a message and prompting the user for information.
print('Welcome to the Task Manager.\n ')
usernames = input('Please enter Username: ')
passwords = input('Please enter Password: ')

#Opening the text file and splitting the username and password.
userfile = open ('user.txt', 'r+')
uselist = userfile.readlines()
usernameList = [us.split(', ')[0] for us in uselist]
userpasswordList = [us.strip('\n').split(', ')[1] for us in uselist]

#Creating a while loop for the login and password credntials as well as an error message if the username is already in the user.txt file.
while 1:
    if usernames in usernameList:
        login = False
        for usnum, usn in enumerate(usernameList):
            if usn == usernames and userpasswordList[usnum] == passwords:
                 print('You are successfully logged in.')
                 login = True
                 break
        if login:
            break
    else:
        print('Error: Please try again. ')
    usernames = input('Please enter Username: ')
    passwords = input('Please enter Password: ')

#Creating a while loop and an if statement to check if the user entered the correct information.
while 1:

#Displaying the various options to the user.
    if usernames == 'admin':
        user_select = input('''Please select one of the following options:
              r - register user
              a - add task
              va - view all tasks
              vm - view my tasks
              s - statistics
              e - exit
              \n
              ''')
    else:
        user_select = input('''Please select one of the following options:
              r - register user
              a - add task
              va - view all tasks
              vm - view my tasks
              e - exit
              \n
              ''')

#If the user selected 'r' then the following menu will display for further information from the user. 
    if user_select == 's':
        task_text = open('tasks.txt','r')
        user_text = open('user.txt','r')
        num = 0
        count = 0
        for i in task_text:
            total_task = 1
            print('This is the total number of tasks: ' + str(total_task))

        for i in user_text:
            total_user = 1
            print('This is the total number of users: ' + str(total_user))

#If the user selected 'r' then the following menu will display for further information from the user. 
    if user_select == 'r':
        user_input_username = input('Please enter a username: ')
        while user_input_username in usernameList:
            print("user already exist.")
            user_input_username = input('Please enter a username: ')
    
        user_input_password = input('Please enter a password: ')
        user_input_confirm_password = input('Please confirm password: ')

#Writing to the text file
    if user_input_password == user_input_confirm_password:
        userfile.write(user_input_username + ", " + user_input_password + "\n")
        userfile.close()
        
    elif user_input_password != user_input_confirm_password:
        print("Error: Please try again.")

#If the user chooses 'a' the following will be executed.
    if user_select == 'a':
         task_text = open('tasks.txt','r+')
         username_input = input('Please enter a username. ')
         user_task = input('Please enter the title of the task. ')
         user_description_task = input('Please give a description of the task. ')
         user_due_date = input('Please provide the due date of the task. ')
        
#Importing a module to give the current date and writing to the text file.    
         from datetime import date
         user_date = str(date.today())
         task_text.write(username_input + ", " + user_task + ", " + user_description_task + ", " + user_due_date + ", " + user_date)
         task_text.close()

#If the user selects va from the menu the following will happen.
    if user_select == 'va':
        task_file = open('tasks.txt','r')
        for i in task_file:
             i.split(", ")
             split_i = i.split(", ")
             print('Task                ' + split_i[1])
             print('Assigned to:        ' + split_i[0])
             print('Date assigned:      ' + split_i[4])
             print('Due date:           ' + split_i[3])
             print('Task Completed:     No')
             print('Task Description:   ' + split_i[2])

#If the user selects vm the following will happen.
    if user_select == 'vm':
        task_file = open('tasks.txt','r')
        for i in task_file:
            i.split(", ")
            split_i = i.split(", ")
            if usernames == split_i[0]:
                i.split(", ")
                split_i = i.split(", ")
                print('Task               ' + split_i[1])
                print('Assigned to        ' + split_i[0])
                print('Date assigned:     ' + split_i[4])
                print('Due date:          ' + split_i[3])
                print('Task Completed:    No')
                print('Task Description:  ' + split_i[2])

#If the user selects e the while loop is discontinued.   
    if user_select == 'e':
        break

    break



