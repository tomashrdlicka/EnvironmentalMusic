How to run the instrument:
Follow the instructions in the intended order

A) Weather Client
1. Open OSCWeatherClient.py in the Environment_data_collection folder
2. Install required dependencies 
3. Replace the field marked YYY on top of the file with your API key from https://openweathermap.org/api
4. Replace the field marked XXX on top of the file with the computer’s current IP address
5. Run the program


B) Time Client
1. Open OSCTimeClient.py in the Environment_data_collection folder
2. Install required dependencies 
3. Replace the field marked XXX on top of the file with the computer’s current IP address
4. Run the program in another terminal window


C) GyrOSC
1. Install GyrOSC from AppStore 
2 Run the app
3. Insert your computer’s current IP address in “Target IP address”
4. Type 6000 in “Port”
5. Turn on Gyroscope and Run in Background

D) Sound Engine
1. Install Pure Data from https://puredata.info/downloads
2. Run Sound_Engine.pd in the soundEngine folder
3. Press bang on the Time_Input, Motion_Input and Environment_Input
4. Turn the engine on using the toggle

The instrument is now ready to be used



