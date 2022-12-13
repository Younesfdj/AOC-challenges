with open('./txt files/day1.txt', 'r') as file :
    # --- First part
    top1 = -1
    total_cal = 0
    max_list = []
    for calories in file:
        if calories == '\n':
            if total_cal > top1:
                top1 = total_cal
                max_list.append(top1)
            total_cal = 0
        else :
            total_cal += int(calories.strip())
    print(f'Total calories is {top1}')
    # --- Second part
    max_list.pop(max_list.index(top1))
    top2 = max(max_list)
    max_list.pop(max_list.index(top2))
    print(f'Total calories of the top3 is {top1+top2+max(max_list)}')
file.close()