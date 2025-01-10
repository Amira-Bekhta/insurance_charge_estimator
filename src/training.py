from data_load import load
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor




data = load("processed", "processed", True)

X = data.iloc[:, :-1]
y = data.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestRegressor()
model.fit(X_train, y_train)

joblib.dump(model, "model/model.pkl")
joblib.dump(X_test, "model/X_test.pkl")
joblib.dump(y_test, "model/y_test.pkl")

