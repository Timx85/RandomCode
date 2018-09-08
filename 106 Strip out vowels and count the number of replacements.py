text = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
vowels = 'aeiou'


def strip_vowels(text=text):
    """Replace all vowels by *, return newly formed string
       and number of replacements done"""
    NumberOfVowels = 0
    textNew = []
    chars = list(text)

    for c in chars:
        if c.lower() in vowels:
            c = '*'
            NumberOfVowels += 1
        textNew.append(c)

    return ''.join(textNew),NumberOfVowels

import re
def strip_vowelsV2(text=text):
    return re.subn(f'[{vowels}]', '*', text, flags=re.I)

print(strip_vowels(text))
print(strip_vowelsV2(text))