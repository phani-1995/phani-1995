import pandas as pd
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')
df = pd.read_csv("D:\\FLASK\\Data.csv")
df1 = df['Gender'].value_counts()
print(df1)


@app.route("/")
def chart():
    return render_template('index.html')


@app.route("/data")
def data():
    df2 = df1.to_dict()
    return df2


if __name__ == "__main__":
    app.run(debug=True)
