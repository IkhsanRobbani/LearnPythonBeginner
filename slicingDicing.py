#slicing atau dicing kaya ngambil beberapa elemen list atau belah list
sebuah = ["1",2.0,4.0,6.0,8.0,3.0,6.0]
a=sebuah[:2]
b=sebuah[2:]
c=sebuah[-1]
d=sebuah[3:5]
print(a)
print(b)
print(c)
print(d)
areas = [["hallway", 11.25], ["kitchen", 18.0], ["living room", 20.0], ["bedroom", 10.75], ["bathroom", 9.50]]

print(areas[1][0])
print(areas[-1][1])

#updating list data


#copy list dg benar tanpa merubah list original
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy
areas_copy = areas[:]

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)