class Codec:

    def __init__(self) -> None:
        self.mapThing = {}

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """

        res = ""

        for word in strs:
            for c in word:
                if c not in self.mapThing:
                    self.mapThing[str(ord(c))] = c
                res += str(ord(c))
                res += ","
            res += "/"
        return res
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """

        myArray = s.split("/")
        myArray.pop()
        res = []

        current = ""
        for stringThing in myArray:
            temp = stringThing.rstrip(",").split(",")

            for c in temp:
                if c == "":
                    continue
                current += self.mapThing[c]
            res.append(current)
            current = ""
        return res
            
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
