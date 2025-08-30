from dotenv import load_dotenv
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    # ... your existing logic
    return render_template("index.html", meal_plan=None, grocery_list=None)
# Load environment variables from .env file
load_dotenv()

if __name__ == "__main__":
    app.run(debug=True)