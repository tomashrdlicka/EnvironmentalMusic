# Bachelor Project for Queen Mary University of London - Computer Science Degree

## Project Overview
This project demonstrates an innovative approach to integrating environmental and motion data into a custom sound engine. Below are detailed instructions on setting up and running the instrument.

## Project Construction Overview (Click on image)
[![Watch the video](https://img.youtube.com/vi/osoEanJy1pE/maxresdefault.jpg)](https://www.youtube.com/watch?v=osoEanJy1pE)

## Run the Instrument
Follow the steps below in the intended order to set up and run the instrument.

### A) Weather Client
1. Open `OSCWeatherClient.py` located in the `Environment_data_collection` folder.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Replace the placeholder `YYY` at the top of the file with your API key from [OpenWeatherMap](https://openweathermap.org/api).  
4. Replace the placeholder `XXX` at the top of the file with your computer’s current IP address.  
5. Run the program:
  ```bash
  python OSCWeatherClient.py
  ```
### B) Time Client
1. Open `OSCTimeClient.py` in the `Environment_data_collection` folder.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt ```
3. Replace the placeholder XXX at the top of the file with your computer’s current IP address.
4. Run the program in a separate terminal window:
```bash
python OSCTimeClient.py
```

### C) GyrOSC
1. Install **GyrOSC** from the App Store.
2. Launch the app.
3. Enter your computer's current IP address in the **Target IP address** field.
4. Set the **Port** to `6000`.
5. Enable **Gyroscope** and run it in the background.

### D) Sound Engine
1. Install Pure Data from this link.
2. Run Sound_Engine.pd located in the soundEngine folder.
3. Press the bang button for the Time_Input, Motion_Input, and Environment_Input.
4. Activate the sound engine by toggling the switch.


### The instrument is now ready to use.

## Playthrough DEMO (Click on image):
[![Watch the video](https://img.youtube.com/vi/12AitBk8yDo/maxresdefault.jpg)](https://www.youtube.com/watch?v=12AitBk8yDo)
