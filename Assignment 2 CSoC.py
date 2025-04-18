#Fibbonacci series
f0=0
f1=1
n=int(input("Enter the number of terms: "))
if n<=0:
    print("Please enter a positive integer")
else:
    i=0
    print("Fibonacci sequence:")
    while i< n:
        print(f0)
        f2=f0+f1
        f0=f1
        f1=f2
        i+=1    


#Prime Numbers Till N
m=int(input("Enter the number of terms for prime : "))
if m<=0:
    print("Please enter a positive integer")
else:
    print("Prime numbers:")
    for num in range(2, m+1):
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                break
        else:
            print(num)

# Vowel and Consonant Counter
text = input("Enter a sentence: ")

vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
for char in text:
    if char.isalpha(): 
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)


#Center-Aligned Star Triangle
q = int(input("Enter the number of rows: "))
for i in range(1, q + 1):
    spaces = ' ' * (q - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)

