if __name__ == '__main__':
    n = int(input().strip())

    for n_itr in range(n):
        first_multiple_input = input().rstrip().split()

        px = int(first_multiple_input[0])

        py = int(first_multiple_input[1])

        qx = int(first_multiple_input[2])

        qy = int(first_multiple_input[3])
        
        findPoint = lambda px, py, qx, qy: [(qx << 1) - px, (qy << 1) - py]

        result = findPoint(px, py, qx, qy)

        print(' '.join(map(str, result)))
