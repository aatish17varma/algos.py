def palindromicSubstrings(string):
    count = 0
    for i in range(len(string)):
        if i - 1 >= 0 and string[i] == string[i-1]:
            count += expand(string, i-1,i)
        count += expand(string,i,i)
    return count

def expand(string,beg,end):
    beg -= 1
    end += 1
    count = 0
    while beg >= 0 and end <= len(string) - 1:
        if string[beg] == string[end]:
            beg -= 1
            end += 1
            count += 1
        else:
            break
    return count + 1


print(palindromicSubstrings("abc"))
print(palindromicSubstrings("aaa"))


