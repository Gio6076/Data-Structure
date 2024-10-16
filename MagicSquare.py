def MagicSquare(n):
    if n % 2 == 0:
        raise ValueError("PLEASE ENTER ODD NUMBER ONLY. INVALID")
    magic_square = [[0] * n for _ in range(n)]
    num = 1
    i, j = 0, n // 2  
    while num <= n * n:
        magic_square[i][j] = num
        num += 1
        new_i = (i + 2) % n
        new_j = (j - 1) % n  
        if magic_square[new_i][new_j] != 0:
            i = (i + 1) % n
        else:
            i, j = new_i, new_j
    return magic_square
def square_magix(square):
    n = len(square)
    for row in square:
        print(" ".join(f"{x:2d}" for x in row))
n = int(input("PLEASE ENTER THE SIZE OF THE MAGIC SQUARE: "))
magic_square = MagicSquare(n)
square_magix(magic_square)
