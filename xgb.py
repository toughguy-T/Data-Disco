import pandas as pd
import joblib
import numpy as np


def classify_xgb(data_path, model_name):
    csv_data = pd.read_csv(data_path)
    predictors = [x for x in csv_data.columns if x not in ['index', 'id', 'label1', 'label2']]
    newname = model_name.replace(".", "-")
    with open('classifier_model/' + model_name, 'rb') as pkl_file:

        alg = joblib.load(pkl_file)

        data_predictions = alg.predict(csv_data[predictors])
        data_preprob = alg.predict_proba(csv_data[predictors])[:, 1]
        # 保留三位有效数字
        data_preprob = [format(value, '.3g') for value in data_preprob]

        submission = pd.DataFrame({'Filename': csv_data['id'], 'PClass': data_predictions,  'Pro': data_preprob})
        submission.to_csv("temp/class_result" + '-' + newname + ".csv", index=False)
