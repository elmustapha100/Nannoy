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
with open('serialization.json','w') as write_file :
    print(json.dump(user_id , write_file))