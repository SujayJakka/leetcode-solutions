class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapThing = {}

        def findAnagranArray(w):
            array = [0] * 26

            for c in w:
                array[ord(c) - 97] += 1
            
            tupleThing = tuple(array)

            arrayThing = mapThing.get(tupleThing, [])
            arrayThing.append(w)
            mapThing[tupleThing] = arrayThing

        for w in strs:
            findAnagranArray(w)
        
        return mapThing.values()
