# Wine Quality Prediction using Tuned KNN

## 📌 Project Overview

This project is a simple command-line application that predicts wine quality based on its physicochemical properties using a **tuned K-Nearest Neighbors (KNN) regression or classification model**.

The model is trained and tuned using cross-validation. The best-performing model is saved and reused to make predictions from user-provided inputs without retraining every time the application runs.

## 🎯 Objectives

- Implement the K-Nearest Neighbors algorithm for wine quality prediction.
- Tune KNN hyperparameters using cross-validation.
- Accept wine characteristics through a command-line interface.
- Predict wine quality using the saved, tuned model.
- Understand model persistence and real-time predictions.

## 🛠️ Technologies Used

- Python
- NumPy
- Scikit-learn
- Joblib
- Wine Quality Dataset

## 📊 Dataset Description

The model uses physicochemical properties of wine to predict its quality score.

The input features are:

| Feature | Description |
|---|---|
| Fixed Acidity | Non-volatile acids present in wine |
| Volatile Acidity | Volatile acids, mainly acetic acid |
| Citric Acid | Citric acid content |
| Residual Sugar | Sugar remaining after fermentation |
| Chlorides | Salt content |
| Free Sulfur Dioxide | Free sulfur dioxide concentration |
| Total Sulfur Dioxide | Total sulfur dioxide concentration |
| Density | Density of the wine |
| pH | Acidity or alkalinity level |
| Sulphates | Sulphate content |
| Alcohol | Alcohol percentage by volume |

**Target variable:** Wine quality score.

## 🧠 Machine Learning Workflow

1. Load the Wine Quality dataset.
2. Separate input features and the target variable.
3. Split the data into training and testing sets.
4. Scale the features when required.
5. Train and tune the KNN model using cross-validation.
6. Select the best model based on the chosen evaluation metric.
7. Save the tuned model using Joblib.
8. Load the saved model in the CLI application.
9. Accept new wine characteristics from the user.
10. Predict and display the wine quality score.

## ⚙️ Hyperparameter Tuning

KNN performance depends on the choice of hyperparameters.

The tuning process may evaluate:

- **`n_neighbors`**: Number of nearest neighbors considered.
- **`weights`**: Whether neighbors contribute equally or according to distance.
- **`metric`**: Distance measure used to find neighboring samples.

GridSearchCV with cross-validation can be used to select the best combination. The actual parameters depend on the search grid used during training.

## 📁 Project Structure

```text
wine_quality_cli/
│
├── knn_tuning.ipynb   # Model training and hyperparameter tuning
├── knn_model.pkl      # Saved tuned KNN model or pipeline
├── app.py             # Command-line prediction application
└── README.md          # Project documentation
```

## 💻 Installation and Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd wine_quality_cli
```

Replace `<your-repository-url>` with your actual GitHub repository URL.

### 2. Install dependencies

```bash
pip install numpy scikit-learn joblib
```

### 3. Ensure the model file exists

Make sure `knn_model.pkl` is present in the project directory. If it is not available, run the training and tuning notebook and save the fitted best estimator before launching the application.

### 4. Run the application

```bash
python app.py
```

## 🚀 Usage

The application prompts the user to enter the 11 wine characteristics one by one.

Example input:

```text
fixed acidity: 7.4
volatile acidity: 0.70
citric acid: 0.00
residual sugar: 1.9
chlorides: 0.076
free sulfur dioxide: 11
total sulfur dioxide: 34
density: 0.9978
pH: 3.51
sulphates: 0.56
alcohol: 9.4
```

Example output:

```text
===================================
WINE QUALITY PREDICTION
===================================
Predicted quality score: 5
===================================
```

*Note: The displayed score is illustrative. The actual prediction depends on the saved model.*

The application also allows users to predict another wine without restarting the program.

## 📈 Model Evaluation

Evaluate the tuned model using an appropriate held-out test set.

For a classification model, useful metrics include:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix

For a regression model, useful metrics include:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² score

Add your actual evaluation results here after running your notebook. The appropriate metrics depend on whether wine quality is modeled as a classification or regression problem.

## 💡 Key Learnings

- Understanding the KNN algorithm and distance-based prediction.
- Selecting hyperparameters using cross-validation.
- Understanding the importance of feature scaling in KNN.
- Saving and loading trained machine learning models.
- Integrating a machine learning model into a command-line application.
- Handling user input and basic input validation.

## 🔮 Future Improvements

- Add stronger input validation based on valid feature ranges.
- Display model evaluation metrics.
- Provide an explanation of the nearest training samples.
- Add automated tests for the prediction function.
- Develop a web interface using Flask or Streamlit.
- Improve reproducibility by recording dataset versions and model parameters.

## ⚠️ Limitations

- Predictions depend on the quality and distribution of the training data.
- The model's performance depends on feature preprocessing and hyperparameter selection.
- Predicted quality scores are estimates and do not replace laboratory analysis or professional wine assessment.
- The model file must be compatible with the scikit-learn environment used to load it.

## 👨‍💻 Author

**Atharva Pundkar**

GitHub: [atharva270405](https://github.com/atharva270405)

---

If you find this project useful, consider starring the repository on GitHub.
