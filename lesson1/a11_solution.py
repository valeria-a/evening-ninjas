total_seconds = int(input("Insert movie length in seconds: "))
# 4000
total_minutes = total_seconds // 60 #66
seconds = total_seconds % 60 # seconds remainder # 40

hours = total_minutes // 60
minutes = total_minutes % 60

print(f"The length of the movie is: {hours}:{minutes}:{seconds}")