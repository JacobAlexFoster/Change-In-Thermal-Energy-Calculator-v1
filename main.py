print("Which two parts of the equation do you know?")
print("Thermal Energy Change = Q")
print("Mass = M")
print("Specific Heat Capacity = C")
print("Temperature Change = T")

x = input("First known variable (Q/M/C/T): ").strip().upper()
y = input("Second known variable (Q/M/C/T): ").strip().upper()

if x == "M" and y == "C":
    m = float(input("Mass (kg): "))
    c = float(input("Specific Heat Capacity (J/kg·°C): "))
    delta_T = float(input("Temperature Change (°C): "))
    Q = m * c * delta_T
    print(f"Thermal Energy Change (Q): {Q} Joules")

elif x == "Q" and y == "M":
    Q = float(input("Thermal Energy Change (J): "))
    m = float(input("Mass (kg): "))
    c = float(input("Specific Heat Capacity (J/kg·°C): "))
    delta_T = Q / (m * c)
    print(f"Temperature Change (T): {delta_T} °C")

elif x == "Q" and y == "C":
    Q = float(input("Thermal Energy Change (J): "))
    c = float(input("Specific Heat Capacity (J/kg·°C): "))
    delta_T = float(input("Temperature Change (°C): "))
    m = Q / (c * delta_T)
    print(f"Mass (M): {m} kg")

elif x == "M" and y == "T":
    m = float(input("Mass (kg): "))
    delta_T = float(input("Temperature Change (°C): "))
    Q = float(input("Thermal Energy Change (J): "))
    c = Q / (m * delta_T)
    print(f"Specific Heat Capacity (C): {c} J/kg·°C")

else:
    print("Invalid input. Please enter Q, M, C, or T.")