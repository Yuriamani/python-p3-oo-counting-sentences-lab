#!/usr/bin/env python3

class MyString:
  def __init__(self, value=''):
    self.value = value

  @property
  def value(self):
    return self._value

  @value.setter
  def value(self, new_value):
    if not isinstance(new_value, str):
      print("The value must be a string.")
    else:
      self._value = new_value

  def is_sentence(self):
    if self.value.endswith("."):
      return True
    else :
      return False
    
  def is_question(self):
    if self.value.endswith("?"):
      return True
    else :
      return False

  def is_exclamation(self):
    if self.value.endswith("!"):
      return True
    else :
      return False

  def count_sentences(self):
    for char in ["?","!"]:
      self.value = self.value.replace(char,".")
    
    sentences = [s for s in self.value.split('.') if s]

    total_sentences= len(sentences)

    return total_sentences    
