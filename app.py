from flask import Flask, render_template, request, json, url_for


app = Flask(__name__)


with open('rates.json', 'r') as f:
    content= f.read()

def read_rates():
    data = json.loads(content)
    return data["rates"]


def get_rates_by_code(rates):
    by_code = {}
    for item in rates:
        code = item["code"]
        by_code[code] = item
    return by_code

rates = read_rates()
rates_by_code = get_rates_by_code(rates)

@app.route('/', methods=["GET", "POST"])
def kalk():
    return render_template("kalk.html")

@app.route('/conversion', methods=["POST"])
def conversion():

    currency_code = request.form["currency"]
    quantity = request.form["quantity"]

    bid_price = rates_by_code[currency_code]["bid"]
    
    conv = float(quantity) * bid_price
    return render_template("kalk.html", conv=conv, bid=bid_price, quantity=quantity)

if __name__ == "__main__":
    app.run(debug=True)