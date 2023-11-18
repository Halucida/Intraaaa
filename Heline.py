import apache_beam as beam

import tensorflow as tf

from typing import List

def alignment(arr : List[float]):
  return tf.math.argmax(arr).numpy()

class Modeli(beam.DoFn):
  def process(self, element):
    result = alignment(element.inference)
    yield result