import pandas as pd
data = pd.read_csv("50_states.csv")
states = data["state"]
print(states)