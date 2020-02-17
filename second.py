import re

'''if re.search("inform","We need to inform him with the inform latest aainformation"):
    print("There is inform")


allinform = re.findall("inform","We need to inform him with the inform latest aainformation")

for i in allinform:
    print(i)


str = "We need to inform him with the inform latest aainformation"

for i in re.finditer("inform",str):
    loc = i.span()
    print(loc)


str = "sat, hat, mat, bat, pat, zat"
#allstr = re.findall("[shmp]at",str)
allstr = re.findall("[H-Zh-z]at",str)
for i in allstr:
    print(i)

regex = re.compile("[m]at")
cat = regex.sub('cat',str)
print(cat)'''

randomstr = ''' 
today is sunny day
We can expect a match
between india and aus
'''

print(randomstr)
regex = re.compile("\n")
randomstr = regex.sub(" ",randomstr)
print(randomstr)

