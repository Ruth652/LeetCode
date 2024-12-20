class DataStream(object):
    def __init__(self, value, k):
        self.value = value
        self.k = k
        self.queue = []
        self.appear = 0 

    def consec(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        self.queue.append(num)  
        
       
        if num == self.value:
            self.appear += 1
        
        if len(self.queue) > self.k:
            val = self.queue.pop(0)
            if val == self.value:
                self.appear -= 1
        
    
        if len(self.queue) >= self.k and self.appear == self.k:
            return True
        
        return False



# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)