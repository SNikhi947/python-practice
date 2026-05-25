text="I am Nikhil Kumar"
print(text[::-1])
vo="aeiouAEIOU"
count=0
for i in text:
    if i in vo:
        count= count+1
print(count)
print(text.upper())
print(text.replace(" ",""))
text="nan"
print(True if text == text[::-1] else False)
