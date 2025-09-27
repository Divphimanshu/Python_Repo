marks1=int(input(" enter marks : "))
marks2=int(input(" enter marks : "))
marks3=int(input(" enter marks : "))

total_per= (marks1+marks2+marks3)/300 * 100

if(total_per>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("you have passed by : ", total_per)
else:
    print("you have failed, only : ", total_per)    