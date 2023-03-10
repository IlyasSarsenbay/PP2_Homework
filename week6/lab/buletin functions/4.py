from time import sleep
import math
def delay(fn, ms, *args):
  sleep(ms / 1000)
  return fn(*args)
ms=int(input())
args=int(input())
print("Square root after specific miliseconds:") 
print("Square root of",args,"after",ms,"miliseconds is",delay(lambda x: math.sqrt(x), ms, args))