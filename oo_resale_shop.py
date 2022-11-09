from computer import Computer
from typing import Dict, Union, Optional
itemID = 0


class ResaleShop:

   # What attributes will it need?
 
   # How will you set up your constructor?
   # Remember: in python, all constructors have the same name (__init__)
   
       # main constructor
   def __init__(self, inventory: Dict[int, Dict[str, Union[str, int, bool]]]):

    #Objectifying inventory
    self.inventory = inventory


    def print_inventory(self):
   # If the inventory is not empty
        if inventory:
            # For each item
            for item_id in self.inventory:
                # Print its details
                print(f'Item ID: {item_id} : {inventory[item_id]}')
        else:
            print("No inventory to display.")
 
 #Newly objectified methods with the "self."
def buy(self, computer: Dict[str, Union[str, int, bool]]):
   global itemID
   itemID += 1 # increment itemID
   self.inventory[itemID] = computer
   return itemID
 
def update_price(self, item_id: int, new_price: int):
   if item_id in self.inventory:
       self.inventory[item_id]["price"] = new_price
   else:
       print("Item", item_id, "not found. Cannot update price.")
 
def sell(self, item_id: int):
   if item_id in self.inventory:
       del self.inventory[item_id]
       print("Item", item_id, "sold!")
   else:
       print("Item", item_id, "not found. Please select another item to sell.")

def refurbish(self, item_id: int, new_os: Optional[str] = None):
        if item_id in self.inventory:
            computer = self.inventory[item_id] # locate the computer
            if int(computer.year_made) < 2000:
                computer.price = 0 # too old to sell, donation only
            elif int(computer.year_made) < 2012:
                computer.price = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer.year_made) < 2018:
                computer.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer.price = 1000 # recent stuff

            if new_os is not None:
                computer.operating_system = new_os # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")