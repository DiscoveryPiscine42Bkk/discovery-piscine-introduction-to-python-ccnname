import sys

if (len(sys.argv) - 1) != 1:
    print("none")
else:
    first_param = sys.argv[1].upper()
    print(f"{first_param}")
