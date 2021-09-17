
test = [6, 4, 3, 7, 2, 1, 5]

def insertion(test):
    """
        插入排序
            从左到右，left-->index-1已排好序,index-->right未排序
            每次选取index的元素，插入到[left, index-1]中
            index依次与前面的元素比较，若小则交换，若大则找到位置，交换即可
    """
    length = len(test)
    for i in range(1, length):
        j = i 
        while (j>0 and test[j] < test[j-1]):
            swap(test, j - 1, j)
            j -= 1
    return test


def swap(test, x, y):
    temp = test[x]
    test[x] = test[y]
    test[y] = temp

print(insertion(test))

