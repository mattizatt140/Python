def fibonacci(n, d):
   if n in d:
        return d[n]
   else:
       ans = fibonacci(n-1, d) + fibonacci(n - 2, d)
       d[n] = ans
       return ans

d = {1:1, 2:2}
fibonacci(1000, d)
print(d[1000])