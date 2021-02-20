class Rectangle:
    sideA = 5.8
    sideB = 13.5

    def __init__(self, *args):
        if len(args) == 2:
            self.sideA = float(args[0])
            self.sideB = float(args[1])
        elif len(args) == 1:
            self.sideA = float(args[0])
            self.sideB = 5.0
        else:
            self.sideA = 4.0
            self.sideB = 3.0

    def GetSideA(self):
        return self.sideA

    def GetSideB(self):
        return self.sideB

    def Area(self):
        return self.sideA * self.sideB

    def Perimeter(self):
        return (self.sideA + self.sideB) * 2

    def IsSquare(self):
        if (self.sideA == self.sideB):
            return True
        else:
            return False

    def ReplaceSides(self):
        self.sideA, self.sideB = self.sideB, self.sideA


class ArrayRectangles(Rectangle):
    rectangle_array = [None] * 10

    def __init__(self, arg):
        if (isinstance(arg, int)) and (arg > 0):
            self.rectangle_array = [None] * arg
        elif (isinstance(arg, list)):
            self.rectangle_array.extend(arg)
        else:
            self.rectangle_array.append(arg)

    def AddRectangle(self, arg):
        if (isinstance(arg, Rectangle)):
            for rec in range(len(self.rectangle_array)):
                if (self.rectangle_array[rec] == "None"):
                    self.rectangle_array.insert(rec, arg)
                    break
                    return True
                else:
                    continue
                    return False
        else:
            return None

    def NumberMaxArea(self):
        max_index = 0
        for rec in range(1, len(self.rectangle_array)):
            if (self.rectangle_array[rec].Area() >= self.rectangle_array[max_index].Area()):
                max_index = rec
            else:
                continue
        return max_index

    def NumberMinPerimeter(self):
        min_index = 0
        for rec in range(1, len(self.rectangle_array)):
            if (self.rectangle_array[rec].Perimeter() <= self.rectangle_array[min_index].Perimeter()):
                min_index = rec
            else:
                continue
        return min_index

    def NumberSquare(self):
        squares_count = 0
        for rec in self.rectangle_array:
            if rec.IsSquare():
                squares_count += 1
            else:
                continue
        return squares_count
