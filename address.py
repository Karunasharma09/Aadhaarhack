import json

class Address():
    def __init__(self, address):
        self.uid = address['UID']
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
        self.name = address['Name']
        self.email = address['Email']
        self.phone = address['Phone']
    
    def toJSON(self):
        add = {}
        add['UID']= self.uid
        add['Name']= self.name
        if self.co:
            add['C/o']= self.co
        add['House no.']= self.house
        if self.street:
            add['Street']= self.street
        add['Landmark']= self.landmark
        if self.area:
            add['Area']= self.area
        if self.city:
            add['City']= self.city
        add['PO']= self.po
        add['District']= self.district
        if self.sDistrict:
            add['Sub district']= self.sDistrict
        if self.state:
            add['State']= self.state
        add['Pincode']= self.pin
        add['Email']= self.email
        add['Phone']= self.phone
        return json.dumps(add)

    def trim(self):
        if "SELF" in self.co.upper():
            self.co = ""

        if self.area.upper() in self.house.upper():
            self.house = self.house.lower().replace(" "+self.area.lower(), "")
        elif self.city.upper() in self.house.upper():
            self.house = self.house.lower().replace(" "+self.city.lower(), "")

        if self.landmark:
            temp = self.landmark.upper().split()[0]
            if "NEAR" != temp and "OPP" != temp[:3]:
                self.landmark = f"Near: {self.landmark}"
        
        if self.city.upper() in self.po.upper():
            self.po = self.po.lower().replace(" "+self.city.lower(), "")
        elif self.district.upper() in self.po.upper():
            self.po = self.po.lower().replace(" "+self.district.lower(), "")
        elif self.sDistrict.upper() in self.po.upper():
            self.po = self.po.lower().replace(" "+self.sDistrict.lower(), "")
        elif self.state.upper() in self.po.upper():
            self.po = self.po.lower().replace(" "+self.state.lower(), "")
        if self.po[-1] == ",":
            self.po = self.po[:-1]

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
        self.house = self.house.upper()
        self.street = self.street.capitalize()
        self.landmark = self.landmark.title()
        self.po = self.po.title()
        self.area = self.area.capitalize()
        self.city = self.city.title()
        self.sDistrict = self.sDistrict.title()
        self.district = self.district.title()
        self.state = self.state.title()
        self.name = self.name.title()
        self.email = self.email.lower()
    
    def optimize(self):
        self.trim()
        self.capital()