#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value=''):
        self.value = value if isinstance(value, str) else ''
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")
            self._value = ''

    def is_sentence(self):
        return self.value.endswith('.')
    
    def is_question(self):
        return self.value.endswith('?')
    
    def is_exclamation(self):
        return self.value.endswith('!')
    
    def count_sentences(self):
        # Replace all multiple punctuation with a single period for uniformity
        cleaned_value = re.sub(r'[.!?]+', '.', self.value)
        # Split the string into potential sentences
        sentences = cleaned_value.split('.')
        # Filter out empty strings from the resulting list
        sentences = [s for s in sentences if s.strip()]
        return len(sentences)


string = MyString()
string.value = "This is a string! It has three sentences. Right?"
print(string.is_sentence())      # Output: False
print(string.is_question())      # Output: True
print(string.is_exclamation())   # Output: False
print(string.count_sentences())  # Output: 3
