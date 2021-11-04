# import flask

from flask import Flask, url_for

# import jinja template engine
from flask import render_template

from flask import Response, request, jsonify

# create an app instance
app = Flask(__name__)

current_id = 11
phones = [
 {
   "id": 1,
   "model": "iPhone 12 Pro",
   "company": "Apple",
   "picture": "https://i.ibb.co/HxRFLhm/iphone-12-pro.jpg",
   "description": "The iPhone 12 Pro is Apple's high-end flagship devices with 5G, triple-lens cameras, LiDAR Scanners," + 
   "refreshed designs, and A14 chip. The Pro camera system takes low-light photography to the next level"+
   " — with an even bigger jump on iPhone 12 Pro. And Ceramic Shield delivers four times better drop performance.",
   "price": 1199.99,
   "year": 2020,
   "stores": [
     {
       "name": "Best Buy",
       "mark_as_deleted": False,
       "location": "Brooklyn"
     },
     {
       "name": "T Mobile",
       "mark_as_deleted": False,
       "location": "Manhattan"
     },
     {
        "name": "Verizon",
       "mark_as_deleted": False,
       "location": "Staten Island"
     }
   ]
  
  },

  {
   "id": 2,
   "model": "iPhone 12",
   "company": "Apple",
   "picture": "https://i.ibb.co/DrBR18V/iphone-12.jpg",
   "description": "The iPhone 12 is Apple's mainstream flagship iPhones for 2020. The phones come in 6.1-inch and 5.4-inch sizes with identical features,"+
    "including support for faster 5G cellular networks, OLED displays, improved cameras, and Apple's latest A14 chip, all in a completely refreshed design.",
   "price": 799.99,
   "year": 2020,
   "stores": [
     {
       "name": "Best Buy",
       "mark_as_deleted": False,
       "location": "Brooklyn"
     },
     {
       "name": "T Mobile",
       "mark_as_deleted": False,
       "location": "Manhattan"
     },
     {
        "name": "Verizon",
       "mark_as_deleted": False,
       "location": "Staten Island"
     }
   ]  
  },

  {
   "id": 3,
   "model": "iPhone 12 SE",
   "company": "Apple",
   "picture": "https://i.ibb.co/n0sPLDN/iphone-12-SE.jpg",
   "description": "iPhone SE adopts the iPhone 8's design, right down to the 4.7-inch screen surrounded by chunky bezels on the top and bottom of the screen. The iPhone SE features the same A13 Bionic processor as the iPhone 11 lineup. That enables the iPhone SE to take portrait shots and bring out highlights in faces using Smart HDR.",  
   "price": 399.99,
   "year": 2020,
   "stores": [
     {
       "name": "Kings Plaza",
       "mark_as_deleted": False,
       "location": "Brooklyn"
     },
     {
       "name": "T Mobile",
       "mark_as_deleted": False,
       "location": "Queens"
     },
     {
        "name": "Verizon",
       "mark_as_deleted": False,
       "location": "Manhattan"
     }
   ] 
  },

  {
   "id": 4,
   "model": "iPhone 11",
   "company": "Apple",
   "picture": "https://i.ibb.co/v1nBVn2/iphone-11.jpg",
   "description": "The iPhone 11 features a 6.1-inch display, a dual-lens camera, and an A13 Bionic chip."+ 
   "The phone has night mode camera and the body is made of more durable glass.The iPhone 11 does not include 3D Touch,"+ 
   "instead using Haptic Touch",
   "price": 899.99,
   "year": 2019,
   "stores": [
     {
       "name": "Target",
       "mark_as_deleted": False,
       "location": "Brooklyn"
     },
     {
       "name": "T Mobile",
       "mark_as_deleted": False,
       "location": "Manhattan"
     },
     {
        "name": "Verizon",
       "mark_as_deleted": False,
       "location": "Staten Island"
     }
   ] 
  },

  {
   "id": 5,
   "model": "iPhone XR",
   "company": "Apple",
   "picture": "https://i.ibb.co/q7WqP5c/iphone-XR.jpg",
   "description": "Apple's iPhone XR from 2018 is a budget alternative to Apple's latest lineup, featuring a 6.1-inch LCD,"+ 
   "a 12-megapixel single-lens rear camera, and an A12 chip. It has a glass body with aluminium frame and IP67 water and dust resistance."+ 
   "Instead of Touch ID, the iPhone XR uses the same TrueDepth camera system that's in the iPhone XS with faster, more efficient Face ID facial recognition for unlocking your device, making Apple Pay payments, and more.",
   "price": 499.99,
   "year": 2018,
   "stores": [
     {
       "name": "Target",
       "mark_as_deleted": False,
       "location": "Brooklyn"
     },
     {
       "name": "T Mobile",
       "mark_as_deleted": False,
       "location": "Manhattan"
     },
     {
        "name": "Verizon",
       "mark_as_deleted": False,
       "location": "Staten Island"
     }
   ] 
  },

  {
   "id": 6,
   "model": "Galaxy Note20 Ultra",
   "company": "Samsung",
   "picture": "https://i.ibb.co/Vtnnb0K/galaxy-note-2-ultra.jpg",
   "description": "The Galaxy Note 20 Ultra is the best phone in the series, offering just about everything you’d want from a phone." +
   "It comes with a massive 6.9-inch WQHD+ display that’s curved on the sides,"+ 
   "the latest Snapdragon 865 Plus or Exynos 990 processor and a 4,500mAh battery. It’s made of metal and glass and supports expandable storage.",
   "price": 1049.99,
   "year": 2020,
   "stores": [
     {
       "name": "Verizon",
       "mark_as_deleted": False,
       "location": "Brooklyn"
     },
     {
       "name": "T Mobile",
       "mark_as_deleted": False,
       "location": "Manhattan"
     },
     {
        "name": "Best Buy",
       "mark_as_deleted": False,
       "location": "Staten Island"
     }
   ] 
  },

  {
   "id": 7,
   "model": "Galaxy S20 FE 5G",
   "company": "Samsung",
   "picture": "https://i.ibb.co/yfBSwYX/galaxy-s20-FE.jpg",
   "description": "The Galaxy S20 features a flagship processor, expandable storage, an IP68 rating, a big AMOLED display," +
   "wireless charging, Wireless PowerShare, and a triple-lens rear camera."+ 
   "In addition to the usual specs and features, the five different color hues provide a wider range of options for users who want their phones to reflect their personalities.",
   "price": 649.99,
   "year": 2020,
   "stores": [
     {
       "name": "Verizon",
       "mark_as_deleted": False,
       "location": "Brooklyn"
     },
     {
       "name": "T Mobile",
       "mark_as_deleted": False,
       "location": "Manhattan"
     },
     {
        "name": "Best Buy",
       "mark_as_deleted": False,
       "location": "Staten Island"
     }
   ] 
  },

  {
   "id": 8,
   "model": "Galaxy A51 5G",
   "company": "Samsung",
   "picture": "https://i.ibb.co/KqNCsYC/galaxy-A51.jpg",
   "description": "The Galaxy A51 measures 6.24 by 2.90 by 0.31 inches (HWD) and comes in at 6.06 ounces. It’s light and just narrow enough to hold and use in one hand without any big issues. The front of phone is dominated by a near bezel-less 6.5-inch AMOLED display with a 20:9 aspect ratio and a small hole for the front-facing camera. Resolution comes in at 2,400 by 1,080, for a higher pixel density (405ppi).",
   "price": 299.99,
   "year": 2019,
   "stores": [
     {
       "name": "Kings Plaza",
       "mark_as_deleted": False,
       "location": "Brooklyn"
     },
     {
       "name": "T Mobile",
       "mark_as_deleted": False,
       "location": "Queens"
     },
     {
        "name": "Verizon",
       "mark_as_deleted": False,
       "location": "Manhattan"
     }
   ] 
  },

  {
   "id": 9,
   "model": "Google-Pixel 5",
   "company": "Google",
   "picture": "https://i.ibb.co/8PmV6T4/pixel-5.jpg",
   "description": "Google Pixel 5 runs the latest Android 11 OS, has a second ultrawide camera and bigger batteries than any previous Pixel phone." +
   "The Pixel 5 is equipped with a few more features: a 90Hz display, 2GB more RAM, a bigger battery and a water-resistant,"+
   "aluminum body. It also has wireless charging and reverse wireless charging.",
   "price": 649.99,
   "year": 2020,
   "stores": [
     {
       "name": "Verizon",
       "mark_as_deleted": False,
       "location": "Brooklyn"
     },
     {
       "name": "T Mobile",
       "mark_as_deleted": False,
       "location": "Manhattan"
     },
     {
        "name": "Best Buy",
       "mark_as_deleted": False,
       "location": "Staten Island"
     }
   ] 
  },

  {
   "id": 10,
   "model": "Google-Pixel 4A",
   "company": "Google",
   "picture": "https://i.ibb.co/LCLQ5n9/pixel-4a.jpg",
   "description": "Inside the Pixel 4A is Qualcomm's Snapdragon 730G chip with 6 gigabytes of RAM, a sizable step up from the Snapdragon 670 in the Pixel 3A." +
   "The Pixel 4A 5G adds an ultrawide camera to the mix (just like the Pixel 5), and they all share a nearly-identical 8-megapixel selfie camera.",
   "price": 1199.99,
   "year": 2020,
   "stores": [
     {
       "name": "Verizon",
       "mark_as_deleted": False,
       "location": "Brooklyn"
     },
     {
       "name": "T Mobile",
       "mark_as_deleted": False,
       "location": "Manhattan"
     },
     {
        "name": "Best Buy",
       "mark_as_deleted": False,
       "location": "Staten Island"
     }
   ] 
  }
]


