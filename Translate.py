import time


t1 = time.time()

import translators as ts

text = 'cheese'

print(ts.bing(text, from_language ='en', to_language = 'fr'))

t2 = time.time()
t = t2 - t1
print("Elapsed time is : ", t, " seconds")
