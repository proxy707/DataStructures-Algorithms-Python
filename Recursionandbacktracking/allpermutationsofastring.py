def listToString(arr):
    return ''.join(arr)

def permute(a,l,r):
    if l==r:
        print(listToString(a))
    else:
        for i in range(l,r+1):
            a[l],a[i]  = a[i],a[l]
            permute(a,l+1,r)
            a[l],a[i]  = a[i],a[l] # backtrack
            
t = int(input())
while t:
    s = str(input())
    permute(list(s),0,len(s)-1)
    
