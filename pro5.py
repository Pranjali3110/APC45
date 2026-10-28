#Write a PYTHON program to evaluate the student performance
      #If % is >=90 then Excellent performance
      #If % is >=80 then  Very Good performance
      #If % is >=70 then Good performance
      #If % is >=60 then average performance
      #else Poor performance

per=int(input("Enter the percentage:"))
if per>=90:
 print("Excellent performance")
elif per>=80 & per<90:
 print("Very Good performance")
elif per>=70 & per<80:
 print("Good performance")
elif per>=60 & per<70:
 print("Average performance")
else:
 print("Poor performance")