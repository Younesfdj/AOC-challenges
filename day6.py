def duplicate_letter(list)->int:
    # Find if there's duplicated letters in a word
    intr=''
    intr=intr.join(list)
    doubler=0
    for i in list:
        occu_of_i=0
        for j in intr:
            if i==j:
                occu_of_i=occu_of_i+1
        if occu_of_i>1:
            doubler=doubler+1
    if doubler==0:
        return 1
    else :
        return -1

f=open('./txt files/day6.txt','r')

conteur1=4
mot=f.read(4) # get the first 4 characters 
a=f.read(1)   # get the marker after the 4th char
while a!='':
    mot=mot+a # add that marker
    if duplicate_letter(list(mot[1:]))==1:   # verify if its a marker by verifying if the charachters are distinct 
        break
    else :   # if not increment the processed charachters by 1
        conteur1=conteur1+1
    mot=mot[1:] # remove the first char
    a=f.read(1)  # get a new possible marker

print(conteur1+1)

f.close()
f=open('./txt files/day6.txt','r')   # reopen the file 

# --- same algorithm with different values , here the check will be with 14 distinct charachters ---
conteur2=14
mot=f.read(14)
a=f.read(1)
while a!='':
    mot=mot+a
    if duplicate_letter(list(mot[1:]))==1:
        break
    else :
        conteur2=conteur2+1
    mot=mot[1:]
    a=f.read(1)

print(conteur2+1)

f.close()