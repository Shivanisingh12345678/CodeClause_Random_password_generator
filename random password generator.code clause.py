import string
print("welcome to our random password generator")
def main():
    Length=int(input("Enter the length of Password you want:"))
    LowerD=string.ascii_lowercase
    UpperD=string.ascii_uppercase
    digitD=string.digits
    symbolsD=string.punctuation
    combine=LowerD+UpperD+digitD+symbolsD
    x=random.sample(combine,length)
    password="".join(x)
    print(password)
    main()
main()
