class Solution:
      
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        l = len(beginWord)
       
        wordList.append(beginWord)
        mapThing = collections.defaultdict(list)

        for word in wordList:
            for i in range(l):
                mapThing[word[:i] + "*" + word[i+1:]].append(word)
        
        myQueue = [[beginWord, 1]]
        visited = set(beginWord)

        while myQueue:
            word, res = myQueue.pop(0)
            for i in range(l):
                intermediate = word[:i] + "*" + word[i+1:]
                closeWords = mapThing[intermediate]

                for closeWord in closeWords:
                    if closeWord == endWord:
                        return res + 1
                    if closeWord not in visited:
                        myQueue.append([closeWord, res + 1])
                        visited.add(closeWord)

        return 0
            



                



        
       
        


        