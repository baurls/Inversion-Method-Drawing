# Inversion Method
## Idea
The circle inversion method provides a point-to-point mapping, mapping an infinite area to a finite and vice versa.

## Definition

![](https://github.com/baurls/Inversion-Method-Drawing/raw/master/images/explanations/basic_scene.png "Overview")

A circle provides a unique mapping orign: The circe splits the plane into two areas: **A**I the circle area and **A**O all other points.
For any point **p** ϵ **A**O we can find a corresponding point inside the circle using the following algorithm:
 1. Draw a line **g** through the point **p** and the circle center
 2. Draw a circle border tangent (**t**) and find the point on the circle border intersecting **t**
 3. Find the projection point **p'** on the line **g**.
