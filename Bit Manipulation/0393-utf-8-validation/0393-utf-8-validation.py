class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        i = 0

        while i < len(data):
            byte = data[i]
            count = 0
            mask = 128

            while mask & byte:
                count+=1
                mask>>=1
            
            if count == 0:
                i+=1
                continue
            if i+count > len(data):
                return False
            if count == 1 or count > 4:
                return False
            
            for j in range(i+1,i+count):
                if data[j] >> 6 != 0b10:
                    return False

            i+=count
        return True
