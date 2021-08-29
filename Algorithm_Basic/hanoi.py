def hanoi(n, a, b, c): #a是起点，c是终点，b是中转点，n是需要转移的数量
    if n>0:
        hanoi(n-1, a, c, b) #前n-1个从a经过c移动到b
        print("moving from %s to %s" %(a,c)) #第n个从a移动到c
        hanoi(n-1, b, a, c) #前n-1个从b经过a移动到c

if __name__ == '__main__':
    hanoi(4,'A','B','C')