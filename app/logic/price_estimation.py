import pandas as pd
import numpy as np
import joblib


def perform_price_estimation(sample):
    kmeans = joblib.load('./logic/SRC/groups.pkl')
    group = kmeans.predict([[float(sample.x5),float(sample.x6)]])
    df = {
        'x2': sample.x2,
        'x3': sample.x3,
        'x4': sample.x4,
        'group': group
    }
    df = pd.DataFrame(df)
    normalizer = joblib.load('./logic/SRC/normalizer.pkl')
    df = normalizer.transform(df)
    model = joblib.load('./logic/SRC/real_estate.pkl')
    predict = model.predict(df)
    return predict[0]



