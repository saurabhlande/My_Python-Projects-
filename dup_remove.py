list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

alist=[]
for i in list:
    if i not in alist:
        alist.append(i)
alist=list
print(alist)

# print(list(set(duplicate)))
#
#
# write a program tack number from user and conver into roman equivalent
# a = input("enter no.")
#     def int_to_Roman(self, num):
#         val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
#         syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
#         roman_num = ''
#         i = 0
#         while num > 0:
#             for _ in range(num // val[i]):
#                 roman_num += syb[i]
#                 num -= val[i]
#             i += 1
#         return roman_num
#
#
# print(int_to_Roman().int_to_Roman(1))

