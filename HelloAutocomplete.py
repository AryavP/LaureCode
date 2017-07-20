import autocomplete

autocomplete.load()

def predict(statement = []):
 sentence = "".join(statement).split(" ")
 choices = []

 one = None
 two = None
 if len(sentence)>1:
  length = len(autocomplete.predict_currword_given_lastword(sentence[-2], sentence[-1]))
  if length>=1:
   one = autocomplete.predict_currword_given_lastword(sentence[-2], sentence[-1])[0]
  if length>=2: two = autocomplete.predict_currword_given_lastword(sentence[-2], sentence[-1])[1]
 else:
  length = len(autocomplete.predict_currword(sentence[-1]))
  if length>=1:one = autocomplete.predict_currword(sentence[-1])[0]
  if length>=2:two = autocomplete.predict_currword(sentence[-1])[1]

 if one is not None: one = extract(one)
 if two is not None: two = extract(two)
 
 if one is not None: choices.append(one)
 else: choices.append("N/A")
 choices.append(sentence[-1])
 if two is not None: choices.append(two)
 else: choices.append("N/A")

 print " - ".join(choices)
 return choices

def extract(string):
 statements = list(string)
 return statements[0]

def check(lis = []):
 new_list = "".join(lis).split(" ")
 length = len(new_list[-1])
 print length
 if length >= 3 and length%2 != 0: return True
 else: return False

if __name__=="__main__":
 lis = ['t', 'h']
 test = ['m']
 print check(lis)
 print predict(lis)
