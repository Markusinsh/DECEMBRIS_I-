def faktorials(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorials(n-1)

# Galvenā funkcija (Testēju ar skailti 12)
if __name__ == "__main__":
    skaitlis = int("12")
    rezultats = faktorials(skaitlis)
    print(f"{skaitlis} faktoriāls ir {rezultats}")
