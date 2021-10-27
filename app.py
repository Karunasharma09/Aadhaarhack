from flask import Flask, request, render_template
import json


def functionToOptimizeAddress():
    pass

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    origAdd = request.get_json()
    co = origAdd['C/o']
    house = origAdd['House no.']
    street = origAdd['Street']
    landmark = origAdd['Landmark']
    area = origAdd['Area']
    city = origAdd['City']
    po = origAdd['PO']
    district = origAdd['District']
    sDistrict = origAdd['Sub district']
    state = origAdd['State']
    pin = origAdd['Pincode']

    # Function call to optimise values

    return json.dumps({
        "C/o": co,
        "House no.": house,
        "Street": street,
        "Landmark": landmark,
        "Area": area,
        "City": city,
        "PO": po,
        "District": district,
        "Sub district": sDistrict,
        "State": state,
        "Pincode": pin
    })
    
@app.route('/')
def index():
    try:
        return render_template("index.html")
    except:
        return "Put index.html in the templates directory of repo"

if __name__ == '__main__':
    app.debug = True
    app.run()