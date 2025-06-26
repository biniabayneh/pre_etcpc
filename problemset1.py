# Problem A. Taxi !! Input file: Output file: Balloon Color: standard input standard output Gold Ahmed and Amr need to return home within ten minutes to avoid punishment.
# They have a total of A and B units of money, respectively, and the taxi fare to their home is C units.
# Determine if they have enough money to pay for the taxi. Input The input consists of a single line containing three integers A, B, C (0 AB 1001 C 100).
# Output Print "YES"if they can afford the taxi, otherwise print "NO".
# Examples standard input standard output 4 2 3 32 1 34 YES NO
A, B, C = map(int, input().split())
if A + B >= C:
    print("YES")
else:
    print("NO")