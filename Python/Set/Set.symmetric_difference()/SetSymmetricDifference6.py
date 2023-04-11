# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
This solution does not utilise any 'set' methods / constructors such as set(), .add(), |, &, etc.
"""
if __name__ == "__main__":
  _ = input()
  english_ = []
  for eng in input().split(" "):
    english_ += [int(eng)]
    
  _ = input()
  french_ = []
  for fr in input().split(" "):
    french_ += [int(fr)]
    
  # list to hold papers not in either english_ or french_
  english_french = list()
  
  [english_french.append(i) for i in english_ if i not in french_]
  [english_french.append(j) for j in french_ if j not in english_]
  
  print(english_french.__len__())
