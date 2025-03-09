import sys

def solve():
    lines = sys.stdin.read().strip().split('\n')
    i = 0
    while i < len(lines):
        M_line = lines[i].strip()
        i += 1
        try:
            M = int(M_line)
        except ValueError:
            break
        
        coins_line = lines[i].strip().split()
        i += 1
        
        coins = []
        total = 0
        for c in coins_line:
            if c == '1':
                coins.append(1000)
                total += 1000
            else:
                coins.append(50)
                total += 50
        
        dp = 1  
        
        for val in coins:
            dp |= (dp << val)
        
        half = total // 2
        best = 0
        for s in range(half, -1, -1):
            if ((dp >> s) & 1) == 1:
                best = s
                break
        
        diff = total - 2*best
        print(diff)

if __name__ == "__main__":
    solve()
