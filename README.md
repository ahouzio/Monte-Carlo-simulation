# Monte-Carlo for $\pi$ approximation :
## Description :
**Monte Carlo methods** are a broad class of computational algorithms that rely on repeated random sampling to obtain numerical results. A classic application is the estimation of pi. 

The idea is to simulate random points on a square of side 2r units centered on (0,0). Imagine a circle inside the same domain with same radius r and inscribed into the square. We then calculate the ratio of number points that lied inside the circle and total number of generated points.

We know that area of the square is $4r^{2}$ while that of circle is $\pi r^{2}$ .  The ratio of these two areas will be $\frac{\pi}{4}$.
When the number of points generated is big enough the area of the circle(or square) will be the number of points inside. By doing simulation of a lot of points, we can get a good approximation of pi

## Usage :

We can generate an image containing the simulated points and the approximation written in the center by the following command : 
```
python approximate_pi.py SIZE N PRECISION
```
where **size** is the size of the image, **N** is the number of points to simulate and **PRECISION** is the precision of the approximation.  
