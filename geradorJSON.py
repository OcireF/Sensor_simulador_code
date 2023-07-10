from flask import Flask

import random


app = Flask( __name__ )


@app.route('/')
def index():
    return "Welcome to the Motor Vehicle Recognition Service"

@app.route('/GeradorJson', methods=['GET'])
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
                "LAFmax":[],
                "LAFmax_Lin":[],
                "LFmax":[],	
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
                "LAE_Lin":[],
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
    
    data["DataRecord"]["STATION"]["ID"] = random.randint(0, 1000000)
    data["DataRecord"]["STATION"]["Geolocation"] = random.randint(0, 1000000) / 10
    data["DataRecord"]["STATION"]["Direction"] = random.randint(0, 10000) / 10
    data["DataRecord"]["STATION"]["MicSensitivity"] = random.randint(0, 10000) / 10
    data["DataRecord"]["STATION"]["Height"] = random.randint(0, 10000) / 10
    data["DataRecord"]["STATION"]["Orientation"]["Azimuth"] = random.randint(0, 10000) / 10
    data["DataRecord"]["STATION"]["Orientation"]["Elevation"] = random.randint(0, 10000) / 10
    
    data["DataRecord"]["timeStamp"] = random.randint(0,10000) / 10
   
    data["DataRecord"]["noise_levels"]["LAeq"].append(random.randint(350, 750) / 10)
    
    data["DataRecord"]["noise_levels"]["LAFmax"].append(random.randint(1000, 1300) / 10)
    
    data["DataRecord"]["noise_levels"]["LFmax"].append(random.randint(1000, 1500) / 10)
    
    data["DataRecord"]["noise_levels"]["LAFmin"].append(random.randint(200, 600) / 10)
    
    data["DataRecord"]["noise_levels"]["LASmax"].append(random.randint(1000, 1400) / 10)
    
    data["DataRecord"]["noise_levels"]["LASmin"].append(random.randint(600, 1000) / 10)
    
    data["DataRecord"]["noise_levels"]["LFmin"].append(random.randint(500, 1000) / 10)
    
    data["DataRecord"]["noise_levels"]["LCPeak"].append(random.randint(100, 1700) / 10)
    
    data["DataRecord"]["noise_levels"]["LAE"].append(random.randint(300, 1100) / 10)
    
    data["DataRecord"]["noise_levels"]["SEL"].append(random.randint(400, 1100) / 10)
    
    data["DataRecord"]["noise_levels"]["Impul"].append(random.randint(0, 10) / 10)
    data["DataRecord"]["noise_levels"]["Tonal"].append(random.randint(0, 10) / 10)
    data["DataRecord"]["noise_levels"]["LowFreq"].append(random.randint(0, 10) / 10)
   
    data["DataRecord"]["weather"]["Temperature"].append(random.randint(0, 70))
            
    data["DataRecord"]["weather"]["AirSpeed"].append(random.randint(0, 70))
    data["DataRecord"]["weather"]["AirDirection"].append(random.randint(0, 70))
     
       
    print("Pedido recebido!")    
    return data




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

if __name__ == '__main__':
    app.run( host='0.0.0.0', port=4002, debug=True )
