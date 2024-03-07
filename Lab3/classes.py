#Classes

class MyClass:
    x = 5

#Creat 
    

#EXAMPLE 1:

class Strings:
    def getString(self):
        self.word = input()
    def printString(self):
        print(self.word.upper())

s = Strings()
s.getString()
s.printString()




# class Shape:
#     def init(self,length):
#         self.length = length
#     def area(self):
#         print(0)

# class Square(Shape):
#     def init(self, length):
#         super().init(length)
#         # self.color = color
#     def area(self):
#         print(self.length**2)



# sq = Square(8)
# sq.length = 6
# sq.area()