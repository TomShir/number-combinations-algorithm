from colorama import Fore 
import sys 
from itertools import permutations 
import os
import pyttsx3
pyttsx3.init()
try:
    integer=int(input('integer:'))
    strinteger=str(integer)
    combinations=list(permutations(strinteger))
    time.sleep(1)
    print(f'All  possible combinations of the given integer value:{strinteger}\n\t')
    time.sleep(1)
    for combination in combinations:
        print(f'{"".join(combination)}\n')
        time.sleep(1)
    else:
        pass ''')
except ValueError:
    error_msg=f'ValueError:inappropiate value was entered'
    for text in error_msg:
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write(f'{Fore.RED}{text}')
    else:
        print(f'{Fore.RESET}')
        time.sleep(1)
        os.system('cls')
        pyttsx3.speak("program exitted due to ValueError")
        sys.exit(f'{Fore.RESET}')
