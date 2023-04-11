if __name__ == "__main__":
  _, english_newspapers = input(), set()
  
  for eng_paper in input().split(' '):
    english_newspapers.add(int(eng_paper))
  
  _, french_newspapers = input(), set()
  
  for fr_paper in input().split(' '):
    french_newspapers.add(int(fr_paper))

  all_papers = english_newspapers.union(french_newspapers)
  both_papers = english_newspapers.intersection(french_newspapers)
  print(len(all_papers.difference(both_papers)))
