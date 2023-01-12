records =[]
all_scores = []
names = []

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())

        records.append([name,score])
        all_scores.append(score)

    unique_scores = list(set(all_scores))
    unique_scores.sort()

    for j in range(len(records)):
        if unique_scores[1] == records[j][1]:
            names.append(records[j][0])
        
    names.sort()
    for k in range(len(names)):
        print(names[k])
