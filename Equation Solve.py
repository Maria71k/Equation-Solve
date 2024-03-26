def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root, root
    else:
        real_part = -b / (2*a)
        imaginary_part = (-discriminant)**0.5 / (2*a)
        return complex(real_part, imaginary_part), complex(real_part, -imaginary_part)

def main():
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    roots = solve_quadratic(a, b, c)
    print("Roots:", roots)

if __name__ == "__main__":
    main()
