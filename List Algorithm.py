class search:
    """
    对数字列表的索引值查找
    1. linear_search 线性查找
    2. binary_search 二分查找
    """
    @staticmethod
   
    def linear_search(li:list = None,val:int = None) -> int:
        """
        线性查找[O(n)]
        列表可无序,不需要创建实例
        参数：
            li : 列表
            val : 目标值
        返回：
            val所在li中的索引值,如果未找到返回None
        """
        for ind, v in enumerate(li):
            if v == val:
                return(ind)
            

        return(None)
            
    def binary_search(li:list = None,val:int = None,sequence:str = "S") -> int:
        """
        二分查找[O(logn)]
        列表需排序，不需要创建实例
        默认正序列表查找(S)
        参数：
            li : 列表
            val : 目标值
            sequence : 列表顺序
                正序搜索: S(Sure);倒序搜索: O(Opposite) 
        返回：
            val所在li中的索引值,如果未找到返回None
        """
        
        left = 0
        right = len(li) - 1
        while left <= right:
            mid = (left + right) // 2
            if li[mid] == val:
                return(mid)
            
            if sequence.upper() == "S":
                if li[mid] > val:
                    right = mid - 1
                else:
                    left = mid + 1

            elif sequence.upper() == "O":
                if li[mid] > val:
                    left = mid + 1
                else:
                    right = mid - 1

            else:
                return(None)
            
        return(None)


class sort:
    """
    对数字列表的排序处理
    1. bubble_sort 泡泡排序
    2. select_sort 选择排序
    3. insert_sort 插入排序
    """
    @staticmethod

    def bubble_sort(li:list,sequence:str = "S") -> list:
        """
        冒泡排序[O(n)]
        直接调用，不需要创建实例
        默认正序排序列表(S)
        参数：
            li : 列表
            sequence : 列表排序顺序
                正序排列: S(Sure);倒序排列: O(Opposite) 
        返回：
            将原列表排序后,返回排序后的列表
        (原列表被排序)
        """
        if sequence.upper() == "S":
            exchange= False
            for i in range(len(li) - 1):
                for j in range(len(li) - i - 1):
                    if li[j] > li[j + 1]:
                        li[j], li[j + 1] = li[j + 1], li[j]
            
            if not exchange:
                return(li)

        elif sequence.upper() == "O":
            exchange = False
            for i in range(len(li) - 1):
                for j in range(len(li) - i - 1):
                    if li[j] < li[j + 1]:
                        li[j], li[j + 1] = li[j + 1], li[j]
                        exchange = True

            if not exchange:
                return(li)


    def select_sort(li:list,sequence:str = "S") -> list:
        pass
        """
        选择排序[O(n²)]
        直接调用，不需要创建实例
        默认正序排序列表(S)
        参数：
            li : 列表
            sequence : 列表排序顺序
                正序排列: S(Sure);倒序排列: O(Opposite) 
        返回:
            将原列表排序后,返回排序后的列表
        (原列表被排序)
        
        """
        if sequence.upper() == "S":
            for i in range(len(li) - 1):
                min_loc = i
                for j in range(i + 1, len(li)):
                    if li[j] < li[min_loc]:
                        min_loc = j
                li[i], li[min_loc] = li[min_loc], li[i]
                print(li)
            return(li)
        
        elif sequence.upper() == "O":
            for i in range(len(li) - 1):
                min_loc = i
                for j in range(i + 1, len(li)):
                    if li[j] > li[min_loc]:
                        min_loc = j
                li[i], li[min_loc] = li[min_loc], li[i]
                print(li)
            return(li)

    def insert_sort(li:list,sequence:str = "S") -> list:
        pass
        """
        插入排序[O(n²)]
        直接调用，不需要创建实例
        默认正序排序列表(S)
        参数：
            li : 列表
            sequence : 列表排序顺序
                正序排列: S(Sure);倒序排列: O(Opposite) 
        返回:
            将原列表排序后,返回排序后的列表
        (原列表被排序)
        
        """
        if sequence.upper() == "S":
            for i in range(1, len(li)):
                tmp = li[i]
                j = i - 1
                while j >= 0 and li[j] > tmp:
                    li[j + 1] = li[j]
                    j = j - 1
                li[j + 1] = tmp
            return(li)

        elif sequence.upper() == "O":
            for i in range(1, len(li)):
                tmp = li[i]
                j = i - 1
                while j >= 0 and li[j] < tmp:
                    li[j + 1] = li[j]
                    j = j - 1
                li[j + 1] = tmp
            return(li)



import random

axx = [8,5,3,7,6,4,1,2,0,9]
ass = list(range(100000))
add = list(range(100000))
random.shuffle(ass)


print(axx)
sort.insert_sort(axx,"s")
print(axx)
sort.insert_sort(axx,"o")
print(axx)
