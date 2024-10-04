import argparse
from datetime import date, datetime
import random
import time

from pythonosc import osc_message_builder
from pythonosc import udp_client

if __name__ == "__main__":

    isConnected = True

    # Replace XXXXX with computer's current IP address
    client = udp_client.SimpleUDPClient("192.168.1.111", 5000)

    while isConnected:
        now = datetime.now()
        today = date.today()
        today = str(today)
        year = today[0:4]
        month = today[5:7]
        day = today[8:10]

        current_time = now.strftime("%H:%M:%S")
        hour = current_time[0:2]
        tenMinute = current_time[3:4]
        minute = current_time[4:5]
        tenSecond = current_time[6:7]
        second = current_time[7:8]

        keyScale = (int(year) + int(month) + int(day) + int(hour)) % 13
        bassChord = (int(hour) + int(tenMinute)) % 6
        midChord = (int(tenMinute) + int(minute)) % 6
        upChord = (int(minute) + int(tenSecond)) % 6

        client.send_message("/keyScale", keyScale)
        client.send_message("/bassChord", bassChord)
        client.send_message("/midChord", midChord)
        client.send_message("/upChord", upChord)

        time.sleep(10)
