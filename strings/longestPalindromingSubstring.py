
''' 
	LONGEST PALINDROMIC SUBSTRING
	_____________________________

	Problem : Given a string s, find the longest substring of that string s which is also a palindrome

	Example : "banana" -> "anana" , "million" -> "illi" 

'''

def longestPalindromicSubstring(string):
	answers = []
	for i in range(len(string)):
		first = second = third = string[i]	
		if i-1 >= 0 and string[i-1] == string[i]:
			first = expand(string, i-1, i)
		elif i+1<=len(string) -1  and string[i + 1] == string[i]:
			second = expand(string,i,i+1)
		
		third = expand(string,i,i)
		answers.append(max([first,second,third], key = len))
	print(answers)	
	return max(answers, key = len)


def expand(string, beg, end):
	beg -= 1
	end += 1
	while beg >= 0 and end <= len(string) - 1: 
		if string[beg] == string[end]:
			beg -= 1
			end += 1
		else:
			break

	return string[beg + 1 : end]	


print(longestPalindromicSubstring("banana"))
print(longestPalindromicSubstring("million"))


