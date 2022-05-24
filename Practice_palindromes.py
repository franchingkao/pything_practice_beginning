#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#verson 1: by my own
entry = input("enter string to test for palindromes or \'exist\': ")
word = entry.lower()

if word.isalnum():

    if word != "exist":
        if word[0] == word[-1]:
            print(True)
        else:
            print(False)


# In[1]:


#version2 by teaching: make the function

#test whether is a palindrome
def is_palindrome(tester):
    if tester == tester[::-1]:
        return True
    else:
        return False


# In[2]:


#test whether is a number or alphabet
def is_alnum(tester):
    new_word = ""
    for x in tester:
        if x.isalnum():
            new_word += x
    return new_word


# In[5]:


#set it always run io
run = True
while run:
    entry = input("enter string to test for palindromes or \'exit\': ")
    tester = entry.lower()
    
    if tester == "exit":
        run = False
        break #add 'break' here so that it won't run the rest of lines to print the result
    
    word = is_alnum(tester)
    result = is_palindrome(word)
    print(f"Palindrome test result: {result}")

