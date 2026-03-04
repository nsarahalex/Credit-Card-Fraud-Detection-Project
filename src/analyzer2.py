import pandas as pd

df = pd.read_csv('data/creditcard.csv')

#print("----Dataset Health Check----")
#print(df.info())
#print(df.columns.tolist())

# Check the distribution of the 'Class' column

fraud_distribution = df['Class'].value_counts()
print(fraud_distribution)

# 0: legit 1: fraud
#Percentage of fraud

percentage = (fraud_distribution[1]/len(df))*100
print(f"Percentage of fraud = {percentage:.4f}%")

#Find the mean amount in each category
legit = df[df['Class'] == 0]
fraud = df[df['Class'] == 1]


avg_legit_mean = legit['Amount'].mean()
avg_fraud_mean = fraud['Amount'].mean()
print(f"Avg amout for legit : {avg_legit_mean:.2f}")
print(f"Avg amout for fraud: {avg_fraud_mean:.2f}")

threshold = 120
# create a new column where the amout is greater than 120, and another feature V1< - 2.0. 
df['is_flagged'] =( df['Amount'] > threshold)

hits = df[df['is_flagged'] ==True ]
hits.to_csv('data/falgged_transactions.csv',index =False)

print("\n ----Export Complete ___")
print("Flagged transactions saved to 'data/flagged_transactions.csv'")
true_frauds = hits[hits['Class'] == 1]
print(f"total flagged frauds = {len(true_frauds)}")
print(f"Total transactions flagged : {df['is_flagged'].sum()}")
print(df[df['is_flagged'] == True].head())