word1 = ["ab", "c"]
word2 = ["a", "bc"]

class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        
        word1 = ''.join(word1)              #aqui lo que hacemos es usar el .join para unir las lista en una
        word2 = ''.join(word2)              # igualmente aquí
        
        if word1 == word2:                  # aqui le ponemos le condicion de si word1 es igual a word2 retorne True, si no False
            return True
        else:
            return False