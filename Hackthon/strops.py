
#1 getspan() function
print("#1 getspan() function")
print()
def getspan(str1,ss):
    count=0
    list1=[]
    list2=[]
    start=0
    end=0
    matching_character=0
    while(start<len(str1)):
        matching_character=str1[start:].find(ss)
        if(matching_character==-1):
            break
        start=str1[start:].find(ss)+start
        end=start+len(ss)
        list1.append((start,end))
        count+=1
        start=end
    list2.append(count)
    list2.append(list1)
    return list2
print('-'*100)
str1=input("enter the string-->")
ss=input("enter the substring-->")
print(getspan(str1,ss))
print('-'*100)
 
#2 reverseWords(s) function 
print("#2 reverseWords(s) function ")
print()
def reverseWords(s):
    for i in range(len(s)-1,-1,-1):
        print(s[i],end='')
    print()
print('-'*100)
s=input("enter the string-->")
reverseWords(s)
print('-'*100)

#3 remove function()
print("#3 remove puntuation function()")
print()
def removePunctuation(s):
    str=""
    for i in s:
        if(i.isalpha() or i.isdigit() or i==" "):
            str=str+i
    return str
print('-'*100)
s=input("enter the sting-->")
print(removePunctuation(s))
print('-'*100)

print("#4 countWords function()")
print()
#4 countWords function()
def countWords(s):
    count=1
    if(s==""):
        s=input('please enter a string----->')
    for i in s.strip():
        if i==" ":
            count+=1
    return count
print('-'*100)
s=input("enter the sentence-->")
print(countWords(s))
print('-'*100)

print("#5 charecterMap() function")
print()
#5 charecterMap() function
def charecterMap(s):
    d={}
    count=0
    for i in s:
        if(i in d):
            d[i]+=1
        else:
            d[i]=count+1
 
    print(d)
print('-'*100)
str=input("enter the string")
charecterMap(str)
print('-'*100)

print("#6 makeTitle() function")
print()
#6 makeTitle() function
def makeTitle(s):
    return s.title()
print('-'*100)
s=input("enter the string for the title-->")
print(makeTitle(s))
print('-'*100)
makeTitle(s)

print("#7 normalizeSpaces() function")
print()
#7 normalizeSpaces() function
def normalize(str):

    str1 = str.split()
    return " ".join(str1)
print("-"*100)
str=input("enter the string normalize spaces------>")
str1=(str).strip()
print(normalize(str1))
print("-"*100)


#8 transform() function
print("#8 transform() function")
print()
def transform(s):
    tran = str.maketrans(s, s.swapcase())
    res = s.translate(tran)
    print(''.join(list(reversed(res))))
print('-'*100)
s=input("enter the string to translate-->")
transform(s)
print('-'*100)
 
#9 permuntations function() 
print("#9 permuntations function()")
print()
import random
def factorial(num):
    fact=1
    if(num<0):
        raise ("value not found")
    while(num!=0):  
        fact=fact*num
        num=num-1
    return(fact)


def permuntations(data):
    mn=factorial(len(list(data)))
    print(mn,'ways')
    list1=[]
    a=list(data)
    random.shuffle(a)
    na=''.join(a)
    for i in range(mn):
        random.shuffle(a)
        na=''.join(a)
        while True:
            if na not in list1:
                list1.append(''.join(a))
                break
            else:
                random.shuffle(a)
                na=''.join(a)
 
    return(list1)
print('-'*100)
data=input("enter string---->")
print(permuntations(data))
print('-'*100)
 



 