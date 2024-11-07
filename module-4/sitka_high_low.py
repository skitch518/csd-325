import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get the dates, high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)
        low = int(row[6])
        lows.append(low)

#Created a function to plot the highs
def plot_highs(dates, highs):
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')

    # Add title and labels to the plot
    plt.title("Daily High Temperatures - 2018", fontsize=24)
    plt.xlabel('Date', fontsize=16)
    fig.autofmt_xdate()  
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()
#Created a function to plot the lows    
def plot_lows(dates, lows):
    fig, ax = plt.subplots()
    ax.plot(dates, lows, c='blue')
    
    # Add title and labels to the plot
    plt.title("Daily Low Temperatures - 2018", fontsize=24)
    plt.xlabel('Date', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

#Created a main function to allow the user to select from high or low
# & To be recursive so the program will continue until the user exits
def main(dates, highs, lows):   
   #Validate data
    try:
        highs_vs_lows = input("Would you like to see the high or low temperatures? (high/low) or exit: ")
    except ValueError:
        print("Please enter a valid input")
    #Change input to lowercase to prevent case sensitivity
    highs_vs_lows = highs_vs_lows.lower()
    if highs_vs_lows == "high":
        plot_highs(dates, highs)
    elif highs_vs_lows == "low":
        plot_lows(dates, lows)
    elif highs_vs_lows == "exit":
        print("Thank you for using the program")
        sys.exit()
    else:
        print("Please enter a either high, low, or exit")
    #Call the main function to create a loop
    main(dates, highs, lows)

# Explain to the user that they must close the graph to continue
print("Select either high or low tempatures to display. To display another graph close the first graph and enter either high or low. To exit close the graph and enter exit.")
print(" ")

if __name__ == '__main__':
    main(dates, highs, lows)
