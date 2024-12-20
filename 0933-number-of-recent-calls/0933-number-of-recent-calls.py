class RecentCounter(object):

    def __init__(self):
        self.queue=[]
        self.result=0
    

    def ping(self, t):
                self.queue.append(t)
                while self.queue:
                    if self.queue[0]>=t-3000 :
                        self.result=len(self.queue)
                        break
                    else:
                        self.queue.pop(0)
                return self.result
                
            
    
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)