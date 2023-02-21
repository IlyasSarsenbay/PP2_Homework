from datetime import datetime
  
start = datetime.strptime(input(), "%H:%M:%S")
end = datetime.strptime(input(), "%H:%M:%S")
  
difference = end - start
  
seconds = difference.total_seconds()
print(seconds)