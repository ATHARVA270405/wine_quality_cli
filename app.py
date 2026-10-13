
import joblib
import numpy as np

# Load the saved, tuned KNN model
model = joblib.load("knn_model.pkl")

# Keep this order identical to the training dataset
FEATURES = [
    "fixed acidity",
    "volatile acidity",
    "citric acid",
    "residual sugar",
    "chlorides",
    "free sulfur dioxide",
    "total sulfur dioxide",
    "density",
    "pH",
    "sulphates",
    "alcohol"
]


def get_wine_input():
    values = []

    print("\nEnter the wine characteristics")
    print("-" * 35)

    for feature in FEATURES:
        while True:
            try:
                value = float(input(f"{feature}: "))

                if not np.isfinite(value):
                    print("Enter a valid finite number.")
                    continue

                values.append(value)
                break

            except ValueError:
                print("Invalid input. Enter a number.")

    return np.array(values).reshape(1, -1)


def predict_quality():
    wine_data = get_wine_input()

    # Predict using the saved model
    prediction = model.predict(wine_data)[0]

    print("\n" + "=" * 35)
    print("WINE QUALITY PREDICTION")
    print("=" * 35)
    print(f"Predicted quality score: {prediction}")
    print("=" * 35)


def main():
    print("Welcome to the Wine Quality Predictor!")

    while True:
        try:
            predict_quality()
        except Exception as error:
            print(f"Prediction error: {error}")

        again = input(
            "\nPredict another wine? (yes/no): "
        ).strip().lower()

        if again not in ("yes", "y"):
            print("Thank you for using the application!")
            break


if __name__ == "__main__":
    main()
