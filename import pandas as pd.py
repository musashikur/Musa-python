import pandas as pd
#import matplotlib.pyplot as plt
# Sample data
balances = [1000, 2500, 4300, 1200, 5000]
# Creating a Series
balance_series = pd.Series(balances, name="Account Balance")
#print(balance_series)
#--------plot-------

# Sample data
data = {"Customer ID": [101, 102, 103, 104],"Name": ["Alice", "Bob", "Charlie", "David"],"Account Balance": [3000, 1500, 4000, 800],"Account Type": ["Savings", "Checking", "Savings",
"Checking"]
}
# Creating a DataFrame
bank_df = pd.DataFrame(data)
#print(bank_df)
#print(bank_df.head()) # By default, shows the first 5 rows


#Get all customers with a balance greater than $2000
high_balance_customers = bank_df[bank_df["Account Balance"]
> 2000]
print(high_balance_customers)
#Select specific columns, such as only customer names and account balances:
balances_df = bank_df[["Name", "Account Balance"]]
print(balances_df)
#Add a column for Interest Earned (e.g., assuming a 5% interest rate for demonstration):
bank_df["Interest Earned"] = bank_df["Account Balance"] *0.05
print(bank_df)
#Change the account type for a specific customer:
bank_df.loc[bank_df["Name"] == "Alice", "Account Type"] ="Premium Savings"
print(bank_df)

