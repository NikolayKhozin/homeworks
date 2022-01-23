
import math

# 1
item_1 = 10

# 2
item_2 = 20
# 3
result_sum = item_1 + item_2
print(result_sum)
#
result_subtr = item_1 - item_2
print(result_subtr)
#
result_multi = item_1 * item_2
print(result_multi)
#
result_exp = item_1 ** item_2
print(result_exp, type(result_exp))

result_m_exp = math.pow(item_1, item_2)
print(result_m_exp)
# 11,12

result_s_root = item_1 ** 0.5
print(result_s_root)
# 13,14

result_m_s_root = math.sqrt(item_1)
print(result_m_s_root)
# 15,16

result_mp_s_root = math.pow(item_1,1 / 2)
print(result_mp_s_root)

# odd нечетный, even четный
item_1 = 3
item_2 = 6
result_division = item_1 / item_2
print(result_division)
# 21,22

result_m_floor = math.floor(result_division)
print(result_m_floor)
# 23,24

result_m_ceil = math.ceil(result_division)
print(result_m_ceil)
# 25,26

result_int = int(result_division)
print(result_int)
# 27,28

result_no_division_loss = item_1 // item_2
print(result_no_division_loss)
# 29,30
item_1 = 7
item_2 = 2
result_division_loss = item_1 % item_2
print(result_division_loss)
# 31,32

item_3 = 5
item_3 = item_3 + 10
print(item_3)
# 33,34,35

item_3 = item_3 - 5
print(item_3)
# 37

item_3 = item_3 * 3
print(item_3)
# 39

item_3 = item_3 / 2
print(item_3)
# 41

item_3 = item_3 ** 2
print(item_3)
# 43

item_3 = item_3 ** 0.5
print(item_3)
# 45

item_3 = item_3 % 2
print(item_3)
# 47
# boolean

b_item_t = True
b_item_f = False
b_item_result_sum = bool (b_item_t + b_item_f)
print(b_item_result_sum)
# 51

b_item_relult_subtr =bool (b_item_t - b_item_f)
print(b_item_relult_subtr)
# 53
b_item_relult_multi = bool (b_item_t * b_item_f)
print(b_item_relult_multi)
# 55

# b_item_relult_division = b_item_t / b_item_f
# print(b_item_relult_division)
# 57

b_item_1_int = int(b_item_t)
print(bool(b_item_1_int))
# 59

b_item_2_int = int(b_item_f)
print(b_item_2_int)
