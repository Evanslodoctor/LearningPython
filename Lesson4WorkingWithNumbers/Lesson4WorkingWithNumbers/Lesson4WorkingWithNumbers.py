area = 0
height = 10
width = 20
#Calculate area of the triangel
area = height*width /2
print(area)

# Storing numbers

print(" The are of triangle will be %.f" % area )
#printing the formated decimal number with right justified to take 6 spaces 
#with leading 0s
print("My favorite number is %06d !" % 42)

# Do the same thing with the .format syntax to include out output
print("I have {0:.2f} cats".format(area)) 
print("I have {0:f} cats".format(area)) 
print("I have {0:03d} cats".format(6)) 



