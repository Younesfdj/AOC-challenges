with open('./txt files/day10.txt', 'r') as file:
   cycles=[20,60,100,140,180,220]
   sum_signal_strength=0
   cycle=0
   x=1
   for instruction in file:
        ins=instruction.strip().split()
        if ins[0]=='noop':
            cycle+=1
            if cycle in cycles:
                sum_signal_strength+=x*cycle
        elif ins[0]=='addx':
            cycle+=1
            val=int(ins[1])
            x+=val
            if cycle in cycles :
                sum_signal_strength+=cycle*(x-val)
            cycle+=1
            if cycle in cycles :
                sum_signal_strength+=cycle*(x-val)
print(sum_signal_strength)
file.close()