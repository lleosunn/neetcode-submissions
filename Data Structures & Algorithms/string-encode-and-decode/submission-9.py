s = "fdsafdjksla;fjkdsa,fdjskal;fjdskl;a"
l, r = s.split(",", maxsplit=1)
print(l, r)

class Solution:

    def encode(self, strs: List[str]) -> str:
        # encode them by combining all the strings
        # first character is a number that determines the length of the next string
        # to mark the end of the number, we add a marker " "
        # length, marker, string, length, marker, string
        out = ""
        for string in strs:
            out += str(len(string)) + "," + string
        # print("encode: ", out)
        return out

    def decode(self, s: str) -> List[str]:
        # get the length, start counting after the marker, only count for length, repeat
        out = []
        while s:
            l, s = s.split(",", maxsplit=1)
            
            out += s[:int(l)]
            s = s[int(l):]
        return out

        
# def getLength(string):
#     # given any string, return the number that starts at the beginning of the string and ends with a space
#     out = ""
#     for c in string:
#         if c == " ":
#             return int(out)
#         out += "c"


