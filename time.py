totalseconds = 7340
hours = 0
minutes = 0
seconds = 0
while totalseconds >= 3600:
    hours += 1
    totalseconds -= 3600
while totalseconds >= 60:
    minutes += 1
    totalseconds -= 60
seconds = totalseconds
print(f"Time: {hours} hours, {minutes} minutes, {seconds} seconds")


time = int(input("enter time in seconds : "))
min = time//60
haur=time//3600
sec=time%3600
print(haur,"Haur", min, "Minute", sec,"Sec")




