class Anagram:
    def __init__(self,word):
        self._word = word
    
    def match(self,words):
        if(not words):
            return []
        else:
            allmatches = []
            self._words = words
            
            for word in self._words:
                if len(word) == len(self._word):
                    count = 0
                    while(count!=len(word)):
                        if(word.count(word[count]) == self._word.count(word[count])):
                            print(word[count])
                            count = count + 1
                        else:
                            break
                    if(count == len(word)):
                        allmatches.append(word)
            return allmatches


an = Anagram("hello")
print(an.match(["elloh","hi","lol","holle"]))