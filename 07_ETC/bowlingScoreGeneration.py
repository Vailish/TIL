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
    return lst



lst1 = makes_num()
lst2 = makes_num()
lst3 = makes_num()
lst4 = makes_num()
cnt = 0
    
a = "{"
b = "}"
c = ["테스테스테스", "라면보단우동", "아이린좋아용", "나한테왜그래", "하상재하상재", "풍둔나선수리검", "지각하고싶어요", "댕댕이멍뭉이", "싸피좋아좋아", "스펀지밥핑핑이"][random.randint(0, 9)]
d = ["우동먹고싶다", "면보다밥이지", "소리에게돈까스", "최고의최대만"][random.randint(0, 3)]
e = ["갓리오넬메시", "shadowman", "siuuuu", "볼링덕후입니다"][random.randint(0, 3)]

print(
f'''
{a}
    "gameType" : "true",
    "gameData" : [{a}"nickname" : "우동먹고싶다", "score" : {lst1}{b},
                  {a}"nickname" : "{c}", "score" : {lst2}{b}
    ]
{b}
'''
)

# print(
# f'''
# {a}
#     "gameType" : "false",
#     "gameData" : [{a}"nickname" : "GotSsafy", "score" : {lst1}{b},
#                   {a}"nickname" : "{c}", "score" : {lst2}{b},
#                   {a}"nickname" : "{d}", "score" : {lst3}{b},
#                   {a}"nickname" : "{e}", "score" : {lst4}{b}
#     ]
# {b}
# '''
# )

# print(
# f'''
# {a}
#     "gameType" : "false",
#     "gameData" : [{a}"nickname" : "갓냥이", "score" : {lst1}{b},
#                   {a}"nickname" : "Canna", "score" : {lst2}{b},
#                   {a}"nickname" : "beomi", "score" : {lst3}{b}
#     ]
# {b}
# '''
# )