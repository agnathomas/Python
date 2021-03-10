class rectangle():
    def __init__(self, breadth, length):
        self.breadth = breadth
        self.length = length
    def area(self):
        return self.breadth * self.length

    def perimeter(self):
        return 2 * (self.breadth + self.length)
        print("Rectangle1")
        a = int(input("Enter length of rectangle1: "))
        b = int(input("Enter breadth of rectangle1: "))
        obj1= rectangle(a, b)
        print("Area of rectangle:", obj1.area())
        print("Perimeter of rectangle:", obj1.perimeter())

        print("Rectangle2")
        a = int(input("Enter length of rectangle2: "))
        b = int(input("Enter breadth of rectangle2: "))
        obj2= rectangle(a, b)
        print("Area of rectangle:", obj2.area())
        print("Perimeter of rectangle:", obj2.perimeter())

        if obj1.area() > obj2.area():
            print("Area of rectangle1 grater than rectangle2")
        elif obj1.area() == obj2.area():
            print("Area of rectangle1 and rectangle2 are equal")
        else:
            print("Area of rectangle1 less than rectangle2")

        if obj1.perimeter() > obj2.perimeter():
            print("Perimeter of rectangle1 grater than rectangle2")
        elif obj1.area() == obj2.area():
            print("Perimeter of rectangle1 and rectangle2 are equal")
        else:
            print("Perimeter of rectangle1 less than rectangle2")