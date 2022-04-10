from flask import Flask, render_template, request, json, url_for

app = Flask(__name__)

def read_rates():
    file = open("rates.json", "r")
    content = file.read()
    file.close()

    data = json.loads(content)
    return data["rates"]

def getRatesByCode(rates):
    byCode = {}
    for item in rates:
        code = item["code"]
        byCode[code] = item
    return byCode

rates = read_rates()
ratesByCode = getRatesByCode(rates)

@app.route('/', methods=["GET", "POST"])
def kalk():
    return render_template("kalk.html")

@app.route('/conversion', methods=["POST"])
def conversion():

    currency_code = request.form["currency"]
    quantity = request.form["quantity"]

    bidPrice = ratesByCode[currency_code]["bid"]
    
    conv = float(quantity) * bidPrice
    return render_template("kalk.html", conv=conv, bid=bidPrice, quantity=quantity)

if __name__ == "__main__":
    app.run(debug=True)
