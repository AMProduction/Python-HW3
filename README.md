# Python Homework 3
## Python Classes
### Task 1
### Develop **Rectangle** and **ArrayRectangles** with a predefined functionality
#### On a **Low** level it is obligatory:
To develop **Rectangle** class with following content:
1. 2 fields **sideA** and **sideB** (sides А and В of the rectangle)
1. Constructor with two real parameters **a** and **b** (parameters specify rectangle sides)
1. Constructor with a real parameter **a** (parameter specify side А of a rectangle, side B is always equal to 5)
1. Constructor without parameters (side А of a rectangle equals to 4, side В - 3)
1. Method **GetSideA**, returning value of the side А
1. Method **GetSideВ**, returning value of the side В
1. Method **Area**, calculating and returning the area value
1. Method **Perimeter**, calculating and returning the perimeter value
1. Method **IsSquare**, checking whether current rectangle is shape square or not. Returns true if the shape is square and false in another case.
1. Method **ReplaceSides**, swapping rectangle sides  

#### On **Advanced** level also needed:
Complete Level **Low** Assignment  
Develop class **ArrayRectangles**, in which declare:
1. Field **rectangle_array** - array of rectangles
1. Constructor creating an empty array of rectangles with length n
1. Constructor that receives an arbitrary amount of objects of type **Rectangle** or an array of objects of type **Rectangle**.
1. Method **AddRectangle** that adds a rectangle of type **Rectangle** to the array on the nearest free place and returning true, or returning false, if there is no free space in the array
1. Method **NumberMaxArea**, that returns order number (index) of the rectangle with the maximum area value (numeration starts from zero)
1. Method **NumberMinPerimeter**, that returns order number(index) of the rectangle with the minimum area value (numeration starts from zero)
1. Method **NumberSquare**, that returns the number of squares in the array of rectangles
