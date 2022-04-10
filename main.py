# coding: utf-8
import copy

def print_with_argument_name(argment_name, argment):
    print('{}: '.format(argment_name) + str(argment))


# これはどうなる？
a = 1
b = a
b = 5

print('intのaとbの比較')
print_with_argument_name('a', a)
print_with_argument_name('b', b)
print('\n')

# 出力結果
# a: 1
# b: 5


# では、これは？
c = [1, 2, 3]
d = c
d[0] = 100

print('listのcとdの比較')
print_with_argument_name('c', c)
print_with_argument_name('d', d)
print('\n')

# 出力結果
# c: [100, 2, 3]
# d: [100, 2, 3]

# 整数はイミュータブル(immutable）
# 値を変更できない
# 人間から見ると値が変わったように見えているが、実態は新しいオブジェクトを生成して代入されている
# つまり、コピーされているわけではない

# listはミュータブル（mutable）
# 値を変更できる
# https://docs.python.org/ja/3/reference/datamodel.html?highlight=mutable


# idは固有の識別子を判定する
# 別々のidであることがわかる
print('intのaとbのidの比較')
print_with_argument_name('id(a)', id(a))
print_with_argument_name('id(b)', id(b))
print('listのcとdのidの比較')
print_with_argument_name('id(c)', id(c))
print_with_argument_name('id(d)', id(d))
print('\n')


# こういった挙動を知らないとどういう落とし穴があるか
# 途中で意図せずに値が切り替わってしまう

# リストは以下のような構造と仮定する
# [int, str, int]
# [No, 名前, フラグ]
base_data_list = [
    [1, 'PHP', 1],
    [2, 'Python', 1],
    [3, 'Perl', 0],
    [4, 'Ruby', 1]
]

# リストから特定のフラグとなる値がある場合、削除するメソッド
def make_prefix_p_langeage_list(data_list):
    for i in data_list:
        IS_PREFIX_P_LANGUAGE = i[2]
        if not IS_PREFIX_P_LANGUAGE:
            data_list.remove(i)
    return data_list

# 以下はどのようになるか？
print('make_prefix_p_langeage_listの結果とbase_data_listの比較')
print_with_argument_name(
    'make_prefix_p_langeage_list(base_data_list)', make_prefix_p_langeage_list(base_data_list))
print_with_argument_name(
    'base_data_list', base_data_list)
print('\n')

# 出力結果
# make_prefix_p_langeage_list(base_data_list): [[1, 'PHP', 1], [2, 'Python', 1], [4, 'Ruby', 1]]
# base_data_list: [[1, 'PHP', 1], [2, 'Python', 1], [4, 'Ruby', 1]]

# 元のlistも書き変わっている・・・
# これはPythonが「オブジェクトへの参照渡し」を行っているから
# （Pythonとしては「値渡し」ただし、値=オブジェクトの参照となる。オブジェクトの値そのものを渡していない）
# Pythonにはすべてがクラスという考え方があるが、これはまた別の機会に説明するかも・・・

# https://docs.python.org/ja/3/tutorial/controlflow.html?highlight=if#id1
# https://pythonmaniac.com/call-by-value-or-reference/
# https://teratail.com/questions/273295?link=qa_related_sp

# では具体的に中身を見てみる

base_data_list = [
    [1, 'PHP', 1],
    [2, 'Python', 1],
    [3, 'Perl', 0],
    [4, 'Ruby', 1]
]

print('make_prefix_p_langeage_list, base_data_listのid')
print_with_argument_name(
    'id(make_prefix_p_langeage_list(base_data_list))', id(make_prefix_p_langeage_list(base_data_list)))
print_with_argument_name(
    'id(base_data_list)', id(base_data_list))
# 出力結果
# id(make_prefix_p_langeage_list(base_data_list)): 22558621171648
# id(base_data_list): 22558621171648

# 同じidを返却していることがわかる


# ではどうすれば良いか？
# copyした値を渡す

print('copyした値を渡す')
base_data_list = [
    [1, 'PHP', 1],
    [2, 'Python', 1],
    [3, 'Perl', 0],
    [4, 'Ruby', 1]
]
print_with_argument_name(
    'make_prefix_p_langeage_list(copy_data_list)', make_prefix_p_langeage_list(base_data_list.copy()))
print_with_argument_name(
    'base_data_list', base_data_list
)
print('\n')
# 出力結果
# make_prefix_p_langeage_list(copy_data_list): [[1, 'PHP', 1], [2, 'Python', 1], [4, 'Ruby', 1]]
# base_data_list: [[1, 'PHP', 1], [2, 'Python', 1], [3, 'Perl', 0], [4, 'Ruby', 1]]

# idも確認してみる
print('idも確認してみる')
print_with_argument_name(
    'id(base_data_list)', id(base_data_list)
    )
print_with_argument_name(
    'id(copy_data_list)', id(base_data_list.copy())
    )

# 出力結果
# id(base_data_list): 23352490950336
# id(copy_data_list): 23352490963008
# 違うことがわかった！

