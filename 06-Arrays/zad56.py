def covert_array(array):
    result=[]
    for row in array: 
        for element in row:
            result.append(element)

    return result




array=[[2,3],[1,5]]
print(covert_array(array)) 



