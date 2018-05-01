name = input("Enter file name: ")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst=list()
for line in handle:
    if not line.startswith('From '):continue
    words=line.split()[5]
    word=words.split(':')[0]
    lst.append(word)
counthour=dict()
for hour in lst:
    counthour[hour]=counthour.get(hour,0)+1
fnlst=sorted(counthour.items())
for hour,count in fnlst:
    print(hour,count)
