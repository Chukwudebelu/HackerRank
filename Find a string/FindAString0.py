def count_substring(string, sub_string):
    m = len(sub_string) 
    count = 0
    for i in range(0,len(string)-m+1):
        if string[i:i+m] == sub_string:
            count += 1
        else:
            continue
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
