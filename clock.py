import datetime 
import time

# insipired to try my hand at a terminal clock, https://www.youtube.com/watch?v=bm8bgb_3OX8&t=143s
#and made tweaks that suited me better




now = datetime.datetime.now()

hour = now.hour
min  = now.minute
sec  = now.second
clock = f'{hour}:{min}:{sec}'


try:
    while True:
        now = datetime.datetime.now()
        hour = str(now.hour).zfill(2)
        min  = str(now.minute).zfill(2)
        sec  = str(now.second).zfill(2)
        clock = f'{hour}:{min}:{sec}'
        print(f'{hour}:{min}:{sec} \r',end="")
        time.sleep(1)
     
     


except KeyboardInterrupt:
    print('\nDone.')