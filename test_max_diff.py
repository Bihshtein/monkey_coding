def solution(m):
    rows_to_paint = []
    columns_to_paint = []
    rows_count = (len(m))
    print(rows_count)
    columns_count = len(m[0])
    for i in range(rows_count):
        for j in range(columns_count):
            if m[i][j] == 0:
                rows_to_paint.append(i)
                columns_to_paint.append(j)

    for i in range(rows_to_paint]):
        for
    j in range(columns_count):
    m[i][j] = 0
    for i in range(rows_count):
        for
    j in range(columns_to_paint): \
        m[i][j] = 0
    return m


m = [[1, 0, 2, 3],
     [4, 5, 6, 7],
     [8, 9, 10, 0]]
m= solution(m)
print(m)