import pandas as pd
import joblib

categorical_features = ['protocol_type','service','flag',]
def one_hot_encoding(data,categorical_features=categorical_features):
    for col in categorical_features:
        one_hot =pd.get_dummies(data[col],prefix=col)

        data =  pd.concat([data,one_hot],axis=1)
    # data.drop(categorical_features,axis=1)
    return data

col_names = ["duration","protocol_type","service","flag","src_bytes",
    "dst_bytes","land","wrong_fragment","urgent","hot","num_failed_logins",
    "logged_in","num_compromised","root_shell","su_attempted","num_root",
    "num_file_creations","num_shells","num_access_files","num_outbound_cmds",
    "is_host_login","is_guest_login","count","srv_count","serror_rate",
    "srv_serror_rate","rerror_rate","srv_rerror_rate","same_srv_rate",
    "diff_srv_rate","srv_diff_host_rate","dst_host_count","dst_host_srv_count",
    "dst_host_same_srv_rate","dst_host_diff_srv_rate","dst_host_same_src_port_rate",
    "dst_host_srv_diff_host_rate","dst_host_serror_rate","dst_host_srv_serror_rate",
    "dst_host_rerror_rate","dst_host_srv_rerror_rate","label"]

def predict(test):
    train = pd.read_csv("model/train_data.csv",names=col_names)
    #train = pd.read_csv("train_data.csv",names=col_names)
    test = one_hot_encoding(test)

    # add missing columns
    trainservice=train['service'].tolist()
    testservice= test['service'].tolist()
    difference=list(set(trainservice) - set(testservice))
    string = 'service_'
    difference=[string + x for x in difference]


    for col in difference:
        test[col] = 0

    train = train.drop(categorical_features,axis=1)
    test = test.drop(categorical_features,axis=1)
    test = test.drop('label',axis=1)
    print(test.columns)
    #print(test.shape())
    model = joblib.load('model/model.sav')
    #model = joblib.load('model.sav')
    result = model.predict(test)
    return result

def get_results(dataset_name):
    path="static/files/"
    test = pd.read_csv(path + dataset_name,names=col_names)
    return predict(test)
