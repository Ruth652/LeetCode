class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        numsList=list(map(str,nums))
        for i in range(len(numsList)):
            for j in range(len(numsList)-1):
                       if(numsList[j]+numsList[j+1]<numsList[j+1]+numsList[j]):
                           numsList[j],numsList[j+1]=numsList[j+1],numsList[j]
    
                       
        
        result=''.join(numsList)
        if result[0]=="0":
            return "0"
        else:
            return result
         
                       
                       
                       
                       
                       
                       