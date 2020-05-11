import pandas
import global_vars

def read_csv():
    """
        Read csv from global_vars defined csv
        :return df: dataframe of csv
    """
    df = pandas.read_csv(global_vars.path, sep=';')
    return df

def sum_dictionary(pre_sum_dictionary, name, amount):
    """
        Check for entry in dict and add amount
        :param pre_sum_dictionary: dictionary before summed up
        :param name: creditor/debtor
        :param amount: amount of money
        :return sum_dictionary: summed dictionary
    """
    sum_dictionary = pre_sum_dictionary
    if name in sum_dictionary:
        sum_dictionary[name] += amount
    else:
        sum_dictionary[name] = amount
    return sum_dictionary

def convert_to_float(input_string):
    string = input_string
    float_value = 0.00
    try:
        string = string.replace(",", ".")
        float_value = float(string)
    except Exception as Ex:
        print(f"Could not convert {input_string} to float: {Ex}")
    return float_value

def format_name(input_string):
    # All uppercase for consistent spelling
    string = input_string.upper()
    # Some names have many spaces in it, so we cut it after 5 spaces
    if "    " in string:
        string = string.split("     ")
        string = string[0]
    return string

