from flask import Flask, request


import json
import random


app = Flask( __name__ )
"""
dao = DAO()
proxy = ProxySV()
recognizer = SighthoundRecognizer( "recognition/sighthoundkey.txt" )
manager = SRAManager( dao, recognizer, proxy )
print( "SRA init is done!" )
"""


@app.route('/')
def index():
    return "Welcome to the Motor Vehicle Recognition Service"

@app.route('/GeradorJson', methods=['GET']) #POST?
def GeradorJson():
    
    data = {
        "DataRecord": {
            "STATION": {
                "ID": 100,			
                "Geolocation": 10.4, 
                "Direction": 10.1,
                "MicSensitivity": 1.1,
                "Height": 1.1,			
                "Orientation": {
                    "Azimuth": 1.1,		
                    "Elevation": 1.1,	
                }
            },
            "timeStamp": 10.0,				
            "noise_levels": {
                "LAeq":[],
                "LAeq_Lin":[],
                "LAFmax_Lin":[],
                "LAFmax_Lin":[],
                "LFmax_Lin":[],	
                "LFmax_Lin":[],
                "LAFmin":[],
                "LAFmin_Lin":[],
                "LASmax":[],
                "LASmax_Lin":[],	
                "LASmin":[],
                "LASmin_Lin":[],
                "LFmin":[],
                "LFmin_Lin":[],
                "LCPeak":[],
                "LCPeak_Lin":[],	
                "LAE":[],
                "LAE_Lin ":[],
                "SEL":[],
                "SEL_Lin":[],
                "Impul":[],
                "Tonal":[],
                "LowFreq":[],
                "Freq1_0OctBands":{
                    "16":[],
                    "31.5":[],
                    "63":[],
                    "125":[],
                    "250":[],
                    "500":[],
                    "1000":[],
                    "2000":[],
                    "4000":[],
                    "8000":[],
                    "16000":[]
                },
                "Freq1_3OctBands": {
                    "16":[],
                    "20":[],
                    "25":[],
                    "31.5":[],
                    "40":[],
                    "50":[],
                    "63":[],
                    "80":[],
                    "100":[],
                    "125":[],
                    "160":[],
                    "200":[],
                    "250":[],
                    "315":[],
                    "400":[],
                    "500":[],
                    "630":[],
                    "800":[],
                    "1000":[],
                    "1250":[],
                    "1600":[],
                    "2000":[],
                    "2500":[],
                    "3150":[],
                    "4000":[],
                    "5000":[],
                    "6300":[],
                    "8000":[],
                    "10000":[],
                    "12500":[],
                    "16000":[],
                    "20000":[]
                }
            },
            "weather": {
                "Temperature":[],
                "AirSpeed":[],
                "AirDirection":[]		
            }
        }
    }

    r = random.randint(0,10)
    if (r >= 5) :
        for i in range(1,5):
            data["DataRecord"]["weather"]["Temperature"].append(30 + 
                            random.randint(0, 20))
    else:
        for i in range(1,5):
            data["DataRecord"]["weather"]["Temperature"].append(40 +
                                random.randint(0, 20))
            
    
    data["DataRecord"]["noise_levels"]["Impul"].append(r / 10)
    
    r1 = random.randint(0,10) / 10
    data["DataRecord"]["noise_levels"]["Tonal"].append(r1)    
       
    print("Pedido recebido!")    
    return data


"""
@app.route('/objects')
def getAllObjects():
    return allData
"""

"""
r = random.randint(0,10)
if (r >= 9) :
    data = {
        "ruido[db]" : 120
    }
    return data
else:
    data = {
        "ruido[db]" : 40
    }
    return data
"""


"""
Instructions for Json of Sound Meter

•	LAeq – Equivalent Continuous Sound Pressure Level 
•	LAFmax - max sound pressure level, Fast, A-weighted
•	LFmax - max sound pressure level, Fast, no weighted
•	LAFmin - min sound pressure level, Fast, A-weighted
•	LASmax – max sound pressure level, Slow, A-weighted
•	LASmin - min sound pressure level, Sçpw, A-weighted
•	LFmin - min sound pressure level, Fast, no weighted
•	LCPeak - peak sound pressure level, C-weighted
•	LAE – Sound Exposure Level, Slow, A-weighted
•	SEL - Sound Exposure Level, Slow, no weighted
•	Frequency Bands (1/1 octave, 1/3 octave), no weighted
•	Impul – Impulsivity [0.0-1.0]
•	Tonal – Tonality [0.0-1.0]
•	LowFreq - Low frequency sounds [0.0-1.0]

•	Time calendar
•	Time Analysis Length
•	Mic ID
o	ID
o	Geolocation
o	Direction
o	Calibration data (Sensitivity)
o	Height
•	Temperature
•	Air speed
•	Air direction

DataRecord – conjunto dados obtidos num intervalo de tempo, programável pelo utilizador

"""



