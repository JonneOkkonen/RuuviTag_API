from ruuvitag_sensor.ruuvi import RuuviTagSensor, RunFlag
import time

def listener(data, tag, interval):
    try:
        # RunFlag for stopping execution at desired time
        run_flag = RunFlag()
        def handle_data(values):
            # Send data to main process
            data[tag["index"]] = values[1]
            run_flag.running = False # Stop process
            time.sleep(interval) # Wait interval
            run_flag.running = True # Continue process

        RuuviTagSensor.get_datas(handle_data, tag["address"], run_flag)
    except ValueError:
        data[tag["index"]] = "RuuviTag address is not correct."
    except Exception as e:
        data[tag["index"]] = "Error happened while trying to read RuuviTag values."
        print(e)