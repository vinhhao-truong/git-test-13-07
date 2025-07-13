def total_ord(string):
    if string == "":
        return 0
    return ord(string[0]) + total_ord(string[1:len(string)])


# def str_diff(s1, s2):
#     ord1 = total_ord(s1)
#     ord2 = total_ord(s2)
#     if ord2 - ord1 == 1:
#         return "No such string"

#     last_ord = ord(s1[len(s1) - 1])
#     last_acp = chr(last_ord + 1)

#     if len(s1) == 1:
#         return last_acp

#     return s1[0:len(s1) - 1] + last_acp

def str_diff(s1, s2):
    ord1 = total_ord(s1)
    ord2 = total_ord(s2)
    ord_diff = ord2 - ord1
    if ord_diff == 1:
        return "No such string"
    for i in reversed(range(len(s1))):
        ord_diff -= 1
        this_ord1 = ord(s1[i])
        this_ord2 = ord(s2[i])
        if this_ord1 == this_ord2:
            result = chr(this_ord1) + result
            continue
        result = chr(this_ord1 + 1) + result
    return result


s = input()
t = input()

# print(str_diff(s, t))
print(str_diff(s, t))