# create a base route
@app.route('/')

# create home method
def home():

  global phones

  last5Index = len(phones) - 5

  last5Phones = phones[last5Index:]

  last5Phones = last5Phones[::-1]

  return render_template('home.html', phones = last5Phones)

# create a base route
@app.route('/create')

# create home method
def create():
  return render_template('create.html')

@app.route('/search')

def search():
  return render_template('search.html')

@app.route('/search_phone', methods=['POST'])

def search_phone():
  global phones

  search_data = request.get_json(force=True)

  found_phones = []

  if search_data:
    for phone in phones:
      if (search_data['query'].lower() in phone['model'].lower() 
        or search_data['query'].lower() in phone['company'].lower()):
        found_phones.append(phone)

  return jsonify(found_phones)

@app.route('/create_phone', methods=['POST'])

def create_phone():
  global phones
  global current_id

  phone_data = request.get_json(force=True)

  new_phone = {
    "id": current_id,
    'model': phone_data['model'],
    'company': phone_data['company'],
    'picture': phone_data['picture'],
    'description': phone_data['description'],
    'price': float(phone_data['price']),
    'year': int(phone_data['year']),
    'stores': phone_data['stores']
  }

  phones.append(new_phone)

  current_id += 1

  return jsonify({"id": current_id-1})

@app.route('/view/<int:id>')

def view(id):

  global phones

  view_phone = {}

  for phone in phones:
    if phone['id'] == int(id):
      view_phone = phone
      break

  return render_template('view.html', phone = view_phone)

@app.route('/edit-price', methods=['POST'])

def edit_price():
  global phones

  phone_data = request.get_json(force=True)

  for phone in phones:
    if phone['id'] == int(phone_data['id']):
      phone['price'] = float(phone_data['price'])
      break

  return "true"

@app.route('/delete-store', methods=['POST'])

def delete_store():
  global phones

  phone_data = request.get_json(force=True)

  for phone in phones:
    if phone['id'] == int(phone_data['id']):
      for store in phone['stores']:
        if store['name'] == phone_data['name']:
          store['mark_as_deleted'] = True
          break

  return "true"

@app.route('/undo-store', methods=['POST'])

def undo_store():
  global phones

  phone_data = request.get_json(force=True)

  for phone in phones:
    if phone['id'] == int(phone_data['id']):
      for store in phone['stores']:
        if store['name'] == phone_data['name']:
          store['mark_as_deleted'] = False
          break

  return "true"



