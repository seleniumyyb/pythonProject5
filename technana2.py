'''
calculations_to_hours = 24                                       #ERROR HANDLING WITH TRY/EXCEPT OR TRY/CATCH ERROR
name_of_units = "hours"

def days_to_units(num_of_dys):
    return (f"{num_of_dys} days are {num_of_dys * calculations_to_hours} {name_of_units}")

def validate_and_execute():
     try:
        user_input_number = int(user_input)
        if user_input_number> 0:
            calculated_values = days_to_units(user_input_number)
            print(calculated_values)
        elif user_input_number ==0:
            print("You entered a 0 , pls. enter a valid positive number")
        else:                                                                             #add this because neg. no not printafter applying try
            print("You entered a negative number so no conversion for you")
     except ValueError:
        print("Your input is not a number.Don't ruin my program")

user_input = input("Hey user , Enter a number a days and i ll converted it to hours:\n ")
validate_and_execute()



                                                 # WHILE LOOPS
calculations_to_hours = 24
name_of_units = "hours"

def days_to_units(num_of_dys):
    return (f"{num_of_dys} days are {num_of_dys * calculations_to_hours} {name_of_units}")

def validate_and_execute():
     try:
        user_input_number = int(user_input)
        if user_input_number> 0:
            calculated_values = days_to_units(user_input_number)
            print(calculated_values)
        elif user_input_number ==0:
            print("You entered a 0 , pls. enter a valid positive number")
        else:                                                                             #add this because neg. no not printafter applying try
            print("You entered a negative number so no conversion for you")
     except ValueError:
        print("Your input is not a number.Don't ruin my program")

while True:
        user_input = input("Hey user , Enter a number a days and i ll converted it to hours:\n ")
        validate_and_execute()
        
                                                                         # LET THE GET EXIT

calculations_to_hours = 24
name_of_units = "hours"

def days_to_units(num_of_dys):
    return (f"{num_of_dys} days are {num_of_dys * calculations_to_hours} {name_of_units}")

def validate_and_execute():
     try:
        user_input_number = int(user_input)
        if user_input_number> 0:
            calculated_values = days_to_units(user_input_number)
            print(calculated_values)
        elif user_input_number ==0:
            print("You entered a 0 , pls. enter a valid positive number")
        else:
            print("You entered a negative number so no conversion for you")
     except ValueError:
        print("Your input is not a number.Don't ruin my program")
user_input = ""
while user_input != "exit":
        user_input = input("Hey user , Enter a number a days and i ll converted it to hours:\n ")
        validate_and_execute()


                       # Lists and for Loop
calculations_to_hours = 24
name_of_units = "hours"


def days_to_units(num_of_days):
    return (f"{num_of_days} days are {num_of_days * calculations_to_hours} {name_of_units}")


def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)
        if user_input_number > 0:
            calculated_values = days_to_units(user_input_number)
            print(calculated_values)
        elif user_input_number == 0:
            print("You entered a 0 , pls. enter a valid positive number")
        else:
            print("You entered a negative number so no conversion for you")
    except ValueError:
        print("Your input is not a valid number.Don't ruin my program")
                                                                                  # add list

user_input = ""
while user_input != "exit":
    user_input = input("Hey user , Enter a number a days as a comma separated list and i ll converted it to hours:\n ")
    list_of_days = user_input.split(", ")
    print(list_of_days)
    print(set(list_of_days))

    print(type(list_of_days))
    print(type(set(list_of_days)))

    for num_of_days_element in set(list_of_days):
        validate_and_execute()
'''
                                                # set use to avoid duplicate value

calculations_to_hours = 24
name_of_units = "hours"


def days_to_units(num_of_days):
    return (f"{num_of_days} days are {num_of_days * calculations_to_hours} {name_of_units}")


def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)
        if user_input_number > 0:
            calculated_values = days_to_units(user_input_number)
            print(calculated_values)
        elif user_input_number == 0:
            print("You entered a 0 , pls. enter a valid positive number")
        else:
            print("You entered a negative number so no conversion for you")
    except ValueError:
        print("Your input is not a valid number.Don't ruin my program")
                                                                                #add set
user_input = ""
while user_input != "exit":
    user_input = input("Hey user , Enter a number a days as a comma separated list and i ll converted it to hours:\n ")
    #list_of_days = user_input.split(", ")
    #print(list_of_days)
    #print(set(list_of_days))

    #print(type(list_of_days))
    #print(type(set(list_of_days)))

    for num_of_days_element in set(user_input.split(", ")):
        validate_and_execute()
