# 1. What is the difference between 
# a parameter and an argument in a python function

"A parameter is the variable listed inside the parentheses in the function"
"definition. An argument is the value that are sent to the function when it is called"

# 2. In your own words, describe what 
# a conditional statement (if/else) is 

"executes a block of code if a specified condition is true."

# 3. write a simple conditional state using a comparision operator(greater than, less than, etc. 
in_game_money=300.00
weapon_in_game=200.00

if in_game_money>weapon_in_game:
    print('you have the weapons,congrates.')
else:
     print('sorry,insufficient funds.')

# 4. Write a conditional statement for food in the refridgerator.
# your conditional statement should be wrapped in a function that takes one (1)
# parameter. The data type for this parameter should be true or false. 
# your function should have a line of code that asks the user if there is food in the refridgerator.
# If there is food in the refridgerator, print time to cook. If there is 
# NOT food in the fridge, print time to shop. 
# When you call your function there should be an argument that accepts 
# a boolean. 

# We know that it talks about functions,parameter,data type ,print,and def
# IF food_in_refridgerator=True
# Else no_food_in_refridgerator=False

def put_food_in_refridgerator(food_in_refridgerator):
    food_in_fridg==True:
      print('time to cook')
    else
     print('time to shop')
put_food_in_refridgerator(True)

# 5. Create a function that checks the inventory of cereal for a store. 
# your function should have a parameter that accepts an integer. In your function
# use a conditional statement to determine if you need to order more cereal.
# If there is more than 10 boxes, print "inventory full", else if there are less than 
# 10 boxes print "we need to order more cereal".
def cereal_inventory(cereal):
   current_cereal_inventory=10
   if ceral >= current_cereal_inventory:
      print("Inventory is full")
   else :
      print("need to order more cereal.")

cereal_inventory(12)