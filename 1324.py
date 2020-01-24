class Solution:
    def printVertically(self, s: str) -> List[str]:
    	bag_of_words = s.split(' ')
    	max_len = len(max(bag_of_words, key=len)) #Finding length of max length str in list
    	new_bag = list()
    	new_word = list()
    	for word in bag_of_words:
    		for i in range(max_len):
    			try:
    				new_word.append(word[i])
    			except IndexError:
    				new_word.append(' ')
    			except ValueError:
    				new_word.append(' ')
    		new_bag.append(''.join(new_word))
    		new_word.clear()
    	answer_word = []
    	answer_bag = []
    	for j in range(max_len):
    		for k in range(len(new_bag)):
    			answer_word.append(new_bag[k][j])
    		answer_bag.append(''.join(answer_word).rstrip())
    		answer_word.clear()
    	return answer_bag