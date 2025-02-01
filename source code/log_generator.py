import random
 import time
 log_types = ['INFO', 'WARNING', 'ERROR']
 with open('synthetic_logs.log', 'a') as f:
 while True:
 log_type = random.choice(log_types)
 message = f"{log_type}: A sample log message at {time.strftime('%Y-%m-%d
 %H:%M:%S')}\n"
 f.write(message)
 time.sleep(1) 
