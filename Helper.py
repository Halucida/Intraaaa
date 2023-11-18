import apache_beam as beam

import tensorflow as tf

from typing import List

from stop_words import get_stop_words

def stopper(sentence : str):
  unlist = get_stop_words('en')
  plit = sentence.lower()
  plit = sentence.split()
  result = [i for i in plit if i not in unlist]
  result = " ".join(result)
  return result

def alignment(arr : List[float]):
  return tf.math.argmax(arr).numpy()

class Modeli(beam.DoFn):
  def process(self, element):
    result = alignment(element.inference)
    yield result