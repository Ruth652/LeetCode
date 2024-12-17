class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack=[]
        for i in range(len(asteroids)):
            if not stack:
                stack.append(asteroids[i])
            elif asteroids[i]*stack[-1]>0:
                stack.append(asteroids[i])
            elif asteroids[i]>0 and stack[-1]<0:
                stack.append(asteroids[i])
            elif abs(asteroids[i])<abs(stack[-1]):
                 continue
            elif abs(asteroids[i])>abs(stack[-1]):
                        while stack and abs(asteroids[i])>stack[-1]and asteroids[i]*stack[-1]<0 and asteroids[i]<0:
                                   stack.pop()
                        if not stack or asteroids[i]*stack[-1]>0:
                            stack.append(asteroids[i])
                        elif abs(stack[-1])==abs(asteroids[i]):
                            stack.pop()
                                  
                       
            elif abs(asteroids[i])==abs(stack[-1]):
                    stack.pop()
        return stack
                
                 
                