"""
@app.route('/authenticate', methods=['POST'])
def authenticate():
    print( "sra#authenticate() - begin", file=sys.stderr, flush=True )
    
    # params
    username = request.json['username']
    password = request.json['password']
        
    print( f"username:{username}", file=sys.stderr, flush=True )
    print( f"password:{password}", file=sys.stderr, flush=True )
    
    response = manager.authenticateUser(username, password)
    
    print( "sra#authenticate() - end", file=sys.stderr, flush=True )
    
    return response


@app.route('/validateVehicle', methods=['POST'])
def validateVehicle():
    print( "sra#validateVehicle() - begin", file=sys.stderr, flush=True )
    
    # params
    userToken = request.json['userToken']
    vehicle = request.json['vehicle']
    detail = request.json['detail']

    # check permission
    permission = manager.checkPermission(userToken)
    
    if ( "error" in permission ):
        return permission

    response = manager.validateVehicle(vehicle, detail)
    
    print( "sra#validateVehicle() - end", file=sys.stderr, flush=True )

    return response


@app.route('/extractVehicle', methods=['POST'])
def extractVehicle():
    print( "sra#extractVehicle() - begin", file=sys.stderr, flush=True )
    
    # params
    userToken = request.json['userToken']
    vehicleImage = request.json['vehicleImage']
    
    print( f"extractVehicle: vehicleImage: {vehicleImage}", file=sys.stderr, flush=True )
    
    # check permission
    permission = manager.checkPermission(userToken)
    if ( "error" in permission ):
        return permission

    # extract features
    vehicle = manager.extractFeatures(vehicleImage)
    if( "error" in vehicle ):
        return vehicle

    # Get processed image
    visuals = ( vehicle[ 'vehicle_coordinates' ], vehicle[ 'licenseplate_coordinates' ] )
    img_processed = getImageProcessed(vehicleImage, visuals)
    response = {
            "image_processed": img_processed,
            "vehicle": vehicle
    }
    
    print( "sra#extractVehicle() - end", file=sys.stderr, flush=True )
    
    return response


@app.route('/extractAndValidateVehicle', methods=['POST'])
def extractAndValidateVehicle():
    print( "sra#extractAndValidateVehicle() - begin", file=sys.stderr, flush=True )
    
    # params
    userToken = base64.b64decode(request.json['userToken'])
    
    print( f"UserToken Type: {type(userToken)}", file=sys.stderr, flush=True )
    
    vehicleImage = request.json[ 'vehicleImage' ]
    detail = request.json[ 'detail' ]

    # check permission
    print( "Going to check permissions...", file=sys.stderr, flush=True )
    permission = manager.checkPermission( userToken )
    if ( "error" in permission ):
        return permission

    # extract features
    print( "Going to extract features...", file=sys.stderr, flush=True )
    vehicle = manager.extractFeatures(vehicleImage)
    if( "error" in vehicle ):
        return vehicle

    # Get processed image
    print( "Getting processed image...", file=sys.stderr, flush=True )
    visuals = ( vehicle['vehicle_coordinates'], vehicle['licenseplate_coordinates'] )
    
    img_processed = getImageProcessed(vehicleImage, visuals)
    
    print( "Got an image...", file=sys.stderr, flush=True )
    
    response = {}
    response[ "image_processed" ] = img_processed

    vehicle.pop( "vehicle_coordinates", None )
    vehicle.pop( "licenseplate_coordinates", None )
    
    print( "Going to validate vehicle...", file=sys.stderr, flush=True )
    
    response[ "validation" ] = manager.validateVehicle( vehicle, detail )

    print( "Vehicle validated", file=sys.stderr, flush=True )

    # add vehicle features
    response["vehicle"] = vehicle
    
    print( "sra#extractAndValidateVehicle() - end", file=sys.stderr, flush=True )
    
    return response


def getImageProcessed(vehicleImage, visuals):
    img_str = base64.b64decode(vehicleImage)
    nparr = np.fromstring(img_str, np.uint8)
    im_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    visualizer = VehicleVisualizer(im_np, visuals[0], visuals[1])
    visualizer.buildVisualImage()
    img_processed = base64.b64encode(visualizer.getImageBytes()).decode()
    return img_processed

"""
if __name__ == '__main__':
    app.run( host='0.0.0.0', port=4002, debug=True )
