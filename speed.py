import time 
gen_start_time = time.time()
print(sum(n for n in range(1000000000)))
gen_stop = time.time() - gen_start_time