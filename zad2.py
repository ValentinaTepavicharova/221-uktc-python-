min=int(input("Minutes:"))
sec=int(input("Seconds:"))
len=float(input("Total length:"))
meter=int(input("Time for 100m(in seconds):"))

clean_time=(len/100)*meter
add_time=(len//120)*2.5
total_time= clean_time - add_time 
target_time=min*60+sec

if total_time <= target_time:
    print("Peter won an Olympic quota!")
    print("His time is {}!".format(total_time))
else:
    print("No,Peter failed!")
    print("he was {} second slower!".format(total_time-target_time))













