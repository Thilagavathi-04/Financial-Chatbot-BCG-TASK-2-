from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load your financial data CSV (adjust path and filename)
# For demonstration, this line is commented out, uncomment and set your path
# data = pd.read_csv('data/apple_10k.csv')

# Example static data placeholders - replace with real calculations if needed
financial_summary = {
    "total_revenue": "$120 million",
    "net_income_change": "increased by $15 million",
    "total_assets": "$300 million",
    "current_ratio": "1.8",
    "cash_and_equivalents": "$50 million",
    "gross_profit_margin": "45%",
    "eps": "$2.35",
    "total_liabilities": "$180 million",
    "rnd_expense": "$25 million",
    "operating_expense_trend": "increased steadily by 5% annually over the last 3 years"
}

def get_response(user_query):
    query = user_query.lower().strip()

    if query == "what is the total revenue?":
        return f"The total revenue is {financial_summary['total_revenue']}."
    elif query == "how has net income changed over the last year?":
        return f"The net income has {financial_summary['net_income_change']} over the last year."
    elif query == "what are the total assets?":
        return f"The total assets amount to {financial_summary['total_assets']}."
    elif query == "what is the current ratio?":
        return f"The current ratio is {financial_summary['current_ratio']}, indicating good short-term liquidity."
    elif query == "how much cash and cash equivalents does the company have?":
        return f"The company holds {financial_summary['cash_and_equivalents']} in cash and cash equivalents."
    elif query == "what is the company's gross profit margin?":
        return f"The gross profit margin is {financial_summary['gross_profit_margin']}, showing efficient production costs management."
    elif query == "what is the earnings per share (eps)?":
        return f"The earnings per share (EPS) is {financial_summary['eps']}."
    elif query == "what are the total liabilities?":
        return f"Total liabilities stand at {financial_summary['total_liabilities']}."
    elif query == "how much did the company spend on r&d last year?":
        return f"The company invested {financial_summary['rnd_expense']} in research and development last year."
    elif query == "what is the trend of operating expenses over the last 3 years?":
        return f"Operating expenses have {financial_summary['operating_expense_trend']}."
    else:
        return "Sorry, I can only provide information on predefined financial queries."

@app.route("/", methods=["GET", "POST"])
def index():
    response = None
    if request.method == "POST":
        user_query = request.form.get("query")
        response = get_response(user_query)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
