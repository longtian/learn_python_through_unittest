import webbrowser
import time

total_breaks = 3
break_count = 0

print('the program starts at ' + time.ctime())

while break_count < total_breaks:
    time.sleep(2)
    webbrowser.open('http://www.baidu.com');
    break_count += 1
