import json

class Address():
    def __init__(self, address):
        self.co = address['C/o']
        self.house = address['House no.']
        self.street = address['Street']
        self.landmark = address['Landmark']
        self.area = address['Area']
        self.city = address['City']
        self.po = address['PO']
        self.district = address['District']
        self.sDistrict = address['Sub district']
        self.state = address['State']
        self.pin = address['Pincode']
    
    def toJSON(self):
        return json.dumps({
            "C/o": self.co,
            "House no.": self.house,
            "Street": self.street,
            "Landmark": self.landmark,
            "Area": self.area,
            "City": self.city,
            "PO": self.po,
            "District": self.district,
            "Sub district": self.sDistrict,
            "State": self.state,
            "Pincode": self.pin
        })

    def trim(self):
        if "SELF" in self.co.upper():
            self.co = ""

        if self.landmark:
            temp = self.landmark.upper().split()[0]
            if "NEAR" != temp and "OPP" != temp[:3]:
                self.landmark = f"Near: {self.landmark}"
        
        if self.street.upper() in self.area.upper():
            self.street = ""  

        if self.area.upper() in self.po.upper() or self.area.upper() in self.street.upper():
            self.area = ""

        
        dist = self.district.upper()
        if self.city.upper() in dist:
            self.city = ""
        if self.sDistrict.upper() in dist:
            self.sDistrict = ""
        if self.city and self.city.upper() in self.sDistrict.upper():
            self.city = ""

        if self.district.upper() in self.state.upper():
            self.state = ""

    def capital(self):
        self.co = self.co.title()
        self.street = self.street.capitalize()
        self.landmark = self.landmark.capitalize()
        self.area = self.area.capitalize()
        self.city = self.city.title()
        self.sDistrict = self.sDistrict.title()
        self.district = self.district.title()
        self.state = self.state.title()
    
    def optimize(self):
        self.trim()
        self.capital()