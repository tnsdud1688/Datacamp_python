# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0 :
         offset = offset -1
    else :
        offset = offset + 1
    print(offset)
    
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for demensions in areas :
    print(demensions)
    
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate()
for index, a in enumerate(areas) :
    print("room " + str(index) + ": " + str(a))

