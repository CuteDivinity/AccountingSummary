import pandas
import base_helper
import global_vars

df = base_helper.read_csv()
summary_dict = {}

for index, row in df.iterrows():
    accounting_text = row[global_vars.column_accounting_text]
    # Check for blacklist entries, that should be ignored
    if any(accounting_text in item for item in global_vars.blacklist):
        continue
    # Check for cash withdrawal
    elif accounting_text == global_vars.withdrawal_text:
        name = "Cash withdrawal"
    else:
        name = row[global_vars.column_name_of_creditor_debtor]
    name = base_helper.format_name(name)  # format name in case of different spelling on multiple transfers
    # Get amount
    amount_string = row[global_vars.column_amount]
    amount = base_helper.convert_to_float(amount_string)
    # Build the dict
    summary_dict = base_helper.sum_dictionary(summary_dict, name, amount)

print(summary_dict)