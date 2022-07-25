class Rectangle:
    def __init__(self, width, height):
      self.width = width
      self.height = height
      
    def __str__(self) -> str:
        return 'Rectangle(width=' + str(self.width) + ', height=' + str(self.height) + ')'
      
    def set_width(self, width):
        self.width = width
        
    def set_height(self, height) :
        self.height = height
        
    def get_area(self) :
        return self.width * self.height
    
    def get_perimeter(self) :
        return (self.width + self.height) * 2
    
    def get_diagonal(self) :
        return ( self.width ** 2 + self.height ** 2 ) ** 0.5
    
    def get_picture(self) :
        if self.width > 50 or self.height > 50 :
            return 'Too big for picture.'

        return ('*' * self.width + '\n') * self.height
    
    def get_amount_inside(self, shape) :
        return ( self.width // shape.width ) * ( self.height // shape.height )
    
    




class Square(Rectangle):
    def __init__(self, side):
      (self.width ,self.height) = (side, side)
      
    def __str__(self) -> str:
        return 'Square(side=' + str(self.width) + ')'
    
    def set_width(self, width):
        (self.width, self.height) = (width, width)
    
    def set_height(self, height) :
        return self.set_width(height)
    
    def set_side(self, side) :
        return self.set_width(side)


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))