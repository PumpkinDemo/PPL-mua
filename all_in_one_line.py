f = open('mua/Main.java','r')
data = f.read()
lines = data.split('\n')
s = ''
for line in lines:
    s += line.strip()
g = open('out', 'w')
print(s,file=g)
