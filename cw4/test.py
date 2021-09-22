
import pandas as pd
df = pd.read_csv("grocery.csv")
def concat_func(x):
    return pd.Series({
        'Member_number':','.join(x['Member_number'].astype(str).unique()),
        'Date':','.join(x['Date'].unique())
    }
    )


data_new=df.groupby(["Member_number","Date"])['itemDescription'].apply(list).to_frame()
data_new['itemDescription']=data_new['itemDescription'].apply(lambda x:str(x).replace('[','').replace(']',''))
data=data_new['itemDescription'].to_list()
for i in range(len(data)):
    data[i]=data[i].replace("'","").replace(" ","").replace("\n","").split(',')
print(type(data))


print(data)
'''
D1=map(set,item)
candidate = create_candidates(item, verbose=True)
F0, support_data = support_prune(D1, candidate, 0.6, verbose=True)
F, support_data = apriori(dataset, min_support=0.6, verbose=True)
rules = generate_rules(F, support_data, min_confidence=0.8, verbose=True)
'''



