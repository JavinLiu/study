test = [6, 4, 3, 7, 2, 1, 5]


def selection(test):
    """
        选择排序
        从第一个数开始，依次与后面的数进行比较，选择最小的数放到第一个位置。
        test为长为n的随机序列，i=0,1,...,n-1,每次对比n-i次，找到最小的元素，放到i的位置
        即每轮可以找到一个最小的元素放置其最终位置
        供需进行n-1轮，每轮比较n-1次，交换1次位置

    """
    length = len(test)
    for i in range(length):
        min = i
        for j in range(i + 1, length):
            if test[j] < test[min]:
                min = j
        swap(test, i, min)
    return test


def swap(test, x, y):
    """
        交换test中索引为x,y元素的位置
    """
    temp = test[x]
    test[x] = test[y]
    test[y] = temp


print(selection(test))
