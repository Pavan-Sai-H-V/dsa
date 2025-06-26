jewels='aA'
stones='aAAbbbb'

#findout no of jewels in stones  { we use o(n*m) here }
#expected output =3
# def calc(jewels,stones):
#     count=0
#     for stone in stones:
#         if stone in jewels:
#             count+=1
#     return count

# calc(jewels,stones)

s=set(jewels) #time compleity of O(m+n)
def calc(jewels,stones):
    count=0
    for stone in stones:
        if stone in jewels:
            count+=1
    return count

calc(s,stones)