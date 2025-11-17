import asyncio
print('welcome to the GAME')
name=input('Enter your Name:')
age=int(input('Enter your age:'))
is_valid = age>13
print(f'Welcome {name}')

async def check_age():
    print("checking credentials...")
    await asyncio.sleep(3)
    if is_valid:
        print('Valid age to play the game')
    else:
        print("cannot play age is too low")
asyncio.run(check_age())