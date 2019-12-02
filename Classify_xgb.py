import pandas as pd
import joblib


def classify_xgb(data_path, model_name):
    csv_data = pd.read_csv(data_path)
    predictors = [x for x in csv_data.columns if x not in ['index', 'id', 'label1', 'label2']]

    with open(model_name, 'rb') as pkl_file:
        alg = joblib.load(pkl_file)

        data_predictions = alg.predict(csv_data[predictors])
        data_preprob = alg.predict_proba(csv_data[predictors])[:, 1]
        predictions = [round(value) for value in data_predictions]

        submission = pd.DataFrame({'Filename': csv_data['id'], 'PClass': data_predictions,  'Pro': data_preprob})
        submission.to_csv("class_result.csv", index=False)

