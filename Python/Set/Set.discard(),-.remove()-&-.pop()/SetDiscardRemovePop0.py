def set_operations(s, method):
    task = method.split()
    todo = task[0]
    
    if len(task) != 1:
        num = int(task[1])
    
    # for i in range(N):
    if todo == "remove":
        s.remove(num)
        
    elif todo == "pop": 
        s.pop()

    elif todo == "discard":
        s.discard(num)
        
    return s
            

if __name__ == "__main__":
    n = int(input())
    s = set(map(int, input().split()))
    
    N = int(input())
    
    for _ in range(N):
        result = set_operations(s, str(input()))
        
    print(sum(result))
