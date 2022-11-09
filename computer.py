from typing import Dict, Union, Optional

class Computer:

    # What attributes will it need?

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    
    # main constructor
    def __init__(self,description,processor_type,hard_drive_capacity,memory,operating_system,year_made,price):
     
        #Objectifying all the attributes
       self.description=description
       self.processor_type=processor_type
       self.hard_drive_capacity=hard_drive_capacity
       self.memory=memory
       self.operating_system=operating_system
       self.year_made = year_made
       self.price = price

    def create_computer(description,
                    processor_type,
                    hard_drive_capacity,
                    memory,
                    operating_system,
                    year_made,
                    price):
        return {'description': description,
            'processor_type': processor_type,
            'hard_drive_capacity': hard_drive_capacity,
            'memory': memory,
            'operating_system': operating_system,
            'year_made': year_made,
            'price': price
    }