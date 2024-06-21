#class, creating a class, provide blueprint of what class should contain, here name and work
class Person:
    def __init__(self, name: str) -> None:
        self.name = name

    def work(self) -> None:
        print(f'{ self.name} is working.')

#break, after condition, break out of loop
for i in range(10):
    if i == 5:
        break
    else:
        print(i)
print('Done')

#await, keyword with async, waits for task and then continues
import asyncio
from asyncio import Future
async def my_task(no: int) -> dict:
    print('Starting task...')
    await asyncio.sleep(2)
    return {'task': no}

async def main() -> None:
    tasks: Future = asyncio. gather(my_task(1), my_task(2), my_task(3))
    results: list[dict] = await tasks
    print(results)

if __name__ == '__main__':
    asyncio.run(main=main())

# async, asynchronised programming, execute multiple tasks concurrently without waiting for one to finish
import asyncio #asynchronised tasks
async def main() -> None:
    print("I am an asynchronous function!")

if __name__ == '__main__':
    asyncio.run(main==main())

#assert minimum requirements, in example runs with 'users.db'
db: str | None = 'users.db'
# db: str | None = None -- doesn't run because database doesn't exist
assert db, 'Cannot run program without the database'
# next program runs as long as condition is met, n < limit
limit: int = 10
n: int = 2
assert n < limit, f'{n} is not less than the limit ({limit}).'

#as give an alias to a module, to keep it short
import math as m 
from random import randint as ri

x = m.cos(10)
print(x)
y = ri(10, 20)
print(y)

#and check if BOTH conditions are true
a, b, c = 1, 2, 3

if c > b and c > a:
    print('both conditions are true')

#True is constant, integer value of 1
has_no_money: bool = True

print(has_no_money)
print(int(True))

#None represents absence of a value, for example data or element doesn't exist
None 

#False is constant, equal to integer number 0
has_money: bool = False

print(has_money)
print(int(False))