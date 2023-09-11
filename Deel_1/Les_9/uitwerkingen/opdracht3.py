leeftijd = int(input("wat isn je leeftijd?"))
snor = str(input("heeft u een snor? ja/nee?")) 
diploma = str(input("heeft u een diploma?"))

if leeftijd >= 18 and snor == "ja":
    print("je bent aangenomen!")
elif leeftijd < 18 and diploma == "ja":
    print("je bent aangenomen!!!") 
else:
    print("helaas je bent niet aangenomen!")

