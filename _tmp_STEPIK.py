def s(a, *vs, b=10):
   res = a + b
   print(vs)
   for v in vs:
       res += v
   return res
# print(s(0, 0, 31))

def fibo(k):
    sum = 0
    if (k == 0) or (k == 1):
        return 1
    else:
        return fibo(k-1) + fibo(k-2)
# print(fibo(6))

n, k = map(int, input().split())

def cnk(n, k):
    if k > n:
        return 0
    if k == 0:
        return 1
    else:
        return cnk(n-1, k) + cnk(n-1,k-1)


print(cnk(n, k))