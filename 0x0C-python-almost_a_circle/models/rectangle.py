#!/usr/bin/python3
""" This module creates a rectangle class based on the base class """


from models.base import Base


class Rectangle(Base):
    """ This class creates a rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ This initializes the class """

        if id is not None and type(id) is not int:
            raise TypeError("id must be an integer")
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        """ This is the getter for the width """

        return self.__width

    @width.setter
    def width(self, value):
        """ This is the setter for the width """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ This is the getter for the height """

        return self.__height

    @height.setter
    def height(self, value):
        """ This is the setter for the height """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ This is the getter for x """

        return self.__x

    @x.setter
    def x(self, value):
        """ This is the setter for x """

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ This is the getter for y """

        return self.__y

    @y.setter
    def y(self, value):
        """ This is the setter for y """

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ This returns the area """

        return self.__width * self.__height

    def display(self):
        """ This prints the rectangle """

        for lines in range(self.__y):
            print()
        for rows in range(0, self.__height):
            print("{}{}".format(' ' * self.__x, '#' * self.__width))

    def __str__(self):
        """ This sets the string format """

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ This updates values for the rectangle """

        newarray = [self.id, self.__width, self.__height, self.__x, self.__y]
        if len(args) >= 1:
            for i in range(len(args)):
                newarray[i] = args[i]
        else:
            for i in kwargs:
                if i == 'id':
                    newarray[0] = kwargs[i]
                if i == 'width':
                    newarray[1] = kwargs[i]
                if i == 'height':
                    newarray[2] = kwargs[i]
                if i == 'x':
                    newarray[3] = kwargs[i]
                if i == 'y':
                    newarray[4] = kwargs[i]
        self.__init__(newarray[1], newarray[2], newarray[3],
                      newarray[4], newarray[0])

    def to_dictionary(self):
        """ This returns the rectangle as a dictionary """

        return {'id': self.id, 'width': self.__width, 'height': self.__height,
                'x': self.__x, 'y': self.__y}
