# RuuviTag API for Raspberry Pi

REST API for RuuviTag IoT Sensor. Requires Linux machine with Bluetooth. Designed to run on Raspberry Pi.

## Upcoming improvements

* Better support for multiple RuuviTags
* Docker image

# Installation

> :warning: **Works best with Python3**:Tested with Python 3.5.3.

## Gunicorn
```python
# Clone Repository
git clone https://github.com/JonneOkkonen/RuuviTag_API.git

# Install needed packages
sudo apt install gunicorn3
pip3 install flask
pip3 install flask-cors
pip3 install ruuvitag_sensor

# Run in production mode with gunicorn
cd api
gunicorn3 --bind 0.0.0.0:5000 api:app

# Run in development mode
cd api
python3 api.py
```

# Config

Config.json is located in API folder. Fill in all necessary information to it.

```json
{
    "ruuvitags":
    [
        {
            "index": 0,
            "name": "RuuviTag Name",
            "address": "00:00:00:00:00:01"
        }
    ],
    "server":
    {
        "ip": "0.0.0.0",
        "port": "5000"
    }
}

```

# API Routes

**URL** : `/`

**Example** : `http://localhost:5000/`

**Method** : `GET`

## Success Response

**Code** : `200 OK`

**Response Content**

```json
{
    "message": "Welcome to RuuviTag API. Check routing documentation from GitHub.",
    "status": "success"
}
```

## List all Ruuvitags

**URL** : `/ruuvitag/list`

**Example** : `http://localhost:5000/ruuvitag/list`

**Method** : `GET`

### Success Response

**Code** : `200 OK`

**Response Content**

```json
{
    "data": [
        {
            "address": "A1:B2:C3:D4:E5:F6",
            "name": "Ruuvitag name"
        }
    ],
    "status": "success"
}
```

## Read Sensor Data

**URL** : `/ruuvitag/read/:name`

**Example** : `http://localhost:5000/ruuvitag/read/outside`

**Method** : `GET`

### Success Response

**Code** : `200 OK`

**Response Content**

```json
{
    "data": {
        "acceleration": 1037.847773038031,
        "acceleration_x": -362,
        "acceleration_y": -970,
        "acceleration_z": -72,
        "battery": 2773,
        "humidity": 93.0,
        "pressure": 1012.84,
        "temperature": -10.76
    },
    "status": "success"
}
```

### Error Response

**Condition** : If 'name' is wrong

**Code** : `404 NOT FOUND`

**Content** :

```json
{
    "message": "RuuviTag with name (name) not found.",
    "status": "error"
}
```