import random;
def makes_num():
    def randnum(lst, num):
        if num == 1:
            return lst.append(random.randint(0, 10))
        else:
            return lst.append(random.randint(0, 10 - lst[-1]))

    lst = []
    cnt = 0
    while True:
        cnt += 1
        if len(lst) == 22:
            break
        if len(lst) == 21:
            if lst[19] == 10 or lst[20] == 10 or lst[19] + lst[20] == 10:
                randnum(lst, 1)
                continue
            else:
                lst.append(0)
                continue


        if cnt == 1:
            randnum(lst, 1)
            continue
        
        if cnt % 2:
            if lst[-1] == 10:
                lst.append(0)
            else:
                randnum(lst, 0)
    print(lst)


makes_num()
makes_num()