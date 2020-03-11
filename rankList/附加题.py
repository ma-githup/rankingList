# 用于比较版本
def compare_version(version1,version2):
    '''
    :type version1: list
    :type version2: list
    :return: int
    '''
    v1 = version1[0]
    v2 = version2[0]
    if v1 > v2:
        return 1
    elif v1 < v2:
        return -1
    else:
        # 若此时版本列表长度都大于1，则继续递归比较
        if len(version1) > 1 and len(version2) > 1:
            return compare_version(version1[1:],version2[1:])
        # 若其中一个版本列表长度小于等于1，停止比较，取版本列表较长的版本
        elif len(version1) > len(version2):
            return 1
        elif len(version1) < len(version2):
            return -1
        # 若最终长度与数值都相同，则两个版本相同
        elif len(version1) == len(version2):
            return 0
# 用于作为map的参数
def check_zero(x):
    '''
    :type x: str
    :return: str
    '''
    if x.startswith('0'):
        x = x[1:]
        return check_zero(x)
    else:
        return x

version1 = input('请输入版本1：')
version2 = input('请输入版本2：')
# 通过高阶函数map去掉版本号的前导0
version1 = list(map(check_zero,version1.split('.')))
version2 = list(map(check_zero,version2.split('.')))
print(compare_version(version1,version2))