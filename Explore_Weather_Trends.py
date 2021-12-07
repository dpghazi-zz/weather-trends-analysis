#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#importing libraries
import pandas as pd # to load data into Jupyter notebook
import matplotlib.pyplot as plt #to make line chart and visualize data


# In[ ]:


temp = pd.read_csv('clean_data.csv') #importing data set


# In[ ]:


print (temp)


# In[ ]:


#visualize Long Beach Average Temperature
plt.plot(temp['year'],temp['lb_avg_temp']) plt.xlabel("Years")
plt.ylabel("Temperature (°C)")
plt.title("Long Beach Temperature (AVG)") #AVG = Average plt.show()


# In[ ]:


#visualize Long Beach Moving Temperature Average
lb_mv_avg = temp['lb_avg_temp'].rolling(10).mean() # smooth out data using pandas in-built rolling function plt.plot(temp['year'],lb_mv_avg)
plt.xlabel("Years")
plt.ylabel("Temperature (°C)")
plt.title("Long Beach Temperature (MA)") #MA= Moving Average
plt.show()


# In[ ]:


#visualize Global Average Temperature
plt.plot(temp['year'],temp['gl_avg_temp']) plt.xlabel("Years") plt.ylabel("Temperature (°C)") plt.title("Global Temperature (AVG)") plt.show()


# In[ ]:


#visualize Global Moving Temperature Average
gl_mv_avg = temp['gl_avg_temp'].rolling(10).mean() #10 year moving average (refer to Step 2 above) plt.plot(temp['year'],gl_mv_avg)
plt.xlabel("Years")
plt.ylabel("Temperature (°C)")
plt.title("Global Temperature (MA)")
plt.show()


# In[ ]:


#plot final line chart
plt.plot(temp['year'],lb_mv_avg,label='Long Beach') plt.plot(temp['year'],gl_mv_avg,label='Global') plt.xlabel("Years")
plt.ylabel("Temperature (°C)")
plt.title("Long Beach and Global Temperature (MA)")
plt.legend()
plt.show()


# In[ ]:


global_data = pd.read_csv('results-4.csv')
org_gl_ma = global_data['avg_temp'].rolling(10).mean() plt.plot(global_data['year'],org_gl_ma) plt.xlabel("Years")
plt.ylabel("Temperature (°C)")
plt.title("(A) Original Global Temperature (MA)") plt.show()
gl_mv_avg = temp['gl_avg_temp'].rolling(10).mean() #10 year moving average (refer to Step 2 above) plt.plot(temp['year'],gl_mv_avg)
plt.xlabel("Years")
plt.ylabel("Temperature (°C)")
plt.title("(B) Global Temperature (MA)")
plt.show()

