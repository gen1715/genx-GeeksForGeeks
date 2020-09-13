# Simple interest formula is given by:
# Simple Interest = (P x T x R)/100
# Where,
# P is the principle amount
# T is the time and
# R is the rate


def simpleInterest(p,r,t):
    return (p*r*t/100)

if __name__ == '__main__':
    prin,rate,time = int(input("Enter the principle amount:\t")),int(input("Enter the rate:\t")),int(input("Enter the time:\t"))
    si = simpleInterest(prin,rate,time)
    print(f"simple interest for principle {prin} with rate {rate} percent for {time} years is: {si}")
