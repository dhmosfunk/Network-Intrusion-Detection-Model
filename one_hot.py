import pandas as pd
categorical_features = ['protocol_type','service','flag',]
def one_hot_encoding(data,categorical_features=categorical_features):
    for col in categorical_features:
        one_hot =pd.get_dummies(data[col],prefix=col)

        data =  pd.concat([data,one_hot],axis=1)
    # data.drop(categorical_features,axis=1)
    return data