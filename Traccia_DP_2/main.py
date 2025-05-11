def init_func (n) :
    if n == 1 :
        return 30, [2,20,25]
    if n == 2 :
        return 10, [4,5,7,8]
    if n == 3 :
        return 100, [25,50,75]
    
    return None, None


def cut_min (l, cuts) :
    
    cuts = [0] + sorted(cuts) + [l]
    
    dp = [[0] * len(cuts) for _ in range(len(cuts))]
    for seg in range(2, len(cuts)) :
        print(f"{dp}\n\n")
        for i in range(len(cuts) - seg) :
            j = i + seg
            dp[i][j] = float("inf")
            print(f"{dp}\n\n")
            for k in range(i + 1, j) :
                dp[i][j] = min(dp[i][j], cuts[j] - cuts[i] + dp[i][k] + dp[k][j])
                print(f"{dp}\n\n")
                
    return dp[0][len(cuts)-1]
    

if __name__ == '__main__' :
    l, arr = init_func(1)
    if l is None or arr is None :
        print("<--- init error --->")
    min = cut_min(l, arr)
    print(f"Min cost : {min}")
    
    
    
    
    
    
    
