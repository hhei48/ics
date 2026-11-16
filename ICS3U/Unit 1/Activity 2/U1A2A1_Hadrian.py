pi = 3.1415926
print("Welcome to the cylinder surface area calculator!")
height = float(input("Please enter the height of the cylinder (in cm): "))
radius = float(input("Please enter the radius of the cylinder (in cm): "))
cylinder_side = 2*pi*radius*height
cylinder_top_bottom = 2*pi*(radius**2)
surface_area = round(cylinder_side + cylinder_top_bottom, 2)
print(f"The surface area of the cylinder is {surface_area}cm².")
