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
