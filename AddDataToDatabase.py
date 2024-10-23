import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://facereg-attendance-system-default-rtdb.firebaseio.com/",
    'storageBucket':"facereg-attendance-system.appspot.com"
})

ref = db.reference('Students')

data = {
    "101425":
        {
            "name": "Nyquist Ndubuisi Nwaukwa",
            "major": "Computer science",
            "starting_year": 2018,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "101904":
        {
            "name": "Celestina George",
            "major": "Computer science",
            "starting_year": 2018,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "102032":
        {
            "name": "Nkemdirim Chinedu",
            "major": "Computer science",
            "starting_year": 2018,
            "total_attendance": 12,
            "standing": "B",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "102051":
        {
            "name": "Peter Chikwendu",
            "major": "Computer science",
            "starting_year": 2018,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)
