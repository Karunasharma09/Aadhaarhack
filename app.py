from flask import Flask, request, render_template
from address import Address

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    address = Address(request.get_json())

    # Function call to optimise values
    address.optimize()

    return address.toJSON()
    
@app.route('/')
def index():
    try:
        return render_template("index.html")
    except:
        return "Put index.html in the templates directory of repo"

if __name__ == '__main__':
    app.run()