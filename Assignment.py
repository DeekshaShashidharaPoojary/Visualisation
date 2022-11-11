# -*- coding: utf-8 -*-
"""
Created on Fri Nov 2 12:14:35 2022

@author: Deeksha
"""


import pandas as pd
import matplotlib.pyplot as plt

#defing the funtion for line plot
def line_plot(data):
    plt.figure(dpi=144)#dpi is for clarity of the line plot
    #plotting and labelling the chart
    plt.plot(data["PeriodStart"], data["NumberOfCasesCommenced"],label="Cases Commenced")
    plt.plot(data["PeriodStart"], data["NumberOfSuccessfulCases"],label="Cases Successful")
    plt.xlabel("PeriodStart")
    plt.ylabel("Number of cases")
    #assigning the title for the graph 
    plt.title("Line plot showing the improvment in the prosecution")
    plt.legend()#It will show the index value on the graph
    plt.savefig('plot1.png')#saving the image

#defining the funtion for stacked bar plot
def stacked_bar_plot(drink_data):
    plt.figure(dpi=144)#dpi is for clarity of the bar plot
    #plotting and labelling the chart
    plt.bar(drink_data['country'],drink_data['beer_servings'],label='Beer Servings')
    plt.bar(drink_data['country'], drink_data['spirit_servings'],label='Spirit Servings')
    plt.bar(drink_data['country'], drink_data['wine_servings'],label='Wine Servings')
    plt.xlabel("Country")
    plt.ylabel("Drinks")
    #assigning the title for the graph
    plt.title("Stacked bar plot showing the different drinks servings")
    plt.legend()#It will show the index value on the graph
    plt.savefig('plot2.png')#saving the image
 
#defining the funtion for pie chart
def pie_chart(data):
    #dpi is for clarity of the pie chart
    plt.figure(dpi=144)
    #plotting the pie chart and labelling
    plt.pie(drink_data['total_litres_of_pure_alcohol'], labels=drink_data['country'], autopct='%1.2f%%')
    #assigning the title for the chart
    plt.title("Pie chart showing the total liters of pure alcohol consumption")
    plt.savefig('plot3.png')#saving the image
    
#reading a csv file
data=pd.read_csv('fsa-successful-prosecutions-april-2000-march-2017 (3).csv')

#dropping the table which is not usefull for this code
data=data.drop(["PeriodEnd","CompaniesOrIndividualsSuccessfullyProsecuted", "InfFilesCoveredBySuccessfulCases"], axis=1)

#selecting the particular area and year to plot
data=data[(data["Area"]=="food hygiene / safety") & (data['PeriodStart']>='01-04-2011')]
#calling the line funtion
line_plot(data)    

#reading the csv file
drink_data=pd.read_csv("drinks.csv")
print(drink_data)

#selecting only the first 5  rows
drink_data=drink_data.head()
print(drink_data)
#calling the funtion for stacked bar and pie chart
stacked_bar_plot(drink_data)
pie_chart(drink_data)

plt.show()









