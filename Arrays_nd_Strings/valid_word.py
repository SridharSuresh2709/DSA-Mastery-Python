class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        vowel_count = 0
        consonant_count = 0
        vowels = set(['a','e','i','o','u','A','E','I','O','U'])
        # minimum of 3 characters
        if len(word)>=3:
            if word.isalnum():
                for s in word:
                    if s in vowels:
                        vowel_count += 1
                    elif s not in vowels and s.isalpha():
                        consonant_count += 1
            else:
                return False
        else:
            return False
        
        if vowel_count>=1 and consonant_count>=1:
            return True
        else:
            return False


        