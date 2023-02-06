if __name__ == "__main__":
  _, A = int(input()), {*input().split()}
  _, B = int(input()), {*input().split()}
  print(len(A.union(B)))
