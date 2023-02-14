import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

def get_big_mac_price_by_year(year,country_code):
    file_object = open(big_mac_file)
    csv_reader = csv.reader(file_object)
    next(csv_reader)
    line_counter = 0
    mean_big_mac_price = 0
    big_mac_price = 0
    for data in csv_reader:
        if int(data[0][0:4]) == year and data[1].lower() == country_code:
            line_counter += 1
            big_mac_price += float(data[6])
    mean_big_mac_price = big_mac_price / float(line_counter)
    

    return round(mean_big_mac_price, 2)


def get_big_mac_price_by_country(country_code):
    file_object = open(big_mac_file)
    csv_reader = csv.reader(file_object)
    next(csv_reader)
    line_counter = 0
    mean_big_mac_price = 0
    big_mac_price = 0
    for data in csv_reader:
        if data[1].lower() == country_code:
            line_counter += 1
            big_mac_price += float(data[6])
    mean_big_mac_price = big_mac_price / float(line_counter)
    

    return round(mean_big_mac_price, 2)

def get_the_cheapest_big_mac_price_by_year(year):
    file_object = open(big_mac_file)
    csv_reader = csv.reader(file_object)
    next(csv_reader)
    lowest_price = 10000
    country_name = 0
    code = 0
    for data in csv_reader:
        if int(data[0][0:4]) == year and float(data[6]) < lowest_price:
            lowest_price = float(data[6])
            lowest_price = round(lowest_price, 2)
            country_name = data[3]
            code = data[1]


    return f"{country_name}({code}): ${lowest_price}"


def get_the_most_expensive_big_mac_price_by_year(year):
    file_object = open(big_mac_file)
    csv_reader = csv.reader(file_object)
    next(csv_reader)
    highest_price = 0
    country_name = 0
    code = 0
    for data in csv_reader:
        if int(data[0][0:4]) == year and float(data[6]) > highest_price:
            highest_price = float(data[6])
            highest_price = round(highest_price, 2)
            country_name = data[3]
            code = data[1]


    return f"{country_name}({code}): ${highest_price}"

if __name__ == "__main__":
    print("\nWelcome to the Big Mac Index Program!")

    print("\nYou will be asked to indicate what you need: (Big Mac Price by Year), (Big Mac Price by Country),\
        (Cheapest Big Mac Price by Year), and (Most Expensive Big Mac Price by Year). Type (exit) if you no longer need the program")


    while True:
        user_decide = input("\nWhat would you like to know? \n")
        if user_decide.lower() == "big mac price by year":
            user_price_by_year = int(input("\nEnter the desired year: \n"))
            user_country_code = input("\nEnter the country code: \n")
            print(f"\nHere is the Big Mac Price by Year: {get_big_mac_price_by_year(user_price_by_year, user_country_code)}")
        elif user_decide.lower() == "big mac price by country":
            user_country_code = input("\nEnter the desired country code: \n")
            print(f"\nHere is the Big Mac Price by Country: {get_big_mac_price_by_country(user_country_code)}")
        elif user_decide.lower() == "cheapest big mac price by year":
            user_cheap_year = input("\nEnter the desired year: \n")
            print(get_the_cheapest_big_mac_price_by_year(user_cheap_year))
        elif user_decide.lower() == "most expensive big mac price by year":
            user_exp_year = input("\nEnter the desired year: \n")
            print(get_the_most_expensive_big_mac_price_by_year(user_exp_year))
        elif user_decide.lower() == "exit":
            break
        else:
            print("\nSomething was typed incorrectly please try again!")
            


