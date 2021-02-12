altitude = input("Enter the altitude: ")

if int(altitude)<=1000:
    print("Safe to land")
elif int(altitude)>=1000 and int(altitude)<=5000:
    print("Bring down to 1000")
else:
    print("go around and try again later")
