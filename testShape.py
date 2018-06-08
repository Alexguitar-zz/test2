import pandas as pd

groups = ["Modern Web", "DevOps", "Cloud", "Big Data", "Security", "自我挑戰組"]
num = [46, 8, 12, 12 ,6, 58]

dict = {"groups": groups,
       "num": num
       }

select_df = pd.DataFrame(dict)

#print(select_df.shape[1])
print(select_df.iloc[0:1, 1])
