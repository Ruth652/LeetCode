class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
      
        name = [""] * len(names)
        h1 = heights[:]
        

        maximum = max(heights)
        count = [0] * (maximum + 1)
        
    
        for height in heights:
            count[height] += 1
        
      
        target = 0
        for index, value in enumerate(count):
            for i in range(value):
                heights[target] = index
                target += 1
        
     
        for i in range(len(heights)):
            for j in range(len(heights)):
                if h1[i] == heights[j]:
                    if name[j]!=names[i]:
                        name[j] = names[i]
                    else:
                        name[j+1]=names[i]
                
        
   
        name.reverse()
        return name

        
                    
                 
         