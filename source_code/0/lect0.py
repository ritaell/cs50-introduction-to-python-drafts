#comment

""" 
this
is
a 
multi-line 
comment
"""

#ask usere their name
name=input("what is your name? ").strip().title()

#get only the first name
first_name , surname = name.split(" ")
print(f"Your first name is {first_name} and your last name is {surname}")

#print a greeting to the user
print(f"hello, {first_name}")

            
