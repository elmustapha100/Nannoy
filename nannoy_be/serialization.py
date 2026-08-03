#serialization : The process of converting data into JSON format ,that involves the process of transforming 
#data into series of bytes for storage over a network 

import json 
user_id = {
    "name":"Juliet",
    "student_id":2408060552,
    "level":"200",
     "name" : "EL Mustapha",
    "hobbies" : ["travelling","Barca","logic"],
    "career":["Mathematician","software dev"],

    "friends": [
        {"name": "Demilade",
        "hobbies" : ["Gaming","flirting"]
    },
    {
        "name" : "Opemi",
        "hobbies" : ["K-drama","writing"]
    }
    ]
}
# serializing the data into a JSON string format
user_id_json = json.dumps(user_id)
print(user_id_json)

#converting JSON string back to Python 
user_id_python = json.loads(user_id_json)
print(user_id_python)
print(type(user_id_json))
print(type(user_id_python))



