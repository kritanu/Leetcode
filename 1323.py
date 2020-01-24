class Solution:
    def maximum69Number (self, num: int) -> int:
        num_list = [x for x in str(num)]
        for i in range (len(num_list)):
            if(num_list[i] == '6'):
                num_list[i] = '9'
                break
        output = (''.join(num_list))
        return output