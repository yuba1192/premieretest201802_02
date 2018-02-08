# -*- coding: utf-8 -*-
from collections import Counter
from itertools import chain
from janome.tokenizer import Tokenizer

data = []
t = Tokenizer()
f = open('data.txt','r',encoding="utf-8_sig")
val = f.read()
f.close()

tokens = t.tokenize(val)
for token in tokens:
 partOfSpeech = token.part_of_speech.split(',')[0]
 # 今回抽出するのは名詞だけとします。（もちろん他の品詞を追加、変更、除外可能です。）
 if partOfSpeech == u'名詞':

  data.append(token.surface)
chain_data = list(data)
c = Counter(chain_data)
for raw in c.most_common():
   ls_raw = list(raw)
   print(ls_raw[0] + "\t" + str(ls_raw[1]))