class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        def flip(end):
            start = 0
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        result = []
        for i in range(len(arr) - 1, 0, -1):
            maxIndex = 0
            for j in range(1, i + 1):
                if arr[j] > arr[maxIndex]:
                    maxIndex = j
            if maxIndex != i:
                if maxIndex != 0:
                    flip(maxIndex)
                    result.append(maxIndex + 1)

                flip(i)
                result.append(i + 1)

        return result

                    
                    
            