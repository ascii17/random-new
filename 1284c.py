n = int(input())
def checks(arr,d):
    s = 0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if (max(arr[i:j+1]) - min(arr[i:j+1])) == j-i:
                '''if (max(arr[i:j+1]) - min(arr[i:j+1])) in d:
                    d[(max(arr[i:j+1]) - min(arr[i:j+1]))]+=1
                else:
                    d[(max(arr[i:j+1]) - min(arr[i:j+1]))] = 1'''
                s+=1
    if s in d:
        d[s]+=1
    else:
        d[s] = 1
    return s

def helper(arr,i, ans,d):
    if i == len(arr):
        #print (arr[:], checks(arr))
        ans[0]+=checks(arr,d)
        return
    
    for j in range(i,len(arr)):
        arr[i], arr[j] = arr[j], arr[i]
        helper(arr, i+1, ans,d)
        arr[i], arr[j] = arr[j], arr[i]

ans = [0]
d = {}
arr = [i for i in range(1,n+1)]
helper(arr, 0, ans,d)
print (d)
print (ans[0])