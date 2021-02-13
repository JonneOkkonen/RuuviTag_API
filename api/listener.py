from ruuvitag_sensor.ruuvi import RuuviTagSensor

def listener(data, tag, interval):
    while(1):
        try:
            def handle_data(values):
                # Send data to main process
                data[tag["index"]] = values[1]

            RuuviTagSensor.get_datas(handle_data, tag["address"])
        except ValueError:
            state = "RuuviTag address is not correct."
        except Exception as e:
            state = "Error happened while trying to read RuuviTag values."
            print(e)