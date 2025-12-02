def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
       return[]
    row_length =len(mat[0])
    for row in mat:
        if len(row)!=row_length:
            raise ValueError
    return[list(col) for col in zip(*mat)]
def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
       return[]
    row_length =len(mat[0])
    for row in mat:
        if len(row) !=row_length:
           raise ValueError
    return [sum(row) for row in mat]
def col_sums(mat: list[list[float | int]]) -> list[float]:
    transposed =transpose(mat)
    return row_sums(transposed)