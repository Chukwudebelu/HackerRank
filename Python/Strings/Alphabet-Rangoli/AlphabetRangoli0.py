def print_rangoli(size):
    """
    Print an alphabet rangoli of size N
    """
    # Store all the letters
    letter= 'abcdefghijklmnopqrstuvwxyz'
    
    # Rangoli letters (exclude epicenter letter: 'a')
    rng = letter[1:size]
    
    lst = []
    for k in rng:
        lst.append(k)
    
    pat = lst.copy()
    pat.reverse()
    
    # Width of rangoli
    width = 4*len(rng) + 1
    
    rangoli_design = []
    bottom2 = []
    
    k = 1 if size > 1 else 0
    
    # Bottom
    for j in range(len(rng), 0, -1):
        bottom = '-'.join(pat[:-j]) + letter[j].center(3*k, '-') + '-'.join(lst[j:])
    
        rangoli_design.append(bottom.center(width, '-'))
    
    # Center
    cntr = '-'.join(pat[:]) + letter[0].center(3*k, '-') +  '-'.join(lst[0:])
    rangoli_design.append(cntr)
    
    # Top
    for i in range(1, len(rng)):
        top = '-'.join(pat[:-i]) + letter[i].center(3*k, '-') + '-'.join(lst[i:])
        rangoli_design.append(top.center(width, '-'))
    
    if k != 0:
        rangoli_design.append(letter[len(rng)].center(width, '-'))
        
    design_pattern = '\n'.join(rangoli_design)
    
    print(design_pattern)
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
