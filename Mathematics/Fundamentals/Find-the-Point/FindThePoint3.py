def findPoint(px: int, py: int, qx: int, qy: int) -> list:
    x_distance: int = qx - px
    y_distance: int = qy - py
    
    rx: int = qx + x_distance
    ry: int = qy + y_distance
    
    r: list = [rx, ry]
    
    return r

if __name__ == '__main__':
    n = int(input().strip())

    for n_itr in range(n):
        first_multiple_input = input().rstrip().split()

        px = int(first_multiple_input[0])

        py = int(first_multiple_input[1])

        qx = int(first_multiple_input[2])

        qy = int(first_multiple_input[3])

        result = findPoint(px, py, qx, qy)

        print(' '.join(map(str, result)))
