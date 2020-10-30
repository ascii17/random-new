from collections import defaultdict

def addEdge(g, u, v):
    g[u].append(v)

def helper(v, black, gray):
    black[v] = True
    gray[v] = True

    for neigh in g[v]:
        if black[neigh] == False:
            if helper(neigh, black, gray):
                return True
        elif gray[neigh] == True:
            global ans
            ans = neigh
            return True
        
    gray[neigh] = False
    return False
    

def detectCycle(res):
    for i in range(len(res)):
        black, gray = [False]*len(res), [False]*len(res)
        helper(i, black, gray)
        global ans
        res[i] = ans+1
        ans = -1

n = int(input())
arr = list(map(int, input().split()))
g = defaultdict(list)

for i in range(len(arr)):
    addEdge(g,i,arr[i]-1)

#print (g)
#exit ()

ans = -1
res = [False] * len(arr)
detectCycle(res)
print (' '.join([str(i) for i in res]))

