class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        answer = ""
        min_length = 200
        for word in strs:
            min_length = min(min_length, len(word))
        status_flag = True
        for i in range(min_length):
            curr = strs[0][i]
            for j in range(len(strs)):
                if strs[j][i] != curr:
                    status_flag = False
                    break  # Add break to exit inner loop when a difference is found
            if not status_flag:
                break
            answer += curr
        return answer  # Add return statement at the end
