# -*- coding: utf-8 -*-
"""
    8-10 文本处理，分辅音元音和单词数
"""

def statistics(text):
    words=text.split()
    nums=len(words)
    vowel=0
    consonant=0
    for word in words:
        word=word.lower()
        for letter in word:
            if letter in 'aeiou':
                vowel+=1
            elif letter in 'bcdfghjklmnpqrstvwxyz':
                consonant+=1
    print '单词共 %d 个,元音 %d 个，辅音 %d 个' %(nums,vowel,consonant)
    
statistics('All bananas are eated')
                