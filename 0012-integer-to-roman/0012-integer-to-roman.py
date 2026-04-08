class Solution:
    def intToRoman(self, num: int) -> str:
        romanDict = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        s = ''

        while num > 0:

            if num > 999:
                s = s + romanDict[1000]
                num -= 1000
            elif num > 499:
                if num > 899:
                    s = s + romanDict[100] + romanDict[1000]
                    num -= 900
                else:
                    s = s + romanDict[500]
                    num -= 500
            elif num > 399:
                s = s + romanDict[100] + romanDict[500]
                num -= 400
            elif num > 99:
                s = s + romanDict[100]
                num -= 100
            elif num > 49:
                if num > 89:
                    s = s + romanDict[10] + romanDict[100]
                    num -= 90
                else:
                    s = s + romanDict[50]
                    num -= 50
            elif num > 39:
                s = s + romanDict[10] + romanDict[50]
                num -= 40
            elif num > 9:
                s = s + romanDict[10]
                num -= 10
            elif num > 8:
                s = s + romanDict[1] + romanDict[10]
                num -= 9
            elif num > 4:
                s = s + romanDict[5]
                num -= 5
            elif num > 3:
                s = s + romanDict[1] + romanDict[5]
                num -= 4
            else:
                s = s + romanDict[1]
                num -= 1
        
        return s
