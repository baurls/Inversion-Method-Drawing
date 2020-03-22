# Inversion Method
## Idea
The circle inversion method provides a point-to-point mapping, mapping an infinite area to a finite and vice versa.

## Definition

![][basic_scene]

A circle provides a unique mapping orign: The circe splits the plane into two areas: **A**I the circle area and **A**O all other points.
For any point **p** ϵ **A**O we can find a corresponding point inside the circle using the following algorithm:
 1. Draw a line **g** through the point **p** and the circle center
 2. Draw a circle border tangent (**t**) and find the point on the circle border intersecting **t**
 3. Find the projection point **p'** on the line **g**.

![][basic_scene2]

## Program results

### Checkerboard
<img src="https://github.com/baurls/Inversion-Method-Drawing/raw/master/images/checkerboard1.png" height="300"><img src="https://github.com/baurls/Inversion-Method-Drawing/raw/master/outputs/checkerboard1.png" height="300">

<img src="https://github.com/baurls/Inversion-Method-Drawing/raw/master/images/checkerboard2.png" height="300"><img src="https://github.com/baurls/Inversion-Method-Drawing/raw/master/outputs/checkerboard2.png" height="300">

<img src="https://github.com/baurls/Inversion-Method-Drawing/raw/master/images/checkerboard3.png" height="300"><img src="https://github.com/baurls/Inversion-Method-Drawing/raw/master/outputs/checkerboard3.png" height="300">

### Wallpaper
<img src="https://github.com/baurls/Inversion-Method-Drawing/raw/master/images/pencils.png" width="300"><img src="https://github.com/baurls/Inversion-Method-Drawing/raw/master/outputs/pencils.png" width="300">

<img src="https://github.com/baurls/Inversion-Method-Drawing/raw/master/images/plant.png" width="300"><img src="https://github.com/baurls/Inversion-Method-Drawing/raw/master/outputs/plant.png" width="300">

<img src="https://github.com/baurls/Inversion-Method-Drawing/raw/master/images/present.png" width="300"><img src="https://github.com/baurls/Inversion-Method-Drawing/raw/master/outputs/present.png" width="300">

[basic_scene]: https://github.com/baurls/Inversion-Method-Drawing/raw/master/images/explanations/basic_scene.png "Overview"
[basic_scene2]: https://github.com/baurls/Inversion-Method-Drawing/raw/master/images/explanations/basic_scene2.png "Overview"


## Properties
### Bijection
First, the following property holds true: We can invert the algorithm for any inner point: Find a point on the circle border, having p' as projection to the line **g** (this can be found by drawing a perpenticular line); then find the (unique) point which intersects the tangant with **g** in **p**. 
This means each point outside the circle has a corresponding point insinde and: We have a bijective mapping between the outer (infinite sized) area and the inner circle area.

### Special Points
#### Border
Using the algorithm above, we see a special property for points on the circle border: A borderpoint **p** maps the the same point **p**. Therefore, any **p** on the border is the algorithm's identity element.

#### Circle Center
There is no mapping for the plane (cicle) center. 


### Line to Line
If we draw a line through the circle center, the output points lie on the same line.

<img src="https://github.com/baurls/Inversion-Method-Drawing/raw/master/images/explanations/line_to_line.png" width="600">

<img src="https://github.com/baurls/Inversion-Method-Drawing/raw/master/images/explanations/line_to_line_inf.png" width="600">



### Line to Circle
If we draw a line which does not intersect the circle center, its mapping becomes a circle
<img src="https://github.com/baurls/Inversion-Method-Drawing/raw/master/images/explanations/line_to_circ.png" width="600">
