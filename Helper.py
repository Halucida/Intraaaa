from stop_words import get_stop_words

def stopper(sentence : str):
  unlist = get_stop_words('en')
  plit = sentence.lower()
  plit = sentence.split()
  result = [i for i in plit if i not in unlist]
  result = " ".join(result)
  return result