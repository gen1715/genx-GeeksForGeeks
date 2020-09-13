# Formula to calculate compound interest annually is given by:
#
# A = P(1 + R/100) t
# Compound Interest = A – P
# Where,
# A is amount
# P is principle amount
# R is the rate and
# T is the time span


def compoundInterest(P,R,t):
    A = P*(pow((1 + R / 100), t))
    return (A - P)

if __name__ == '__main__':
    prin,rate,time = float(input("Enter the principle amount:\t")),float(input("Enter the rate:\t")),float(input("Enter the time:\t"))
    ci = compoundInterest(prin,rate,time)
    print(f"Compound interest for principle {prin} with rate {rate} percent for {time} years is: {ci}")
