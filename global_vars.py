path = "umsatz.CSV"
column_name_of_creditor_debtor = "Beguenstigter/Zahlungspflichtiger"  # name of creditor/debtor
column_amount = "Betrag"  # amount of money
column_accounting_text = "Buchungstext"  # To check for type of entry
withdrawal_text = "BARGELDAUSZAHLUNG"
blacklist = ["SONSTIGER EINZUG", "ABSCHLUSS"]  # accounting_text entry that should be ignored
summary_dict = {}