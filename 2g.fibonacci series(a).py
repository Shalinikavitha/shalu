n_terms=int(input("How many terms the user wants to prints?"))
n1=0
n2=1
count=0
if n_terms<=0:
   print("Please enter a positive integer, the given number is not valid")
elif n_terms==1:
   print("The Fibonacci sequence of the numbers up to",n_terms,":")
   print(n1)
else:
   print("The Fibonacci sequence of the numbers is :")
   while count<n_terms:
    print(n1)
    nth=n1+n2
    n1=n2
    n2=nth
    count+=1
