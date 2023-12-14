def f(array2D):
    num_rows=len(array2D)
    num_cols=len(array2D[0])

    if num_rows!=num_cols:
        return False
    
    row_sums=[sum(row) for row in array2D]
    col_sums=[sum(col)for col in zip(*array2D)]
    return row_sums == col_sums

print(f([[3,7,2],[4,2,5],[5,2,1]]))