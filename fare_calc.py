def calculate_fare(km, vehicle_type, hour):

    rates = {
        "economy": 10,
        "premium": 18,
        "suv": 25,
        "e": 10,
        "p": 18,
        "s": 25
    }

    if vehicle_type not in rates:
        return "Service Not Available"

    fare = km * rates[vehicle_type]

    if 17 <= hour <= 20:
        fare = fare * 1.5

    return fare


print("Welcome to CityCab Fare Calculator")

km = float(input("Enter distance (in km): "))
vehicle_type = input("Enter vehicle type \n(Economy/Premium/SUV or E/P/S ): ")
vehicle_type=vehicle_type.lower()
hour = int(input("Enter hour (0-23): "))


result = calculate_fare(km, vehicle_type, hour)

print("\n--- Price Receipt ---")

if result == "Service Not Available":
    print(result)
else:
    print("Distance:", km, "km")
    print("Vehicle:", vehicle_type)
    print("Final Fare: Rs", result)