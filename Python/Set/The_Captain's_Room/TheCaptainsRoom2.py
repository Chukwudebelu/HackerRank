from itertools import groupby

if __name__ == "__main__":
  K = int(input().strip(' ')) 
  l1 = list(map(int, input().split(' ')))
   
  for room_num, room_list_count in groupby(sorted(l1)): 
    if len(list(room_list_count)) != K:
      print(room_num)
