sentence= input("Enter a sentence")
keyword= input("Input a keyword from the sentence")
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''#This code defines punctuation
#This code removes the punctuation
no_punct = "" 
for char in sentence:
    if char not in punctuations:
        no_punct = no_punct + char

no_punct1 =(str.lower (no_punct))
print(no_punct1)
