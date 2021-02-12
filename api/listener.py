import time
from ruuvitag_sensor.ruuvitag import RuuviTag

def listener(data, interval, tag):
    while(1):
        try:
            # Get Ruuvitag data
            sensor = RuuviTag(tag["address"]).update()
        except ValueError:
            sensor = "RuuviTag address is not correct."
        except:
            sensor = "Error happened while trying to read RuuviTag values."
        # Send data to main process
        data[tag["index"]] = sensor
        time.sleep(interval)