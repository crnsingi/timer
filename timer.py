import time

def countdown(t):
    while t:
        mins,secs =divmod(t,60)
        timer ='{:02d}:{:02d}'.format(mins,secs)