
total_Sc =760345

hours = total_Sc // 3600
minutes = (total_Sc % 3600) // 60
seconds = total_Sc % 60

print(f"{total_Sc} is {hours} h {minutes} mn {seconds} s")