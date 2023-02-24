# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 07:53:18 2022

@author: Andrew
"""

import pandas as panda
import matplotlib.pyplot as plot

def user_selection(number_of_options):
    """
    Callable function to get user input and check its validity to the scenario.

    Parameters
    ----------
    number_of_options : INT
        Highest number of choice possible.

    Returns
    -------
    choice : INT
        User selection input.

    """
    while True:
        try:
            choice = int(input("Choice: "))
            if choice > number_of_options or choice < 1: #If out of range.
                print("Invalid Selection! Please Try Again\n")
            else:
                return choice
        except ValueError:
            print("Please enter number corresponding with the choices.")

def select_file():
    """
    Provides the possible choices on the files to select.

    Returns
    -------
    str
        Name of the file or exit.

    """
    print("\n"+"="*50,"\n")
    print("Select a file to analyze:")
    print("\t(1)PopChange.csv")
    print("\t(2)Housing.csv")
    print("\t(3)Exit Program")

    while True:
        file_choice = user_selection(3)#Call and run function.
        if file_choice == 1:
            return "PopChange.csv"
        if file_choice == 2:
            return "Housing.csv"
        if file_choice == 3:
            return "EXIT"


def select_column(file):
    """
    Provides the possible choice on the columns in the file to select.

    Parameters
    ----------
    file : STRING
        Name of file that was selected.

    Returns
    -------
    STRING
        The name of the column to be used.

    """
    while True:
        if file == "EXIT":
            return "EXIT"

        if file == "PopChange.csv":
            print("\n"+"="*50,"\n")
            print("Select a column to analyze in", str(file),": ")
            print("\t(1)Pop Apr1")
            print("\t(2)Pop Jul1")
            print("\t(3)Change Population")
            print("\t(4)EXIT")
            column_selection = user_selection(4)#Call and run function.

            def pop_change_columns(column_selection):
                """
                Class based, Swtich case using the dictionary

                Parameters
                ----------
                column_selection : TYPE
                    DESCRIPTION.

                Returns
                -------
                STRING
                    The name of the column to be used.

                """
                switch = {
                    1:'Pop Apr 1',
                    2:'Pop Jul 1',
                    3:'Change Pop',
                    4:'EXIT'
                    }
                return switch.get(column_selection, "Invalid input")
            return pop_change_columns(column_selection)

        if file == "Housing.csv":
            print("\n"+"="*50,"\n")
            print("Select a column to analyze in", str(file),": ")
            print("\t(1)Age")
            print("\t(2)Bedrooms")
            print("\t(3)Built")
            print("\t(4)Rooms")
            print("\t(5)Utility")
            print("\t(6)EXIT")
            column_selection = user_selection(6)#Call and run function

            def housing_columns(column_selection):
                """
                Class based SWITCH case using the dictionary

                Parameters
                ----------
                column_selection : INT
                    Number given by user.

                Returns
                -------
                STRING
                    The name of the column to be used.

                """
                switch = {
                    1:'AGE',
                    2:'BEDRMS',
                    3:'BUILT',
                    4:'ROOMS',
                    5:'UTILITY',
                    6:'EXIT'
                    }
                return switch.get(column_selection, "Invalid input")
            return housing_columns(column_selection)


def plot_graph(data):
    """
    Takes the data and plots the histogram graph in a separate window.

    Parameters
    ----------
    data : dataframe
        Essentially an array of all the data in the column selected.

    Returns
    -------
    None.

    """
    bins = 150#Number of data to display.
    data.plot.hist(bins = bins)#Plot
    plot.title('Histogram', fontweight = "bold")
    plot.show()


def print_analysis(count, mean, standard_deviation, minimum, maximum):
    """
    Def is mainly for organizing purposes.

    Parameters
    ----------
    column : STR
        Name of column.
    count : FLOAT
        Amount of rows in column.
    mean : FLOAT
        Number midway between extremes.
    standard_deviation : FLOAT
        Measure of amount of variation or dispersion of the set of values.
    minimum : FLOAT
        Lowest value in the data.
    maximum : FLOAT
        Highest value in the data.

    Returns
    -------
    None.

    """
    print("\n"+"="*50,"\n")
    print("Count: {:.2f}".format(count))
    print("Mean: {:.2f}".format(mean))
    print("Standard Deviation: {:.2f}".format(standard_deviation))
    print("Minimum Value: {:.2f}".format(minimum))
    print("Maximum Value: {:.2f}".format(maximum))


def analyze():
    """
    Get the file, get the column, find the data and then plot the data.

    Returns
    -------
    None.

    """
    while True:
        file = select_file()#Get and set name of file.
        if file != "EXIT":
            while True:
                column = select_column(file)
                if column != "EXIT":
                    dataframe = panda.read_csv(file, usecols = [column])#data frame
                    count = dataframe[column].count()
                    mean = dataframe[column].mean()
                    standard_deviation = dataframe[column].std()
                    minimum = dataframe[column].min()
                    maximum = dataframe[column].max()
                    print("\n"+"="*50,"\n")
                    print("Statistics for", str(column).capitalize())
                    print("-"*20)
                    print_analysis(count, mean, standard_deviation,
                                   minimum, maximum)

                    plot_graph(dataframe)
                else:
                    break
        else:
            break

print("*"*10,"Welcome to the Data Analysis App","*"*10)
analyze()
print("*"*10,"Thanks for using the Data Analysis App","*"*10)
input("press enter to exit")
