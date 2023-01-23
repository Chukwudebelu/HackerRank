def print_formatted(number):
    len_b = len(f'{number:b}')
    for i in range(1,number+1):
        print(f'{i:d}'.rjust(len_b), f'{i:o}'.rjust(len_b), f'{i:X}'.rjust(len_b), f'{i:b}'.rjust(len_b), end='\n')  
    """
    x: lower case x denotes lowercase letters for hexadecimal: a, b, c, d, e, f
    X: uppercase x denotes uppercase letters for hexadecimal: A, B, C, D, E, F
    """
       
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
