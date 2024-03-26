#!/usr/bin/env python
# coding: utf-8

# In[5]:


## 문제 4 ##
score = int(input("점수를 입력하세요 : "))

if score >= 90:
    print("장학생", end= '')
elif score >=60:
    print("합격", end= '')
else:
    print(" 불합격", end= '')
print("입니다. ^^")


# In[13]:


## 문제 5 ##
num = 5
if num % 2 == 0:
    res = "짝수"
else:
    res = "홀수"
print(res)
## 삼항 연산자 ##
num = 5
res = "짝수" if num % 2 ==0 else "홀수"
print(res)
print("정답 3번")


# In[15]:


## 문제 6 ##
nn = [100, 200, 300, 400, 500]
nn[1] = 777
print("nn = ", nn)
nn[1] = [444,555]
print("nn = ", nn)
nn[1:4] = [444,555]
print("nn = ", nn)
nn[2:] = []
print("nn = ", nn)


# In[17]:


## 문제 5 ##
nn = [100, 200, 300, 400, 500]
print("nn[4] = ", nn[4])
print("nn[-1] = ", nn[-1])
print("nn[-2] = ", nn[-2])
print("nn[1:4] = ", nn[1:4])
print("nn[0:1] = ", nn[0:1])
print("nn[2:-1] = ", nn[2:-1])
print("nn[0::2] = ", nn[0::2])
print("nn[::-1] = ", nn[::-1])
print("nn[::-2] = ", nn[::-2])


# In[63]:


## 문제 8 ##
hap = 0
n = 1234

while n <  4568:
    if n%444 == 0:
        hap += n
    n = n + 1
    
print(hap)
    


# In[53]:


## 문제 9 ##
sum = 0
for i in range(3333, 10000,1):
    if (i % 1234) == 0:
        if sum+i > 100000:
            break
        sum = sum + i
    else:
        continue
print(sum)


# In[65]:


## 문제 14 ##
myData = [[n * m for n in range(1,3)] for m in range(2,4)]
print(myData)


# In[ ]:




