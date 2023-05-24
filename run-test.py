import os
import time
print ('\n')
ask1=float(input ('How long should the CPU be Stress-Tested? (Minuets) 	'))
os.system ("for i in $(seq $(getconf _NPROCESSORS_ONLN)); do yes > /dev/null & done")
print ('\n')
answer=ask1 * 60
time.sleep (answer)
os.system ("killall yes")
print ('Test Complete!')
time.sleep (10)