class UniqueWord:
    def WordCounter(self,word: str):
        listOfWords = word.split()
        dic = {}
        for w in listOfWords:
            if w in dic:
                dic[w] = dic[w] +1
            else:
                dic[w] =1

        return dic
    
uw = UniqueWord()
print(uw.WordCounter("the cat sat on the mat the cat ran"))

class CommonElements:
    def FindCommonSorted(self,list1,list2):
        seen = set()
        duplicate1 =set()
        for var in list1:
            if var in seen:
                duplicate1.add(var)

            else:
                seen.add(var)

        for var2 in list2:
            if var2 in seen:
                duplicate1.add(var2)

            else:
                seen.add(var)
        return list(duplicate1)
    
ce = CommonElements()
print(ce.FindCommonSorted([1,2,2,3,4], [2,4,4,6]))
