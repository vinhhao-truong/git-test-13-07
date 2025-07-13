import resource
import sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10**6)


def greatest_common_divisor(a, b, c):
    if a == b:
        return a

    if b % a == 0:
        return a

    if a % c == 0 and b % c == 0:
        return c

    if a % c == 0 and b % c == 0:
        return c

    return greatest_common_divisor(a, b, c - 1)


n = list(map(int, input().split()))

is_a_sm = n[0] <= n[1]

if is_a_sm:
    print(greatest_common_divisor(n[0], n[1], n[0]))
else:
    print(greatest_common_divisor(n[1], n[0], n[1]))
