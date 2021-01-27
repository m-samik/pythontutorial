#############################################################
###################### Binary Search ########################
#############################################################

# Binary Search Function :: Created by Us Manually.
# value == parameter of our function , for the value to search .
# database == from where our value will be searched

database=list(range(1,12))
def binary_search(database,value):
    
    start=0
    end=len(database) -1
    middle=int((start + end) / 2)
    # while not here is used beacause we dont want our program running infinetly so whenever it gets true it will convert itself to false.
    while not (database[middle] == value):
        if value > database[middle]:
            start = middle + 1
        else:
            end = middle - 1
        middle=int((start + end) / 2)
        print("start :",start , "End :",end ,"Middle :",middle)
        
    if database[middle] == value:
        print("We Found the Value at ",middle)
    else:
        print("not found")
        
    print("start :",start , "End :",end ,"Middle :",middle)
    
value = int(input("Enter the Value for Search in Database : "))
binary_search(database,value)
