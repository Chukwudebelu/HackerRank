if __name__ == '__main__':
    N = int(input())
   
lst = []
for i in range(0,N):
    k = str(input()) # retain user input
    if k.startswith('append'):
        command, num = k.split()
        lst.append(int(num))
    elif k.startswith('insert'):
        command, intgr, pos = k.split()
        lst.insert(int(intgr), int(pos))
    elif k.startswith('remove'):
        command, num = k.split()
        lst.remove(int(num))
    elif k.startswith('sort'):
        lst.sort(reverse=False)
    elif k.startswith('pop'):
        lst.pop()
    elif k.startswith('reverse'):
        lst.reverse()
    else:
        print(lst)
