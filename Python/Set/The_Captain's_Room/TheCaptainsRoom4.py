if __name__ == "__main__":
  K = int(input())
  rooms_list = list(map(int,input().split(None)))

  room_counter_dict = {} # empty dictionary
  for i in range(len(rooms_list)):
      if rooms_list[i] in room_counter_dict.keys(): # store the count of each room
          room_counter_dict[rooms_list[i]]+=1
          
      else: # initialize dictionary keys
          room_counter_dict[rooms_list[i]]=1
          
  for room, count in room_counter_dict.items():
      if count == 1:
          print(room)
