def replace(elem,source,dist):
    i=0   # replace algorithm using an intermidate list 
    intr=[] 
    if elem==1:
        while(i<elem):
            var=liste[source-1].pop(len(liste[source-1])-1)
            liste[dist-1].append(var)
            i=i+1
    else :
        while(i<elem):
            var=liste[source-1].pop(len(liste[source-1])-1)
            intr.append(var)
            i=i+1
        i=0
        while(i<elem):
            var=intr.pop(len(intr)-1)
            liste[dist-1].append(var)
            i=i+1


f=open("./txt files/day5.txt",'r')

l1=['d','l','j','r','v','g','f']
l2=['t','p','m','b','v','h','j','s']
l3=['v','h','m','f','d','g','p','c']
l4=['m','d','p','n','g','q']
l5=['j','l','h','n','f']
l6=['n','f','v','q','d','g','t','z']
l7=['f','d','b','l']
l8=['m','j','b','s','v','d','n']
l9=['g','l','d']

liste=[l1,l2,l3,l4,l5,l6,l7,l8,l9]

for i in f:
    i=i.strip()
    z=i.split()
    z.pop(0) # remove the 'move'
    z.pop(1) # remove the 'from'
    z.pop(2) # remove the 'to'
    # -- after removing we got a list with only 3 elements (how much - source - distination) which suits our func 'replace' --
    replace(int(z[0]),int(z[1]),int(z[2]))

var=''
# part of construction of the word 
for j in liste:
    var=var+j[len(j)-1]

print(var.upper())

f.close()