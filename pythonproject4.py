#_________________________________________
#string list problem about if it is palindrom or not
#word=input("enter the word: ")
#new=word[::-1]
#if word==new:
#    print("yes it is palindrome: ")
#else:
#    print("no")
#______________________________________________________________________________
#rock paper scissors problem vs cpu:
#import random



#s=0

#while s<3:
#    cpu=random.randint(1,3)
#    player=int(input("for rock press 1,for paper press 2,for scissors press 3:- "))
#rock decisions
#    if player == 1 and cpu == 1 :
#        print("cpu also chose rock its a draw draw")
#    elif player == 1 and cpu == 2:
#        print("you loose cpu chose paper")
#    elif player == 1 and cpu == 3:
#        print("you win cpu chose scissors")
#paper decisions
#    if player == 2 and cpu == 2 :
#        print("cpu also chose rock its a draw draw")
#    elif player == 2 and cpu == 3:
#        print("you loose cpu chose paper")
#    elif player == 2 and cpu == 1:
#        print("you win cpu chose scissors")
#scissors decission
#    if player == 3 and cpu == 3 :
#        print("cpu also chose rock its a draw draw")
#    elif player == 3 and cpu == 1:
#        print("you loose cpu chose paper")
#    elif player == 3 and cpu == 2:
#        print("you win cpu chose scissors")
#
#    s += 1
#____________________________________________________________________________________-
#guessing game one problem:
#guess=int(input("guess the number from 1 to 9: "))
#num=guess+2
#s=random.randint(1,9)
#if guess > s :
#    print(f"number was {s}")
#    print("you guessed too high")
#elif  guess < s :
#    print(f"number was {s}")
#    print("you guessed too low")
#elif guess == s:
#    print(f"number was {s}")
#    print("you guessed right!!!!")
#________________________________________________________________________________
#List Overlap Comprehensions problem
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#common=[]
#for i in a:
#    if i in b and i not in common:
#        common.append(i)
#print(common)
#_______________________________________________________________________________________
#Check Primality Functions problem:
#import math

#def prime(a):
#    if a<=1:
#        print("1 and negtive integer can't be prime numbers")
#    for i in range(2,int(a**0.5)):
#        if a % i ==0:
#            print("not a prime")
#        else:
#            print("prime")
#s=int(input())
#prime(s)


