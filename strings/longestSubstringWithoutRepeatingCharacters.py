'''
	Longest Substring without Repeating Characters:
	
	Problem : Given a string, find the longest substring of that string that does not contain any repeating characters

	e.g. abrkaabcdefghijjxxx -> "abcdefghij", which has a length of 10. 


'''





def longestSubstring(string):
	hashMap = {}
	answer = []
	beginning = 0
	for i in range(len(string)):
		if string[i] in hashMap and hashMap[string[i]] > beginning:
			beginning = hashMap[string[i]] + 1
			answer.append(i - beginning + 1)
			hashMap[string[i]] = i 
		else:
			hashMap[string[i]] = i 
			answer.append(i - beginning + 1)
	print(answer)
	return max(answer)


#Testing Output with Code
word = 'abrkaabcdefghijjxxx' 
print(longestSubstring(word))	


'''

	Time Complexity: O(n)
	Space Complexity: O(n)

'''
