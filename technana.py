#how many minutes there are in 20 days
#print(20*24*60)
#string concatenation - adding string together
#print("20 days are " + str(20*24*60) + " minutes")
# one more elegent way that looks good code
#print(f"20 days are {20*24*60} minutes")                 # python new version have this new function using different syntax
                                                          # f is stand for formatting
#print(f"50 days are {50*24*60} minutes")
#print(f"30 days are {30*24*60} minutes")
#print(f"30 days are {30*24*60*60} seconds")             #using variables-are containers for storing values no need to repeat 4 times
#print(f"50 days are {50*24*60*60} seconds")
#print(f"60 days are {60*24*60*60} seconds")
#print(f"70 days are {70*24*60*60} seconds")            #python is dynamically typed vs static typing
'''                                                     #use descriptive variables name
calculations_to_seconds = 24*60*60
print(f"30 days are {30*calculations_to_seconds} seconds")
print(f"50 days are {50*calculations_to_seconds} seconds")
print(f"60 days are {60*calculations_to_seconds} seconds")
print(f"70 days are {70*calculations_to_seconds} seconds")


calculations_to_units = 24*60*60                                    #result will be same as above
name_of_units = "seconds"
print(f"30 days are {30*calculations_to_units} {name_of_units}")
print(f"50 days are {50*calculations_to_units} {name_of_units}")
print(f"60 days are {60*calculations_to_units} {name_of_units}")
print(f"70 days are {70*calculations_to_units} {name_of_units}")


calculations_to_units = 24                                    #for HOURS CALCULATIONS
name_of_units = "hours"
print(f"30 days are {30*calculations_to_units} {name_of_units}")
print(f"50 days are {50*calculations_to_units} {name_of_units}")
print(f"60 days are {60*calculations_to_units} {name_of_units}")
print(f"70 days are {70*calculations_to_units} {name_of_units}")

#function to avoid repeating the same logic in your code using def keyword



calculations_to_units = 24
name_of_units = "hours"
def days_to_units():
    print(f"30 days are {30 * calculations_to_units} {name_of_units}")
    print("All good")
# when run this nothing display why block of code only runs when it called
days_to_units()
# now runs always use def name


#function parameters- information can be passed into functions as parameters and parameters are also called arguments
calculations_to_hours = 24
name_of_units = "hours"
def days_to_units(num_of_dys, custome_message):
    print(f"{num_of_dys}days are {num_of_dys * calculations_to_hours} {name_of_units}")
    print(custome_message)

days_to_units(20, "Awesome")                                      #() input parameter alwayas filled with value otherwise do not run
days_to_units(30, "great")



calculations_to_hours = 24
name_of_units = "hours"
def days_to_units(num_of_dys):
  return (f"{num_of_dys} days are {num_of_dys * calculations_to_hours} {name_of_units}")

user_input = int(input("Hey user , Enter a number a days and i ll converted it to hours:\n "))
#user_input_number = int(user_input)

calculated_values = days_to_units(user_input)
print(calculated_values)



                                  #conditional(if/else)and Boolean data type - validate user input
calculations_to_hours = 24
name_of_units = "hours"

def days_to_units(num_of_dys):
  print(num_of_dys>0)
  if num_of_dys>0:
    return (f"{num_of_dys} days are {num_of_dys * calculations_to_hours} {name_of_units}")
  # for 0 entry
  elif num_of_dys == 0:
    return " You entered a 0 , pls. enter a valid positive number"
  else:
    return "you entered a negative value, so no conversion for you!"
user_input = int(input("Hey user , Enter a number a days and i ll converted it to hours:\n "))
#user_input_number = int(user_input)

calculated_values = days_to_units(user_input)
print(calculated_values)


                                        # MORE USER INPUT VALIDATION LIKE TEXT MSG. OR ENTERED FLOT VALUE
calculations_to_hours = 24
name_of_units = "hours"

def days_to_units(num_of_dys):
  print(num_of_dys>0)
  if num_of_dys>0:
    return (f"{num_of_dys} days are {num_of_dys * calculations_to_hours} {name_of_units}")
  # for 0 entry
  elif num_of_dys == 0:
    return " You entered a 0 , pls. enter a valid positive number"
  #else:
   # return "you entered a negative value, so no conversion for you!"
user_input = input("Hey user , Enter a number a days and i ll converted it to hours:\n ")

if user_input.isdigit():
    user_input_number = int(user_input)
    calculated_values = days_to_units(user_input_number)
    print(calculated_values)
else:
  print("Your input is not a number.Don't ruin my program")            #Avoid to cresh


                                       # CLEANUP OUR CODE
calculations_to_hours = 24
name_of_units = "hours"

def days_to_units(num_of_dys):
  print(num_of_dys>0)
  if num_of_dys>0:
    return (f"{num_of_dys} days are {num_of_dys * calculations_to_hours} {name_of_units}")
  # for 0 entry
  elif num_of_dys == 0:
    return " You entered a 0 , pls. enter a valid positive number"
  #else:
   # return "you entered a negative value, so no conversion for you!"

def validate_and_execute():
     if user_input.isdigit():
        user_input_number = int(user_input)
        calculated_values = days_to_units(user_input_number)
        print(calculated_values)
     else:
        print("Your input is not a number.Don't ruin my program")

user_input = input("Hey user , Enter a number a days and i ll converted it to hours:\n ")
validate_and_execute()

'''
                                     # NESTED If...Else put all the validation in one place
calculations_to_hours = 24
name_of_units = "hours"

def days_to_units(num_of_dys):
    return (f"{num_of_dys} days are {num_of_dys * calculations_to_hours} {name_of_units}")

def validate_and_execute():
     if user_input.isdigit():
        user_input_number = int(user_input)
        if user_input_number> 0:
            calculated_values = days_to_units(user_input_number)
            print(calculated_values)
        elif user_input_number ==0:
            print("You entered a 0 , pls. enter a valid positive number")
     else:
        print("Your input is not a number.Don't ruin my program")

user_input = input("Hey user , Enter a number a days and i ll converted it to hours:\n ")
validate_and_execute()
