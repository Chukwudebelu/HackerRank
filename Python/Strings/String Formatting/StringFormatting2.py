def print_formatted(number):
  wide = len(bin(number)[2:])
  for i in range(1,number+1):
    print(format(i).rjust(wide), format(i,'o').rjust(wide), format(i,'X').rjust(wide), format(i,'b').rjust(wide))
    
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
