class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        number = str(x)
        number_list = []
        for i in number:
            number_list.append(i)
        number_list.reverse()
        if "".join(number_list) == number:
            return True
