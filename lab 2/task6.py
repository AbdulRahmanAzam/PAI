from functools import reduce
import math

l = [1,2,3,4,5]

res = reduce((lambda a, b: a * b), l)

res = math.prod(l)

res = eval('*'.join(map(str, l)))

print(res)
