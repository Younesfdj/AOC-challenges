def reponse1(mina,maxa,minb,maxb)->bool:

    # --- we determine the cases which the interval a doesn't overlap interval b or the oposite ---

    if maxa<minb: # example a=[1-10] b=[12-20] 
        return False
    elif mina<minb and maxa<maxb: # example a=[1-3] b=[2-5] 
        return False
    elif maxb<mina:  # example b=[1-10] a=[12-20]
        return False
    elif minb<mina and maxb<maxa: # example b=[1-3] a=[2-5] 
        return False
    else :  # other cases are correct
        return True

def reponse2(mina,maxa,minb,maxb)->bool:

    # --- we determind only the cases where a doesnt have any element contained in b  

    if maxa<minb: # example a=[1-10] b=[12-20] 
        return False
    elif maxb<mina: # example b=[1-10] a=[12-20]
        return False
    else:   # other cases are true
        return True

f=open('./txt files/day4.txt','r')
pair1=0
pair2=0
for i in f:
    list=i.strip().split(',')
    list1=list[0].split('-') # get the first interval
    list2=list[1].split('-') # get the second interval
    mina=int(list1[0])  # get the inf of interval a
    maxa=int(list1[1])  # get the sup of interval a
    minb=int(list2[0])  # get the inf of interval b
    maxb=int(list2[1])  # get the sup of interval b

    if reponse1(mina,maxa,minb,maxb):
        pair1=pair1+1
    if reponse2(mina,maxa,minb,maxb):
        pair2=pair2+1

print(pair1)
print(pair2)

f.close()