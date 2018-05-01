fname=input("Enter file name: ")
if len(fname)<1:fname="mbox-short.txt"
fh=open(fname)
lst=list()
for line in fh:
    if line.startswith("From "):
        word=line.split()[1]
        print(word)
        lst.append(word)
print(lst)
namecount=dict()
for name in lst:
    namecount[name]=namecount.get(name,0)+1
bigcount=None
bigname=None
for name, count in namecount.items():
    if bigcount is None or count>bigcount:
        bigname=name
        bigcount=count
print(bigname, bigcount)
