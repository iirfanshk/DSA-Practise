import sys

def solveCircularCandyPassing(n, m, passes):
    current = 1
    for p in passes:
        if p < 0:
            return -1
        current = (current-1+p) % n+1
    return current
    
    

def main():
    data = list(map(int, sys.stdin.read().strip().split()))

    n = data[0]
    m = data[1]
    passes = data[2:2 + m]

    result = solveCircularCandyPassing(n, m, passes)
    print(result)

if __name__ == "__main__":
    main()

