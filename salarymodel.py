import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import joblib
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge
df=pd.read_csv("salary.csv")
print(df)
x=df[["experience","skills_score","education_level"]]
y=df["salary"]
poly=PolynomialFeatures(degree=2)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)


x_train_poly=poly.fit_transform(x_train)
x_test_poly=poly.transform(x_test)


model=Ridge(alpha=1.0)
model.fit(x_train,y_train)
pred=model.predict(x_test)
print(pred)
err=mean_absolute_error(pred,y_test.values)
print(err)
joblib.dump(model,"salary_model.pkl")


#linear =1449.13383
#with poly=1250
#ridge=995 so i can use this