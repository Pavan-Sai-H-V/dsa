jewels='aA'
stones='aAAbbbb'
#findout no of jewels in stones
#expected output =3

def lets_calc(jewels,stones):
    count=0
    for stone in stones:
        if stone in jewels:
            count+=1
    return count

lets_calc(jewels,stones)