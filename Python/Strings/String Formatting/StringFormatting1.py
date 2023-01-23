def print_formatted(number):
    width = number.bit_length()
    for i in range(1,number+1):
        print('{}'.format(str(i)).rjust(width), end=' ')
        print('{}'.format(oct(i)[2:]).rjust(width), end=' ')
        print('{}'.format(hex(i)[2:].upper()).rjust(width), end=' ')
        print('{}'.format(bin(i)[2:]).rjust(width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
