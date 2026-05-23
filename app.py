from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to Krupa Patel's Portfolio</h1>
    <p>Master's Student in Information Technology</p>
    <p>Skills: Python, SQL, Java</p>
    <p>Interested in AI Research and Software Development</p>
    """

if __name__ == "__main__":
    app.run(debug=True)
