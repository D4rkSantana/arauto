""" 
Modulo content Template
"""

class Template:
    """ 
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, Fusce suscipit ac enim et eleifend
    Quisque sed augue ut justo varius ultrices eu non lacus.

    Attributes:
        arg (str): argument

    Methods:
        printTemp(): print arg + Lorem ipsum dolor sit amet, consectetur adipiscing elit.

    Example of use:
        template = Template('arg')
        template.printTemp()
    """
    def __init__(self, arg:str):
        """
        Args:
            arg (arg): argument
        """
        self.arg = arg

    def printTemp(self):
        """ Print arg + lorem ipsum. """ 
        print(self.arg)
        print('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')