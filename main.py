from weather.weather import *

myfile = "weather.dat"
mychoice = 0

while True:
    print("       *** TUFFY TITAN WEATHER LOGGER MAIN MENU\n")
    print("1. Set data filename")
    print("2. Add weather data")
    print("3. Print daily report")
    print("4. Historical report")
    print("9. Exit the program")
    mychoice = int(input("Enter menu choice:"))
    if mychoice == 1:
        myfile = input("Enter data filename: ")
        weather = read_data(myfile)
    elif mychoice == 2:
        dt = input("Enter data: ")
        tm = input("Enter time: ")
        t = int(input("Enter temprature: "))
        h = int(input("Enter humidity: "))
        r = float(input("Enter the rainfall: "))
        weather[dt+tm]= {'t':t,'h':h,'r':r}
        write_data(weather, myfile)
    elif mychoice == 3:
        d = input("Enter date (YYYYMMDD): ")
        display = report_daily(weather, d)
        print(display)
    elif mychoice == 4:
        display = report_historical(weather)
        print(display)
    elif mychoice == 9:
        break
