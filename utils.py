from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.model_selection import KFold
from sklearn.preprocessing import OneHotEncoder, StandardScaler





def evaluate_models(y_test, predictions):
    """
    Evaluate the performance of a model using various metrics.

    Args:
    y_test (array-like): True labels.
    predictions (array-like): Predicted labels.

    Returns:
    dict: A dictionary with evaluation metrics.
    """
    evaluation_metrics = {}
    evaluation_metrics['Mean Squared Error'] = mean_squared_error(y_test, predictions)
    evaluation_metrics['Mean Absolute Error'] = mean_absolute_error(y_test, predictions)
    evaluation_metrics['R2 Score'] = r2_score(y_test, predictions)
    
    return evaluation_metrics


def plot_model_evaluation(y_test, predictions):

    plt.figure(figsize=(8, 4))
    plt.scatter(y_test, predictions, alpha=0.5)
    plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--', lw=2)
    plt.xlabel('True Values')
    plt.ylabel('Predictions')
    plt.title('True Values vs Predictions')
    plt.show()

    plt.figure(figsize=(8, 4))
    sns.histplot(y_test - predictions, bins=30, kde=True)
    plt.xlabel('Prediction Error')
    plt.ylabel('Frequency')
    plt.title('Prediction Error Distribution')
    plt.show()


def feature_importance_abs(importance, feature_names):

    """
    NOMÉS PER UN linear regression model!!!
    importance = model.coef_ 
    feature_names = data.columns (list)
    """
    
    feature_importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': importance})
    feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)
    return feature_importance_df
    

def plot_linear_model_feature_importance(importance, feature_names):
    """
    NOMÉS PER UN linear regression model!!!
    importance = model.coef_ 
    feature_names = data.columns (list)
    """
    
    feature_importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': importance})
    feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)

    plt.figure(figsize=(10, 6))
    plt.barh(feature_importance_df['Feature'], feature_importance_df['Importance'], color='skyblue')
    plt.xlabel('Importance')
    plt.ylabel('Feature')
    plt.gca().invert_yaxis()
    plt.show()

def encode_scale(X,scaler,encoder,func):
    cat_cols = ['post_code','festius']
    num_cols = [feat for feat in X.columns if feat not in cat_cols]
    if func == 'train':
        encoded = encoder.fit_transform(X[cat_cols])
        encoded_columns = encoder.get_feature_names_out(cat_cols)
        encoded = pd.DataFrame(encoded, columns=encoded_columns,index=X.index)
        encoded[num_cols] = scaler.fit_transform(X[num_cols])
    elif func == 'test':
        encoded = encoder.transform(X[cat_cols])
        encoded_columns = encoder.get_feature_names_out(cat_cols)
        encoded = pd.DataFrame(encoded, columns=encoded_columns,index=X.index)
        encoded[num_cols] = scaler.transform(X[num_cols])
    return encoded

def cross_validation_model(X, y, model, k=5):
    kf = KFold(n_splits=k,shuffle=True,random_state=1998)
    mse = []
    r2 = []
    for train_index, test_index in kf.split(X):
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]
        
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        mse.append(mean_squared_error(y_test, y_pred))
        r2.append(r2_score(y_test,y_pred))
    mse = np.array(mse)
    r2 = np.array(r2)
    return {'r2_mean': r2.mean(), 'r2_std': r2.std(),'mse_mean': mse.mean(), 'mse_std': mse.std()}