import time

import pandas as pd

from main import classify

# ## Step 1 - Calculate tokens for Conversations

# ## Output will be test.csv file containing NumTokens for each conversation

# df = pd.read_excel("Chat Statistics.xlsx",header=2)

# generate_num_tokens(dataframe=df["Conversations"])

## Step 2 - Read the test.csv, and filter the tokens which are less than 4000

## Output will be tokenized_data.csv file containing all the conversations less than 4000 tokens

# df = pd.read_csv("test.csv")

# filtered_df = df[df['NumTokens'] < 4000].dropna()

# df.to_csv("tokenized_data.csv",index=False,header=True)

## Step 3 - Call the classify_query function and execute the code

## Output will final_responses.csv containing tech or non tech queries

start_time = time.time()

df = pd.read_csv("tokenized_data.csv")

_df = df["Conversations"]

new_df = pd.DataFrame(columns=["Conversations","Classifaction"])

lst = [classify(str(i)) for i in _df]

new_df["Conversations"] = _df

new_df["Classifaction"] = lst

new_df.to_csv("final-100.csv", index=False, header=True)

end_time = time.time()

elapsed_time = (end_time - start_time) / 3600

print("Elapsed Time:", elapsed_time, "hours")

