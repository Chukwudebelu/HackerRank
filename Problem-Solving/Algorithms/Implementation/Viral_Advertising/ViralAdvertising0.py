def viralAdvertising(n):
    shared = [5]; liked = [5//2] # Day 1
    for i in range(n-1):
      shared.append(liked[i] * 3)
      liked += [shared[i+1] // 2]
    return sum(liked)


if __name__ == '__main__':
    n = int(input().strip())
    
    print(viralAdvertising(n))
