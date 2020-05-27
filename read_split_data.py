file=open("text.txt")
x=file.read()
x=x.split(" ")
f=x[1]
f=f.split("/")
print(f[0])
