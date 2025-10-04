#Problem: https://leetcode.com/problems/shortest-distance-to-a-character/

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        #primeiro, verificar todos os índices onde c aparece
        positions = []
        for i in range(len(s)):
            if s[i] == c:
                positions.append(i)

        #segundo, calcular a menor distância para cada índice em relação a c
        answer = []

        for i in range(len(s)):
            minor = 10000
            for positionC in positions:
                if i >= positionC:
                    distance = i - positionC
                else:
                    distance = positionC - i
                if distance < minor:
                    minor = distance
            answer.append(minor)

        return answer

