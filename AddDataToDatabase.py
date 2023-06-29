import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceaccountkey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-bfff6-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "123":
        {
            "name": "Dinesh",
            "major": "Tech",
            "starting_year": "2022",
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2023-06-28 12:58:06"
        },
    "124":
        {
            "name": "Pradhyumn",
            "major": "Binding work",
            "starting_year": "2023",
            "total_attendance": 12,
            "standing": "Avg",
            "year": 1,
            "last_attendance_time": "2023-06-28 12:58:06"
        },
    "125":
        {
            "name": "Sai Charan",
            "major": "Research",
            "starting_year": "2022",
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2023-06-28 12:58:06"
        }

}


for key, value in data.items():
    ref.child(key).set(value)
