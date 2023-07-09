""" Module containing the Contact class. """
import random

class Contact:
    """
    The Contact class groups contact data.

    The Contact class groups the name and number of a contact, as well as waiting times.

    Attributes:
        name (str): Contact name.
        number (str): Whatsapp phone number.
        times (Dict): Dictionary with waiting times
            {
                'time1':1,
                'time2':5,
                'time3':10,
                'time4':2,
            }
        total_time (int): Total waiting time.

    Methods:
        getName(): Return name.
        getNumber(self): Return number.

    Example of use:
        template = Template('arg')
        template.printTemp()
    """
    def __init__(self, name:str, number:str):
        """
        Args:
            name (str): name of contact
            number (str): number of contact
        """
        self.__name = name
        self.__number = self.__parseNumber(number)
        self.times = self.__generateTimes()
        self.total_time = self.__totalTime()

    def getName(self):
        """ Returns contact name. """ 
        return self.__name

    def getNumber(self):
        """ Returns contact number. """ 
        return self.__number

    def __totalTime(self):
        """ Calculates the total estimated time. """ 
        total = 0
        for value in self.times.values():
            total += value
        return total

    def __parseNumber(self, raw_number:str):
        """ Normalize the whatsapp number for the model 5511900000000. """ 
        polished_number = raw_number
        return polished_number
    
    def __generateTimes(self):
        """ Generates a dictionary with waiting times. """ 
        times = {
            'send_msg':random.randint(1, 5),
            'attach':random.randint(2, 6),
            'input_doc':random.randint(5, 11),
            'input_send':random.randint(1, 5),
            'next':random.randint(7, 15)
            }
        return times
