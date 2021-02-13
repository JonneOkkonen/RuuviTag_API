# RuuviTag API for Raspberry Pi

REST API for RuuviTag IoT Sensor. Requires Linux machine with Bluetooth. Designed to run on Raspberry Pi.

# Installation

## Gunicorn
```python
# Clone Repository
git clone https://github.com/JonneOkkonen/RuuviTag_API.git

# Install needed packages
pip install gunicorn
pip install flask
pip install ruuvitag_sensor

# Run in production mode with gunicorn
cd api
gunicorn --bind 0.0.0.0:5000 api:app

# Run in development mode
cd api
python api.py
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
[
    {
        "message": "Welcome to RuuviTag API. Check routing documentation from GitHub.",
        "status": "success"
    }
]
```

## Read Sensor Data

**URL** : `/ruuvitag/read/:name`

**Example** : `http://localhost:5000/ruuvitag/read/outside`

**Method** : `GET`

### Success Response

**Code** : `200 OK`

**Response Content**

```json
[
    {
        "message": {
            "acceleration": 1032.8397746020435,
            "acceleration_x": -362,
            "acceleration_y": -965,
            "acceleration_z": -67,
            "battery": 2797,
            "data_format": 3,
            "humidity": 96.0,
            "pressure": 1017.96,
            "temperature": -10.72
        },
        "status": "success"
    }
]
```

### Error Response

**Condition** : If 'name' is wrong

**Code** : `404 NOT FOUND`

**Content** :

```json
[
    {
        "message": "RuuviTag with name (name) not found.",
        "status": "error"
    }
]
```