from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>hello world!</h1>"

@app.route('/DVD/<int:dvd_id>')
def dvdbuying(dvd_id):
    return f"""
    <h2>Wow, you want to buy a DVD? The DVD#{dvd_id}?<h2>
    <img src="https://q4j2g5j9.stackpathcdn.com/ddg-dream/215d7d2ac93cfb837fa285e6324209135c525ac3.jpg">
    """




app.run()

