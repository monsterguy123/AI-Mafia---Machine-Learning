import matplotlib.pyplot as plt

# x = [1, 5, 8,12,7,2]
# y = [1, 5, 8,2,7,2]

# plt.style.use('fivethirtyeight')

# # Use plt.plot instead of plt.show for plotting
# plt.plot(x, y, color='green', linestyle='dashed', linewidth=3,
#          marker='o', markerfacecolor='red', markersize=8)

# plt.show()
# ---------------------------------#---------------------------------#
# plotting bar chart
# left = [1 ,2, 3, 4, 5]

# height = [10, 24, 36, 40, 5]

# tick_label = ['one','two','three','four','five']

# plt.bar(left,height,tick_label=tick_label,width=0.8,color = ['red','blue'])

# plt.xlabel('x-label')
# plt.ylabel('y-label')

# plt.title('My Bar Chart!')
# plt.show()
# plt.close()

# ---------------------------------#---------------------------------#
#plot histogram
# ages = [2,3,4,5,7,9,10,12,23,34,45,56,67,32,45,53,64,76,78,98]
# range = (0,100)
# bins = 10
# plt.hist(ages,bins,range,color='red',histtype='bar',rwidth=0.8)
# plt.show()
# plt.close()

# ---------------------------------#---------------------------------#
#plotting scatter plot
# x = [1,2,3,4,5,6,7,8,9,10]
# y = [2,4,5,7,6,8,9,11,12,12]
# plt.scatter(x,y,label='stars',color="blue",marker="*",s=30)
# plt.legend()
# plt.show()
# plt.close()

#plotting pie char
# activities = ['eat','sleep','work','play']

# slices = [3,7,8,9]

# colors = ['r','m','g','b']

# plt.pie(slices,labels = activities,colors=colors,startangle=90,shadow=True,explode=(0,0,0.1,0),radius=1.2,autopct='%1.1f%%')

# plt.show()