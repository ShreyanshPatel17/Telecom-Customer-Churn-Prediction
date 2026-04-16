import joblib

def load_all():
    pipeline = joblib.load('models/churn_pipeline.pkl')
    
    model = pipeline['model']
    scaler = pipeline['scaler']
    label_encoders = pipeline['label_encoders']
    features = pipeline['features']
    
    return model, scaler, label_encoders, features