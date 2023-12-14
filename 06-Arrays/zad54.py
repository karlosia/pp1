def transpose_matrix(m):



    result=[[0,0,0],[0,0,0],[0,0,0]]

    for i in range(len(m)):
        for j in range(len(m[0])):
            result[i][j]=m[j][i]
           
    return result



    
