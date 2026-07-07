class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for word in strs:
            n = len(word)
            encoded.append(f"{len(word)}#{word}")
        return "".join(encoded)

       
    
        

     

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0 

        
        while i < len(s):
            
            #finding position #
            j = i

            while s[j] != '#':
                j += 1

            #Length of str 
            l = int(s[i:j])

            #extracting word
            word = s[j+1:j+1+l]
            decoded.append(word)

            #Move to the next encoded word
            i = j+1+l
        
        return decoded

        

            


        
