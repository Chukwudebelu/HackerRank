# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath

if __name__ == "__main__":
    z = complex(input())
    
    r = abs(z)
    phi = cmath.phase(z)
    
    print(F'{r:.3f}\n{phi:.3f}')
