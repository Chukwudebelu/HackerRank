# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
  m = int(input().strip(None))
  english_paper = {*map(int,input().split(' '))}
  
  n = int(input().strip(None))
  french_paper = {*map(int,input().split(' '))}
  
  print(len(english_paper.symmetric_difference(french_paper))) # french_paper.symmetric_difference(english_paper)
