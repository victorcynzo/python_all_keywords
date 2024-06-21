#softkeyword can be used as python variable and softkeyword
#keyword cannot be used as variable

#type since Python 3.12, so need to update Python for this one..., declare own type
type IntOrStr = int | str
var: IntOrStr = 10
var2: IntOrStr = 'text'
var3: IntOrStr = None #otherwise return warning message

#match, power of pattern matching
weather: tuple[str, int] = 'rain', 6
match weather:
    case 'rain', severity if severity <= 5:
        print(f'Rain ({severity})')
    case 'rain', severity if severity > 5:
        print(f'Very hard rain! ({severity})')
    case 'cloudy', severity:
        print(f'CloudCream, anyone? ({severity})')
    case _:
        print('Unknown weather')

#case, to match case statements, can be more readable and concise than if/elif/else statements
weather: str = 'rain'
match weather:
    case 'rain':
        print('Not again!')
    case 'cloudy':
        print('CloudCream, anyone?')
    case _: #all the other cases, underscore as soft keyword
        print('Unknown weather, damn you climate change!')

# _ underscore, can use as variable name, throwaway variable, not something you refer to
# or to define dunder method in a class
from typing import Callable
_ = 10
for _ in range(3):
    print('Hello')
class Fruit:
    def __init__(self) -> None:
        print('Dunder methods use underscores to define them.')

#soft keywords

#yield, create generators, once value has been yielded, it disappears
from typing import Generator
def generate_numbers(limit :int) -> Generator:
    for i in range(0, limit):
        yield i

numbers: Generator = generate_numbers(limit=10)
print(next(numbers)) #once retrieved, deletes from generator
print(next(numbers))
print(next(numbers))
print(list(numbers)) #check output

#with, automatcially open, close, and finally (if wrong) file, always closes file after, handles all
with open('text.txt', 'r') as file:
    text: str = file.read()
    print(text)

#while is used for while loops, or for infinite loops by typing while True
import time
is_connected: bool=True
i: int = 1
while is_connected:
    if i==3:
        is_connected = False
    print(f'Connected for: {i}s')
    time.sleep(1)
    i += 1
print('Connection lost... ')

#try, run dangerous code, code that might run an exception
try:
    result: float = 1_000_000 / 0 #gives zerodivisionerror,
    #for example wrong user input, float and user gives 10 (int)
except ZeroDivisionError:
    print('Go home bob, you are drunk...')

#return, returns(outputs) value from a function 
from datetime import datetime
def get_time() -> str: #specify that it returns a string
    now: datetime = datetime.now()
    return f'{now:%r}' #by default return None, even without specified
print(get_time())

#raise, manually make an exception
raise Exception('Manually raised an exception for no reason.')

#pass, placeholder for function, class, or for loop
def func():
    pass
class Fruit:
    pass

#or, check for multiple conditions (non-inclusive), only one needs to be satisfied
a, b, c = 5, 10, 20
if c > a or a == b:
    print('One of the conditions was satisfied.')

#not, check if statement not true
names: list[str] = ['Bob', 'Tom', 'James', 'Jef']
if 'Bob' not in names:
    print('Bob is lost...')

selected_user: str | None = None
if selected_user is not None: #use is not, don't use !=
    print(f'You have selected: {selected_user}.')
else:
    print('No user selected')

#nonlocal
def func() -> None:
    item: str = 'candle'
    def inner_func() -> None: #state that function returns None
        nonlocal item #chooses item not in this local function (apple), but the candle one
        item = 'apple'
        print(item)
    inner_func()
func()

#lambda, nameless function
p = lambda x: print(x) #generally would not assign to variable, so bad example
p(10) #or (lambda x: (print(x))(10))

from typing import Callable, Any
def print_results(func: Callable, elements: list[Any]):
    for elem in elements:
        print(func(elem))

print_results(lambda x: x*2, elements=[1,2,3,4]) #quite nice to only use funciontionality once

#is, checks if object is same, compares memory address (not value)
class Fruit:
    ...
apple: Fruit = Fruit() #instance of the fruit
other_apple = apple #second variable points to original value
print(apple is other_apple) #True
banana: Fruit = Fruit()
print(apple is banana) #False, not same object

print(f'{id(apple)=}') #whatever id is
print(f'{id(other_apple)=}')
print(f'{id(banana)=}') #different id from apple and other apple

#in, two possible places, check in for loop, also can do membership checks
names: list[str] = ['Bob', 'James', 'Joe']
for name in names:
    print(name)
if 'Bob' in names:
    print('We found Bob!')

#import, used to import packages and modules
import random
print(random.random())

#if, boolean expressions, check condition after 'if', True then execute following block
age: int = 137
if age > 100:
    print('Wow, you are fucking old')

#global refers to objects in global namespace, can be accessed anywhere
name: str = 'Bob'

def change_name() -> None:
    global name #need to reference global scope here, otherwise will refer to local scope
    name = 'James' #local scope
change_name()
print(name)

#from, import specific functionality
from random import randint

#for, for-loop and iterations, for each in each, do next indented code
from typing import Any
elements: list[Any] = [1, 'text', True, 'Bob']
for element in elements:
    print(element)

#finally, runs no matter what, always executed
#except, run when exception is met
from typing import Never
def dangerous_code() -> Never:
    raise ValueError('Bad value')
try:
    dangerous_code()
except ValueError as e:
    print(f'Yo, you messed up: "{e}".')
finally:
    print('finally: I fun no matter what happens')

#else, only executes when none of the other conditions are met
#elif, used as middle layer in if-else checks, can use as many as you'd like
weather: str = 'rainy'

if weather == 'rainy':
    print('Remember to bring an umbrella!')
elif weather == 'cloudy':
    print('Remember to wear CloudCream!')
elif weather == 'sunny':
    print('Remember to eat icecream!')
else:
    print('Fuck the weather then I guess..')

#del, delete the object, first time value, second error
name: int = 10
print(name)

del name
print(name)

#def, defines a function
def  func() -> None:
    print('Hello World')
func()

#continue, ignore rest of code, for loop exits for Bob
names: list[str] = ['Tom', 'Bob', 'James']

for name in names:
    if name == 'Bob':
        print('We do not say hello to Bob')
        continue
    print(f'Hello, {name}!')

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