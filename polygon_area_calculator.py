from tkinter import Widget
from turtle import width


class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    
    def set_width(self, width):
        self.width = width
        return self.width
    
    def set_height(self, height):
        self.height = height
        return self.height

    
    def __str__(self):
        return f'Rectangle(width = {self.width}, height ={self.height})'
        
    def get_area(self):
        self.area = self.width * self.height 
        return self.area 
    
    def get_perimeter(self):
        self.perimeter = (2 * self.width) + (2 * self.height )
        return self.perimeter 

    def get_diagonal(self):
        self.diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
        return self.diagonal 
    
    def get_picture(self):
        self.count = 0
        if self.width | self.height >= 50:  return ("Too big for picture.")

        while self.height > 0:
            print(self.width * '*')
            self.height -= 1
            self.count += 1 
        self.height += self.count
        self.count = 0
        
    def get_amount_inside(self, sq_or_rec):
        self.sq_or_rec = sq_or_rec.get_area()
        self.amount = list()
        self.amount.append(self.sq_or_rec)
        self.amount.append(self.get_area())
        self.amount.sort()
        self.amount = round(self.amount[1] / self.amount[0]) 
        return self.amount



class Square(Rectangle):
    def __init__(self,width_height):
        self.width = self.height = width_height
        self.set_width(width_height)
        self.set_height(width_height)


    def set_side(self, width_height):
        self.width = self.height = width_height

    def __str__(self):
        return f'Square(side={self.width})'
        



rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
rect.get_picture()

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
sq.get_picture()

rect.set_height(8)
rect.set_width(4)

print(rect.get_amount_inside(sq))
