#!/usr/bin/python3
""" This module creates a Square class that inherits from Rectangle """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ This class inherits from Rectangle, which inherits from Base """

    def __init__(self, size, x=0, y=0, id=None):
        """ This initializes the square """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ This returns the string representation """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """ This is the getter for size """

        return self.width

    @size.setter
    def size(self, value):
        """ This is the setter for size """

        super().__init__(value, value)

    def update(self, *args, **kwargs):
        """ This updates the value of a square """
        newarray = [self.id, self.width, self.x, self.y]
        if len(args) >= 1:
            for i in range(len(args)):
                newarray[i] = args[i]
        else:
            for i in kwargs:
                if i == 'id':
                    newarray[0] = kwargs[i]
                if i == 'size':
                    newarray[1] = kwargs[i]
                if i == 'x':
                    newarray[2] = kwargs[i]
                if i == 'y':
                    newarray[3] = kwargs[i]
        super().__init__(newarray[1], newarray[1], newarray[2],
                         newarray[3], newarray[0])

    def to_dictionary(self):
        """ This returns a dictionary representation """

        return {'id': self.id, 'size': self.width,
                'x': self.x, 'y': self.y}
