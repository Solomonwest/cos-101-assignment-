def force():
    mass = float(input("Enter the mass in kg: "))
    acceleration = float(input("Enter the accelaration in m/s^2: "))
    print("The Force is ", mass * acceleration, "N.")

def average_speed():
    total_distance = float(input("Enter the total distance covered in metres: "))
    total_time = float(input("Enter the total time taken in seconds: "))
    print("The Average Speed is ", total_distance / total_time, "m/s.")

def power():
    workdone = float(input("Enter the wokdone in Joules: "))
    time = float(input("Enter the time taken in seconds: "))
    print("The Power is ", workdone / time, "Watts.")

def area_of_a_triangle():
    base = float(input("Enter the base value of the triangle"))
    height = float(input("Enter the height of the triangle"))
    print("The Area of the triangle is ", 1/2 * base * height, "cm.")

def area_of_a_rectangle():
    length = float(input("Enter the length of the rectangle"))
    width = float(input("Enter the width of the rectangle"))
    print("The Area of the Rectangle is ", length*width, "cm.")

intro = int(input("Welcome to Solomon west's Calculator, What would you like to calculate? \n Type 1 to calculate Force  \n Type 2 to calculate Average speed \n Type 3 to calculate power \n Type 4 to calculate Area of a triangle \n Type 5 to calculate Area of a rectangle \n"))


if intro == 1:
    force()
elif intro == 2:
    average_speed()
elif intro == 3:
    power()
elif intro == 4:
    area_of_a_triangle()
elif intro == 5:
    area_of_a_rectangle
else:
    print("Invalid Parameters Provided, Kindly re-run the program.")

print("Thanks for using our servives")