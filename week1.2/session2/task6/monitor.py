# Week 1.2, Session 2: Task 6
machine_temperature = int(input("Enter the machine's temperature in degrees Celsius: "))
machine_pressure = int(input("Enter the machine's pressure in PSI: "))
machine_status = int(input(" Enter 1 for operating, 0 for stopped: "))

if machine_temperature > 80:
    print("Machine temperature is too high, please sut down the machine")
elif machine_temperature < 50:
    print("Machine temperature is low, no action needed.")
else:
    print("Machine temperature is within safe limits." )

if machine_pressure > 100:
    print("High pressure is detected, maintenance is recommended.")
elif machine_pressure < 70:
    print("Machine pressure is low, the system is operating normally.")
else:
    print("Machine pressure is stable." )

if machine_status == 1:
    if machine_temperature > 80 or machine_pressure > 100:
        print("The machine is running in unsafe conditions, please shut it down.")
    else:
        print("The machine is running normally.")
else:
    print("Machine is stopped, no immediate action is required." )