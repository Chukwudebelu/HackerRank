from collections import deque

def mutate_string(string, position, character):
  deq = deque(string) # no need to include max_length parameter
  deq[position] = character
  return ''.join(deq)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
