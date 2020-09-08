from flask import *
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=("POST", "GET"))
def show_tables():
    data = pd.read_csv('issues.csv', encoding='ISO-8859-1')
    # print(data.head(3))
    return render_template('index.html',tables=[data.to_html(classes='data',header="true")])

if __name__ == "__main__":
    app.run(debug=True)