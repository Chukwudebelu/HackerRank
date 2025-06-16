#!/bin/python3
# Without using the Regex Module!
# Enter your code here. Read input from STDIN. Print output to STDOUT


if __name__ == "__main__":
    N = int(input().strip())
    
    for _ in range(N):
        cCN = input()
        
        if cCN.isdigit():
            islength = True if len(cCN) == 16 else False
            
            is456 = bool(1 if cCN[0] == '4' or cCN[0] == '5' or cCN[0] == '6' else 0)
            
            resp = 'Valid' if (islength and is456) else 'Invalid'
            print(resp); continue
                
        elif cCN.__contains__('-'):
            if cCN.count('-') == 3:
                is456 = bool(1 if cCN[0] == '4' or cCN[0] == '5' or cCN[0] == '6' else 0)
                
                if cCN[4] == '-' and cCN[9] == '-' and cCN[14] == '-':
                    isHyphen = True
                else:
                    isHyphen = False
                    
                cCN = cCN.replace('-','')
                islength = True if len(cCN) == 16 and cCN.isdigit() else False
                
                for i in range(len(cCN)-4+1):
                    if cCN[i] == cCN[i+1] == cCN[i+2] == cCN[i+3]:
                        isRepeated4X = True
                        break
                    else:
                        isRepeated4X = False
                
                resp = 'Valid' if (is456 and isHyphen and islength and not isRepeated4X) else 'Invalid'
                print(resp); continue
            else:
                print('Invalid'); continue

        elif cCN.__contains__(' ') or cCN.__contains__('_'):
            print('Invalid'); continue
