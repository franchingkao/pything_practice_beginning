#!/usr/bin/env python
# coding: utf-8

# NumPy
# 1. 以陣列取代列表
# 2. 多維度資料

# In[1]:


import numpy as np


# In[2]:


x = np.array([1,2,3])
print(x)
print(x.size)


# In[3]:


# 一維陣列
data = np.array([1,2])
print(data)

# 創造資料數為2的陣列, 資料內容未指定
data = np.empty([2])
print(data)

# 創造資料數為2的陣列, 資料內容為0 
data = np.zeros([2])
print(data)

# 創造資料數為2的陣列, 資料內容為1
data = np.ones([2])
print(data)

# 創造資料數為5的陣列, 資料內容為0至4
data = np.arange(5)
print(data)


# In[ ]:


# 二維陣列 (2x3)
data = np.array([[1,2],[1,2],[1,2]])
print(data)
data = np.empty([2,3])
print(data)
data = np.zeros([2,3])
print(data)
data = np.ones([2,3])
print(data)


# In[ ]:


# 三維陣列 (2x3x4)
data = np.array([[[1,2],[1,2],[1,2]],[[1,2],[1,2],[1,2]],[[1,2],[1,2],[1,2]]])
print(data)
data = np.empty([2,3,4])
print(data)
data = np.zeros([2,3,4])
print(data)
data = np.ones([2,3,4])
print(data)


# In[4]:


# 逐一元素運算 +-*/ > == <= ... (elementwise)
data1 = np.array([1,2,3])
data2 = np.array([3,4,5])

data1+data2


# In[5]:


# 矩陣運算
data1 = np.array([[1,2]]) #1x2
data2 = np.array([[4,5],
                  [3,4,5]]) #2x3

# 內積 1x3 
# *必須要data1的最後一個維度與data2的第一個維度相同才可運算
data1.dot(data2)
data1@(data2)
# 外積 2x6
np.outer(data1,data2)


# In[6]:


#統計運算
data = np.array([[1,2,5],
                 [3,4,7]]) #3x3

# 全部加總
data.sum()
# 加總column
data.sum(0)
# 加總row
data.sum(1)
# 最小值
data.min()
# 最大值
data.max()
# 逐值累加
data.cumsum()
# 平均數
data.mean()
# 標準差
data.std()

# 除了sum以外, 其他method也可以加上column或row僅運算攔獲列


# In[7]:


# 資料的形狀shape
data = np.array([[1,2,3,4],
                [1,2,3,4]])
# 資料維度(形狀)
data.shape
# 資料轉置
data.T
# 資料扁平化
data.ravel()
# 資料重塑
# 資料總數必須一樣
data.reshape(4,2)


# In[8]:


# 多維度資料索引
data1 = np.array([[1,2,3,4],
                [1,2,3,4]])
data2 = np.array([5,4,3])

# 索引位置
data1[1,3]

# y 資料切片slicing
data1[0:1, 2:4]
data2[1:3]
data1[0:2, ...] # ...取全部 空白也會取全部


# In[9]:


# 合併stacking
data1 = np.array([1,2,3])
data2 = np.array([5,4,3])

result1 = np.vstack((data1,data2))
result2 = np.hstack((data1,data2))
print(result1)
print(result2)


# In[10]:


# 切高splitting
data = np.array([[1,2,3,4],[5,4,3,2]])

result1 = np.vsplit(data,2)
result2 = np.hsplit(data,2)
print(result1)
print(result2)

# 必須要注意數量

