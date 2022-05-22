class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictionary = {'I':'1',
                      'V':'5',
                      'X':'10',
                      'L':'50',
                      'C':'100',
                      'D':'500',
                      'M':'1000'}
        input_list=list(s)
        my_sum = 0
        for i in input_list:
            my_sum=int(dictionary[i])+my_sum


        return(my_sum)


'''
if __name__=='__main__':
    sol=Solution()
    a = sol.romanToInt("II")
    print(a)
'''