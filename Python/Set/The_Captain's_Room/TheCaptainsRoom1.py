if __name__ == "__main__":
  # Number of members per group
  K = int(input().lstrip(' ').rstrip(' '))
  
  # Set to hold all unique Room #s (Captain's included)
  room_numbers_captain = set()
  
  # Add all Room #s together
  sum_all_room_numbers = 0
  
  # Loop Room nums
  for _ in input().split():
      room_num = int(_)
      room_numbers_captain.add(room_num)
      sum_all_room_numbers += room_num
      
  print((sum(room_numbers_captain)*K - sum_all_room_numbers)//(K-1))  
