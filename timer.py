import time
t=time.process_time()
n=100000000
value=10
for i in range(n):
 value2=value*value
elapsed_time=time.process_time()-t
print("N=",n,"value bits=",value.bit_length(),"time=",elapsed_time)

# value=10 took time=23.09
# value=10**10+1 took time=33.19
# value=10**100+1 took time=59.19