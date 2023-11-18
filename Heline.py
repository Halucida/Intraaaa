import apache_beam as beam

from apache_beam.ml.inference.base import RunInference
from apache_beam.ml.inference.base import KeyedModelHandler
from apache_beam.ml.inference.tensorflow_inference import TFModelHandlerTensor
from apache_beam.options.pipeline_options import PipelineOptions

class Modeli(beam.DoFn):
    def process(self, element):
        result = f"{element.example} = {element.inference}"
        yield result