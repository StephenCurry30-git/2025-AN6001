from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return (render_template("index.html"))

@app.route("/prediction",methods=["GET","POST"])
def main():
    q = request.form.get("q")
    return(render_template("p.html"))
if __name__ == "__main__":
    app.run()