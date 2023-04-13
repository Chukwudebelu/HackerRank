if __name__ == "__main__":
  for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
      print(sum(map(lambda x: 10**x, range(i))) ** 2)
