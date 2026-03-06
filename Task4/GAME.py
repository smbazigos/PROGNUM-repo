#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

def game():

    playerinput = input("Choose Rock(R), Paper(P) or Scissors(S): ")

    outputlist = ['R', 'P', 'S']
    x=np.random.choice(outputlist)

    print(f"Im python and I will beat you. I choose: {x}")

    if playerinput == x:
        print("Its a draw. Lets play again")
        game()
    elif playerinput=='P' and x =='R':
        print("YOU LOSE")
    elif playerinput=='P' and x =='S':
        print("YOU WIN")
    elif playerinput=='R' and x=='P':
        print("YOU LOSE")
    elif playerinput=='R' and x=='S':
        print("YOU WIN")
    elif playerinput=='S' and x=='P':
        print("YOU WIN")
    elif playerinput=='S' and x=='R':
        print("YOU LOSE")

game()


# In[ ]:




