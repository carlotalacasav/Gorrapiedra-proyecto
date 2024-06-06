from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


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