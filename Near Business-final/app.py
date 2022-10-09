from flask import Flask, render_template, request, jsonify
import requests, time
from decimal import Decimal
import urllib.request, json

app = Flask(__name__)

@app.route("/")  
def home():
	return render_template("index.html")

# api_key = AIzaSyBUlgvk_Wa46q16A_TdYOnIW9lMdGWtqCk

category_alias = 'hotdogs'

# Define API Key, Search Type, and header
MY_API_KEY = 'CMGfnejuoklneAxbMTNauLJ5TuMMHdUi46j2Bcj1_UljXWuyySNCmgjHJUqd2xTQxU_QzBE9r2TgYzx_G1A4TfQj46vRbi8VN5RIiqqTCDUmC9OjvaZFQx-zipxAY3Yx'
BUSINESS_PATH = 'https://api.yelp.com/v3/transactions/delivery/search'
HEADERS = {'Authorization': 'bearer %s' % MY_API_KEY}




@app.route('/search/', methods=['GET', 'POST'])
def search():
    geo_url = "https://maps.googleapis.com/maps/api/geocode/json?place_id=ChIJeRpOeF67j4AR9ydy_PIzPuM&key=AIzaSyBUlgvk_Wa46q16A_TdYOnIW9lMdGWtqCk"
    response = urllib.request.urlopen(geo_url)
    data = response.read()
    dict = json.loads(data)
    print(geo_url)
    print(dict)    
    if request.method == "GET":
        print("gettttttttttttttttt")
        data = request.get_json(force=True)
        print(',,,,,,,,,,,,,,,,,,,,,,,,,')
        print(data['formObj'])
        print(',,,,,,,,,,,,,,,,,,,,,,,,,')
        PARAMETERS = {
        'term': data['formObj']['kword'],
        'location': data['formObj']['location'],
        'radius': data['formObj']['distance'],
        'categories': data['formObj']['category'],
        }
        businesses_res = requests.get(url=BUSINESS_PATH, params=PARAMETERS, headers=HEADERS)
        # Convert response to a JSON String
        businesses_data = businesses_res.json()  
        # print the data
        businesses_dic = businesses_data['businesses']

        print("hello rendering")
        print(businesses_dic)
        print("hello rendering")
        return render_template("index.html", data=businesses_dic)
    elif request.method == "POST":
        print("posttttttttttttttttttttttttttttt")
        data = request.get_json(force=True)
        print(',,,,,,,,,,,,,,,,,,,,,,,,,')
        print(data['formObj'])
        print(',,,,,,,,,,,,,,,,,,,,,,,,,')
        PARAMETERS = {
        'term': data['formObj']['kword'],
        'location': data['formObj']['location'],
        'radius': data['formObj']['distance'],
        'categories': data['formObj']['category'],
        }
        businesses_res = requests.get(url=BUSINESS_PATH, params=PARAMETERS, headers=HEADERS)
        # Convert response to a JSON String
        businesses_data = businesses_res.json()  
        # print the data
        businesses_dic = businesses_data['businesses']
        print(businesses_dic)

        print("hello rendering")
        print(businesses_dic)
        print("hello rendering")
        return render_template("index.html", data=businesses_dic)
 
    return render_template("index.html")


# @app.route('/post', methods=["GET"])
# def testpost():
#      input_json = request.get_json(force=True) 
#      dictToReturn = {'text':input_json['text']}
#      return jsonify(dictToReturn)



@app.route('/handle_data', methods=['POST', 'GET'])
def handle_data():
    if request.method == "POST":
        formData = request.form
        print(formData)
        print("possssssssssssssssssssssssssssssssssssssssst")
        print(len(formData))
        print(formData['longitude'])
        print(request.method)
        
        if formData['longitude'] != '':
            PARAMETERS = {
            'term': formData['kword'],
            'latitude': float(formData['latitude']),
            'longitude': float(formData['longitude']),
            'radius': formData['distance'],
            'categories': formData['category'],
            }
            print(PARAMETERS)

            try:
                businesses_res = requests.get(url=BUSINESS_PATH, params=PARAMETERS, headers=HEADERS)
                # Convert response to a JSON String
                businesses_data = businesses_res.json()  
                print(businesses_data)
                # print the data
                businesses_dic = businesses_data['businesses']
                time.sleep(10)
                return render_template("index.html", data=businesses_dic)
            except:
                print("An exception occurred")
                businesses_dic = []
                return render_template("index.html", data=businesses_dic)

            
        else:
            PARAMETERS = {
            'term': formData['kword'],
            'location': formData['location'],
            'radius': formData['distance'],
            'categories': formData['category'],
            }
            print(PARAMETERS)
            
            try:
                businesses_res = requests.get(url=BUSINESS_PATH, params=PARAMETERS, headers=HEADERS)
                # Convert response to a JSON String
                businesses_data = businesses_res.json()  
                print(businesses_data)
                # print the data
                businesses_dic = businesses_data['businesses']
                time.sleep(10)
                return render_template("index.html", data=businesses_dic)
            except:
                print("An exception occurred")
                businesses_dic = []
                return render_template("index.html", data=businesses_dic)

            
    else:
        formData = request.form['kword']
        print(formData)
        print("getttttttttttttttttttttttttttt")
        print(request.method)
        return render_template("index.html")



@app.route('/search/<id>')
def display(id):
    path = f'https://api.yelp.com/v3/businesses/{id}'
    business_res = requests.get(url=path, headers=HEADERS)
        # Convert response to a JSON String
    business_data = business_res.json()  
        # print the data
    # print(business_data)
    return render_template("business.html", data=business_data)

if __name__ == "__main__":
    app.run()