import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

def get_big_mac_price_by_year(year,country_code):
    df = pd.read_csv(big_mac_file)
    filtered_df = df[(df['date'].str[:4] == str(year)) & (df['iso_a3'] == country_code.upper())]
    mean_price = round(float(filtered_df['dollar_price'].mean()), 2)

    return mean_price


def get_big_mac_price_by_country(country_code):
    df = pd.read_csv(big_mac_file)
    country_code_df = df[df['iso_a3'] == country_code.upper()]
    mean_price_country =round(float(country_code_df['dollar_price'].mean()), 2)
    
    return mean_price_country

def get_the_cheapest_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)
    min_df = df[df['date'].str[:4] == str(year)]
    min_df_idx = min_df['dollar_price'].idxmin()
    min_item = df.loc[min_df_idx]
    cheapest_big_mac_price = f"{min_item['name']}({min_item['iso_a3']}): ${round(min_item['dollar_price'], 2)}"

    
    return cheapest_big_mac_price


def get_the_most_expensive_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)
    max_df = df[df['date'].str[:4] == str(year)]
    max_df_idx = max_df['dollar_price'].idxmax()
    max_item = df.loc[max_df_idx]
    expensive_big_mac_price = f"{max_item['name']}({max_item['iso_a3']}): ${round(max_item['dollar_price'], 2)}"
    
    
    return expensive_big_mac_price

if __name__ == "__main__":
    print("\nWelcome to the Big Mac Index Program!")
    
    print("\nYou will be asked to indicate what you need: (Big Mac Price by Year), (Big Mac Price by Country),\
 (Cheapest Big Mac Price by Year), and (Most Expensive Big Mac Price by Year). Type (exit) if you no longer need the program")
    
    
    while True:
        user_decide = input("\nWhat would you like to know? \n")
        if user_decide.lower() == "big mac price by year":
            user_price_by_year = int(input("\nEnter the desired year: \n"))
            user_country_code = input("\nEnter the country code: \n")
            print(f"\nHere is the Big Mac Price by Year: {get_big_mac_price_by_year(user_price_by_year, user_country_code.lower())}")
        elif user_decide.lower() == "big mac price by country":
            user_country_code = input("\nEnter the desired country code: \n")
            print(f"\nHere is the Big Mac Price by Country: {get_big_mac_price_by_country(user_country_code.lower())}")
        elif user_decide.lower() == "cheapest big mac price by year":
            user_cheap_year = int(input("\nEnter the desired year: \n"))
            print(get_the_cheapest_big_mac_price_by_year(user_cheap_year))
        elif user_decide.lower() == "most expensive big mac price by year":
            user_exp_year = int(input("\nEnter the desired year: \n"))
            print(get_the_most_expensive_big_mac_price_by_year(user_exp_year))
        elif user_decide.lower() == "exit":
            break
        else:
            print("\nSomething was typed incorrectly please try again!")



            