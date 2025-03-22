

#Given numbers = [1, 2, 3, 4, 5], use a for loop to print each number.
numbers=[1,2,3,4,5]
for i in numbers:
    print(i)

#Given fruits = ["apple", "banana", "cherry"], use a for loop to print:
fruits=["apple","banana","cherry"]
for i in fruits:
    print("i like fruits")

#Given nums = [10, 20, 30, 40], use a for loop to calculate and print the total sum.
nums=[10,20,30,40]
b=0
for i in nums:
        b=b+1
print(b)        

#Given numbers = [1, 2, 3, 4, 5, 6], use a for loop to count how many numbers are even.
numbers=[1,2,3,4,5,6]
count=0
for i in numbers:
     if i%2==0:
        count+=1
print(count)        

# Given nums = [3, 7, 2, 8, 5], use a for loop to find and print the largest number.
nums=[3,7,2,8,5]
largest=0
for i in numbers:
     if i>largest:
          largest=i
print("largest no.is",largest)   

#Given original = [5, 10, 15, 20], use a for loop to copy all elements into a new list.
original=[5,10,15,20]
new=[]
for i in original:
    new.append(i*2)
print(new)     

#Given nums = [1, 2, 3, 4], use a for loop to create a new list where each number is doubled.
nums=[1,2,3,4,5]
new=[]
for i in nums:
     new.append(i*2)
print(new)     
     
# Given words = ["hello", "world", "python"], use a for loop to print the elements in reverse order.
v=["hello","world","python"]
new=[]
for i in range(len(v)-1,-1,-1):
     new.append(v[i])
print(new)     

#Given words = ["apple", "banana", "avocado", "grape"], use a for loop to print only the words that start with "a".
v=["apple","banana","grape","avacado"]
new=[]
for i in v:
     if i[0].lower()=="a":
          new.append(i)
print(new)          
          
#Given numbers = [-5, 10, -3, 7, -2, 8], use a for loop to create a new list containing only the positive numbers. 
numbers=[-5,10,-3,7,-2,8]
new=[]
for i in numbers:
     if i>0:
        new.append(i)
print(new)        
    
     