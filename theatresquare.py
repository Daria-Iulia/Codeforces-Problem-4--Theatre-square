import math

n, m, a= map(int, input() .split())

flag_l = math.ceil(n / a)

flag_w = math.ceil(m / a)

total = flag_l * flag_w

print(total)