#!/usr/bin/env python
# coding: utf-8

# In[43]:


N, M, V = map(int, input().split())


# In[44]:


matrix = [[0]*(N+1) for i in range(N+1)]


# In[45]:


visited = [0]*(N+1)


# In[46]:


for i in range(M):
    startnode, endnode = map(int, input().split())
    matrix[startnode][endnode] = matrix[endnode][startnode] = 1
    


# In[55]:


def dfs(V) : 
    visited[V] = 1
    print(V, end = ' ')
    for i in range(1,N+1):
        if (visited[i]==0 and matrix[V][i]==1):
            dfs(i)


# In[56]:


dfs(V)
print()


# In[ ]:



    
    


# In[ ]:




