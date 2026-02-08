"""
·List Algorithm v1.0
- 加入线性查找
- 加入二分查找
- 加入冒泡排序
- 加入选择排序
- 加入插入排序

·List Algorithm v1.1
更新内容：
- 快速排序基础版本
- 快速排序三数取中优化版
- 修复冒泡排序退出条件
- 修复部分注释
- 每个代码加入静态运行
"""




class search:
    """
    对数字列表的索引值查找
    1. linear_search 线性查找
    2. binary_search 二分查找
    """
    @staticmethod
   
    def linear_search(li:list = None, val:int = None) -> int:
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

    @staticmethod        
    def binary_search(li:list = None, val:int = None, sequence:str = "S") -> int:
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
    1. bubble_sort 冒泡排序
    2. select_sort 选择排序
    3. insert_sort 插入排序
    4. partition_M 归为函数-基础(_quick_sort 自定义快速排序前置)
    5. median_of_three 三数取中(partition_S 归为函数-三数取中前置)
    6. partition_S 归为函数-三数取中(_quick_sort 自定义快速排序前置)
    7. _quick_sort 自定义快速排序-基础
    8. quick_sort 快速排序-三数取中
    """
    @staticmethod
    def bubble_sort(li:list, sequence:str = "S") -> list:
        """
        冒泡排序[O(n²)]
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
            for i in range(len(li) - 1):
                exchange= False
                for j in range(len(li) - i - 1):
                    if li[j] > li[j + 1]:
                        li[j], li[j + 1] = li[j + 1], li[j]
                        exchange = True
                if not exchange:
                    break
            return(li)

        elif sequence.upper() == "O":
            for i in range(len(li) - 1):
                exchange = False
                for j in range(len(li) - i - 1):
                    if li[j] < li[j + 1]:
                        li[j], li[j + 1] = li[j + 1], li[j]
                        exchange = True
                if not exchange:
                    break
            return(li)
                
    @staticmethod
    def select_sort(li:list, sequence:str = "S") -> list:
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

    @staticmethod
    def insert_sort(li:list, sequence:str = "S") -> list:
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

    @staticmethod
    def partition_M(li:list, left:int, right:int, sequence:str = "S"):
        """
        归位函数-基础(快速排序的前置函数)
        参数：
            li : 列表
            left :列表起始位置
            right : 列表结束位置
        输出:
            空
        注意:递归默认深度有限！
        """
        if sequence.upper() == "S":
            temp = li[left]
            while left < right:
                while left < right and li[right] >= temp:
                    right -= 1
                li[left] = li[right]
                while left < right and li[left] <= temp:
                    left += 1
                li[right] = li[left]
            li[left] = temp
            return(left)
        

        elif sequence.upper() == "O":
            temp = li[left]
            while left < right:
                while left < right and li[right] <= temp:
                    right -= 1
                li[left] = li[right]
                while left < right and li[left] >= temp:
                    left += 1
                li[right] = li[left]
            li[left] = temp
            return(left)

    @staticmethod    
    def median_of_three(li:list, left:int, right:int) -> int:
        mid = (left + right) // 2
        a = li[left]
        b = li[mid]
        c = li[right]
        if a < b < c or c < b < a:
            return(mid)
        elif b < a < c or c > a > b:
            return(left)
        else:
            return(right)

    @staticmethod
    def partition_S(li:list, left:int, right:int, sequence:str = "S"):
        """
        归位函数-三数取中(快速排序-快速排序前置函数)
        参数：
            li : 列表
            left :列表起始位置
            right : 列表结束位置
        输出:
            空
        注意:递归默认深度有限！
        """
        idx = sort.median_of_three(li, left, right)
        li[idx], li[left] = li[left], li[idx]
        
        if sequence.upper() == "S":
            temp = li[left]
            while left < right:
                while left < right and li[right] >= temp:
                    right -= 1
                li[left] = li[right]
                while left < right and li[left] <= temp:
                    left += 1
                li[right] = li[left]
            li[left] = temp
            return(left)
        

        elif sequence.upper() == "O":
            temp = li[left]
            while left < right:
                while left < right and li[right] <= temp:
                    right -= 1
                li[left] = li[right]
                while left < right and li[left] >= temp:
                    left += 1
                li[right] = li[left]
            li[left] = temp
            return(left)

    @staticmethod
    def _quick_sort(li:list, left:int, right:int, sequence:str = "S") -> list :
        """
        自定义快速排序-基础[O(n·logn)]
        此为自定义函数,需要传入开头和结尾
        需要前置函数partitiong_M
        直接调用，不需要创建实例
        默认正序排序列表(S)
        参数：
            li : 列表
            sequence : 列表排序顺序
                正序排列: S(Sure);倒序排列: O(Opposite) 
        返回：
            将原列表排序后,返回排序后的列表
        (原列表被排序)
        注意:递归默认深度有限！
        """
        if left < right:
            mid = sort.partition_M(li, left, right, sequence)
            sort._quick_sort_M(li, left, mid - 1, sequence)
            sort._quick_sort_M(li, mid + 1, right, sequence)
        return(li)

    @staticmethod
    def quick_sort(li:list, sequence:str = "S") -> list :
        """
        快速排序-三数取中[O(n·logn)]
        此为默认函数,默认列表开头和结尾
        需要前置函数partitiong_S
        直接调用，不需要创建实例
        默认正序排序列表(S)
        参数：
            li : 列表
            sequence : 列表排序顺序
                正序排列: S(Sure);倒序排列: O(Opposite) 
        返回：
            将原列表排序后,返回排序后的列表
        (原列表被排序)
        注意:递归默认深度有限！
        """
        left= 0
        right = len(li) - 1 
        if left < right:
            mid = sort.partition_S(li, left, right, sequence)
            sort._quick_sort_S(li, left, mid - 1, sequence)
            sort._quick_sort_S(li, mid + 1, right, sequence)
        return(li)
    







import random

axx = [8,5,3,7,6,4,1,2,0,9]
ass = list(range(100000))
add = list(range(100000))
random.shuffle(ass)


print(axx)
sort.quick_sort(axx,"S")
print(axx)
sort.quick_sort(axx,"O")
print(axx)
