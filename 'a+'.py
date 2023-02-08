f=open("text.txt",'a+')
f.write('\nhey i am apending a new line here.')
print(f.tell())
f.seek(0)
text=f.read()
print(text)
f.close
