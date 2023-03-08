# There is a bus moving in the city which takes and drops some people at each bus stop.

# You are provided with a list (or array) of integer pairs. Elements of each pair represent the number of people that get on the bus (the first item) and the number of people that get off the bus (the second item) at a bus stop.

# Your task is to return the number of people who are still on the bus after the last bus stop (after the last array). Even though it is the last bus stop, the bus might not be empty and some people might still be inside the bus, they are probably sleeping there :D

# Take a look on the test cases.

# Please keep in mind that the test cases ensure that the number of people in the bus is always >= 0. So the returned integer can't be negative.

# The second value in the first pair in the array is 0, since the bus is empty in the first bus stop.

# [[10,0],[3,5],[5,8]] --> 5
# [[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]] --> 17
# [[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]] --> 21

def bus(arr1): #function with list parameter
    mathlist=[] #empty list to keep track of people on the bus at each stop
    for x in arr1: #for loop to go through each pair in list
        mathlist.append((x[0])-(x[1])) #subtract people who got off the bus from those who got on the bus and put that number in our empty list
    print(sum(mathlist)) #adds up the change from each stop to see how many are still on the bus 

bus([[10,0],[3,5],[5,8]]) #first test
bus([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]) #second test
bus([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]) #third test