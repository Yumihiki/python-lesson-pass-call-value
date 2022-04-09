# coding: utf-8

# これはどうなる？
a = 1
b = a
b = 5

print(a)
print(b)

# 出力結果
# a: 1
# b: 5


# では、これは？
c = [1, 2, 3]
d = c

d[0] = 100

print(c)
print(d)

# 出力結果
# c: [100, 2, 3]
# d: [100, 2, 3]

# リストは以下のような構造と仮定する
# [int, str, int]
# [No, 名前, フラグ]
base_data_list = [
    [1, 'PHP', 1],
    [2, 'Python', 1],
    [3, 'Perl', 0],
    [4, 'Ruby', 1]
]

def make_prefix_p_langeage_list(data_list):
    result = None
    for i in data_list:
        IS_PREFIX_P_LANGUAGE = i[2]
        if not IS_PREFIX_P_LANGUAGE:
            data_list.remove(i)
    result = data_list
    return result

make_prefix_p_langeage_list(base_data_list)

print(make_prefix_p_langeage_list(base_data_list))
print(base_data_list)

