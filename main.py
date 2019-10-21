from nltk.tokenize import word_tokenize
import nltk
import pytesseract
from PIL import Image
import nltk
from nltk.corpus import stopwords
import re
import requests
import json
from string import ascii_lowercase
#x = json.loads("{'foo' : 'bar', 'hello' : 'world'}")

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = Image.open('IMG_20180118_133351.jpg')
text = pytesseract.image_to_string(img)
print(text)
document = ''
stop = stopwords.words('english')
#print(stop)

document = ' '.join([i for i in text.split() if i not in stop])
sentences = nltk.sent_tokenize(document)
#print(str(sentences[0]))

sample = "Albert Einstein was born in Ulm, Germany in 1879."
#nltk.download('stopwords')
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')

s = ''
new = list(text.split('\n'))
#print(new)

for i in range(len(new)):
    res = list(str(new[i]).split())
    email = re.findall(r'[\w\.-]+@[\w\.-]+.com',s.join(res))
    website = re.findall(r'www.[\w\.-]+',s.join(res))
    if email != []:
        print("Email Id : ",email[0])
    if website != []:
        print("Website : ",website[0])
sentences = [nltk.word_tokenize(sent) for sent in sentences]
sentences = [nltk.pos_tag(sent) for sent in sentences]

task = {'encodingType': 'UTF8','document': {'type': 'PLAIN_TEXT','content': text} }
x = json.dumps(task)
resp = requests.post('https://language.googleapis.com/v1/documents:analyzeEntities?key=AIzaSyBmZTuFzxLQmdD1SsjItzfj_-qBEq3vSKY', json=task)

dic = resp.json()["entities"]
#print(dic)
for element in dic:
    if element['type'] == 'PERSON':
        print("Name : ",element['name'])
        break
for element in dic:
    if element['type'] == 'PHONE_NUMBER':
        print("Contact : ",element['name'])
tokenize_word = word_tokenize(text)
#print(tokenize_word)


#new = list(text.split('\n'))
#print(new)
