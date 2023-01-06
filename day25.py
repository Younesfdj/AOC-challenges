# Hello World !
d1 = {
    '2':2,
    '1':1,
    '0':0,
    '-':-1,
    '=':-2
}
d2 = {y: x for x ,y in d1.items()}
def SNAFU_to_dec(snafu:str)->int:
    liste=[]
    for i in range(len(snafu)):
        liste.insert(0,5**i)
    sum=0
    count=0
    for i in liste :
        sum+=i*d1[snafu[count]]
        count+=1
    return sum
def dec_to_SNAFU(nbr:int)->str:
    snafu=""
    while nbr>0:
        c = ((nbr+2)%5)-2
        snafu+=d2[c]
        nbr-=c
        nbr //= 5
    return snafu[::-1]
file='.\day25.txt'
with open(file,'r') as f:
    sum=0
    for number in f:
        sum+=SNAFU_to_dec(number.strip())
print(dec_to_SNAFU(sum))
