class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        aux = ""
        resp = []

        for i in digits:
            aux += str(i)
        
        aux = int(aux)
        aux += 1
        aux = str(aux)

        for i in aux:
            resp.append(int(i))

        return resp

