#Yehuda Levy 332300433


############ Question 1 ############
############ Part 1 ############

def getPentaNum(n1, n2):
    return [(num * (3 * num - 1)) / 2 for num in range(n1, n2)]

############ End of Part 1 ############
############ Part 3 ############

def pentaNumRange(n1, n2):
    if not isinstance(n1, int) or n1 < 0 or not isinstance(n2, int) or n2 < 0 or n1 > n2:
        return "ERROR: the values must be positive integers and n2 > n1"
    return "\n".join(map(lambda nums: " ".join(f"{num:.1f}" for num in nums),
                         (lambda lst, n: [lst[i:i + n] for i in range(0, len(lst), n)]) \
                          (getPentaNum(n1, n2), 10)))

############ End of Part 3 ############
############ End of Question 1 ############

############ Question 2 ############
############ Part 1 ############

def sumDigits(n):
    return sum(map(int, list(str(abs(n)))))

############ End of Part 1 ############
############ Part 2 ############

def numGetter(num):
    if not isinstance(num, int):
        return "ERROR: Input number is incorrect!"
    return sumDigits(num)

############ End of Part 2 ############
############ End of Question 2 ############

############ Question 3 ############

def isPalindrome(n):
    if not isinstance(n, int):
        return "ERROR: Input number is incorrect!"
    return str(abs(n)) == str(abs(n))[::-1]

############ End of Question 3 ############

############ Question 4 ############
############ Part 1 ############

def m(n):
    if not isinstance(n, int) or n < 0:
        return "ERROR: Input number is incorrect!"
    else:
        return sum((map(lambda i: i / (i+1), range(1, n + 1))))

############ End of Part 1 ############
############ Part 2 ############

def userInput(n):
    return "\n".join(f"{i} {m(i)}" for i in range(1, n + 1))

############ End of Part 2 ############
############ End of Question 4 ############

############ Question 5 ############

def add3dicts (d1,d2,d3):
    if not isinstance(d1, dict) or not isinstance(d2, dict) or not isinstance(d3, dict):
        return "ERROR: Input is incorrect!"
    else:
        return { key: (tuple(d[key] for d in (d1, d2, d3) if key in d)
            if sum(key in d for d in (d1, d2, d3)) > 1
            else next(d[key] for d in (d1, d2, d3) if key in d))
            for key in set(d1) | set(d2) | set(d3)}

############ End of Question 5 ############



def main():
############  Main for Question 1 ############
    theInput1 = int(input("enter the value of n1 : "))
    theInput2 = int(input("enter the value of n2: "))
    print(pentaNumRange(theInput1, theInput2))
############  End of Main for Question 1 ############

############  Main for Question 2 ############
    theInput3 = int(input("Enter an integer number n (positive or negative):"))
    print(numGetter(theInput3))
############  End of Main for Question 2 ############

############  Main for Question 3 ############
    theInput4 = int(input("Enter an integer number n (positive or negative):"))
    if isPalindrome(theInput4):
        print("It is a palindrome")
    else:
        print("It is not a palindrome")
############  End of Main for Question 3 ############

############  Main for Question 4 ############
    theInput5 = int(input("Enter a Natural number n:"))
    print(userInput(theInput5))
############  End of Main for Question 4 ############

############  Main for Question 5 ############
    theInput6 = eval(input("Enter a dictionary:"))
    theInput7 = eval(input("Enter a dictionary:"))
    theInput8 = eval(input("Enter a dictionary:"))
    print(add3dicts(theInput6,theInput7,theInput8))
############  End of Main for Question 5 ############




if __name__ == "__main__":
    main()
