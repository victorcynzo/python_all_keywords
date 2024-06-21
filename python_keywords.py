#all 39 keywords in Python
from keyword import kwlist, softkwlist

def display_keywords():
    print('Keywords: ')
    for i, kw in enumerate(kwlist, start=1):
        print(f'{i:2}: {kw}')
    
    print('soft keywords: ')
    for i, skw in enumerate(softkwlist, start=1):
        print(f'{i:2}, {skw}')
    
def main():
    display_keywords()

if __name__ == '__main__':
    main()