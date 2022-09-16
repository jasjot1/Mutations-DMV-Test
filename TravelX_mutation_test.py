from urllib import response
import requests
import json

dmv_headers = {
  'Authorization': '9oc9KcZKoT6vF3mnHgenHRZrWnausfMfsWLqMTFu41SA',
  'content-type': 'application/json',
  'accept': 'application/json'
}
dmv_url = "https://akgifo8n61.execute-api.us-west-1.amazonaws.com/graphql/"

def mutation_dmv(id,fname,lname,ssn,dob,dl,phone,street,city,state,zip,country):
    payload="{\"query\":\"mutation addPerson {\\n    add_Person(\\n      input: {id: \\\"%s\\\", \\n      first_name:\\\"%s\\\", \\n      last_name:\\\"%s\\\", \\n      ssn:\\\"%s\\\",\\n      dob:\\\"%s\\\",\\n      dl:\\\"%s\\\",\\n      phone_num:\\\"%s\\\",\\n      street_address: \\\"%s\\\",\\n      city: \\\"%s\\\",\\n      state: \\\"%s\\\",\\n      zip_code: \\\"%s\\\",\\n      country: \\\"%s\\\"\\n      }\\n      syncMode: NODE_COMMITTED\\n    ) {\\n      result {\\n        _id\\n        first_name\\n        last_name\\n        ssn\\n        dob\\n        dl\\n        phone_num\\n        street_address\\n        city\\n        state\\n        zip_code\\n        country\\n      }\\n    }\\n  }\",\"variables\":{}}" % (id,fname,lname,ssn,dob,dl,phone,street,city,state,zip,country)

    requests.request("POST", dmv_url, headers=dmv_headers, data=payload)


for x in range(5):
    random_user_api = requests.get('https://random-data-api.com/api/v2/users')
    data = random_user_api.text
    parse_json = json.loads(data)

    id = parse_json['id']
    fname = parse_json['first_name']
    lname = parse_json['last_name']
    ssn = parse_json['social_insurance_number']
    dob = parse_json['date_of_birth']
    dl = parse_json['social_insurance_number'] #api doesn't give DL number so I just used social security for now
    phone = parse_json['phone_number']
    street = parse_json['address']['street_address']
    city = parse_json['address']['city']
    state = parse_json['address']['state']
    zip = parse_json['address']['zip_code']
    country = parse_json['address']['country']

    mutation_dmv(id,fname,lname,ssn,dob,dl,phone,street,city,state,zip,country)



