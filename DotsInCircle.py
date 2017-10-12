
x_center, y_center, radius = eval(input())
radius_sqr = radius ** 2;

x, y = eval(input())

while( (x, y) != (0, 0) ):
    distance_from_center_sqr = (x - x_center)**2 + (y - y_center)**2
    if distance_from_center_sqr > radius_sqr :
        print ("NO")
        break
    x, y = eval(input())
else:
    print ("YES")
