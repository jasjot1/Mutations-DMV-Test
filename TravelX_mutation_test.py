from urllib import response
import requests
import json
import random

#Authentication for DMV database
dmv_url = "https://gs65cnv4f8.execute-api.us-west-1.amazonaws.com/graphql/"
dmv_headers = {
  'Authorization': '6DKCZ8dLmag33zgPYkHVHopRCeJdA2WH2h3qpbFFQkMc',
  'content-type': 'application/json',
  'accept': 'application/json'
}

#Authentication for SS database
ss_url = "https://f0rc0vbvbk.execute-api.us-west-1.amazonaws.com/graphql/"
ss_headers = {
  'Authorization': '4LAG8LcuuTF4Zw1ro85e5Z2vB6NkMkc6L1Vq7FgD3tED',
  'content-type': 'application/json',
  'accept': 'application/json'
}

#Authentication for DOS database
dos_url = "https://vlwvzq88ce.execute-api.us-west-1.amazonaws.com/graphql/"
dos_headers = {
  'Authorization': '3ZRpSMsxRZprzstjLTLaBJChKpAJorQ6JaQZmvaZVxxL',
  'content-type': 'application/json',
  'accept': 'application/json'
}


#Adding data to the databases with mutatations:
def mutation_dmv(ssn,fname,lname,dob,dl,phone,street,city,state,zip,country,photo):
  payload="{\"query\":\"mutation addPerson {\\n    add_Person(\\n      input: {ssn:%s,\\n      first_name:\\\"%s\\\", \\n      last_name:\\\"%s\\\", \\n      dob:\\\"%s\\\",\\n      dl:\\\"%s\\\",\\n      phone_num:\\\"%s\\\",\\n      street_address: \\\"%s\\\",\\n      city: \\\"%s\\\",\\n      state: \\\"%s\\\",\\n      zip_code: \\\"%s\\\",\\n      country: \\\"%s\\\",\\n      photo: \\\"%s\\\"\\n      }\\n      syncMode: NODE_COMMITTED\\n    ) {\\n      result {\\n        ssn\\n        first_name\\n        last_name\\n        dob\\n        dl\\n        phone_num\\n        street_address\\n        city\\n        state\\n        zip_code\\n        country\\n        photo\\n      }\\n    }\\n  }\",\"variables\":{}}" % (ssn,fname,lname,dob,dl,phone,street,city,state,zip,country,photo)
  response = requests.request("POST", dmv_url, headers=dmv_headers, data=payload)
  print(response.text)
  
def mutation_ss(ssn,fname,lname,dob,street,city,state,zip,country,job):
  payload="{\"query\":\"mutation addPerson {\\n    add_Person(\\n      input: {ssn:%s,\\n      first_name:\\\"%s\\\", \\n      last_name:\\\"%s\\\", \\n      dob:\\\"%s\\\",\\n      street_address: \\\"%s\\\",\\n      city: \\\"%s\\\",\\n      state: \\\"%s\\\",\\n      zip_code: \\\"%s\\\",\\n      country: \\\"%s\\\",\\n      job: \\\"%s\\\"\\n      }\\n      syncMode: NODE_COMMITTED\\n    ) {\\n      result {\\n        ssn\\n        first_name\\n        last_name\\n        dob\\n        street_address\\n        city\\n        state\\n        zip_code\\n        country\\n        job\\n      }\\n    }\\n  }\",\"variables\":{}}" % (ssn,fname,lname,dob,street,city,state,zip,country,job)
  response = requests.request("POST", ss_url, headers=ss_headers, data=payload)
  print(response.text)

def mutation_dos(ssn,fname,lname,dob,passport_num,passport_exp,street,city,state,zip,country,photo):
  payload="{\"query\":\"mutation addPerson {\\n    add_Person(\\n      input: {ssn:%s,\\n      first_name:\\\"%s\\\", \\n      last_name:\\\"%s\\\", \\n      dob:\\\"%s\\\",\\n      passport_num: \\\"%s\\\"\\n      passport_exp: \\\"%s\\\"\\n      street_address: \\\"%s\\\",\\n      city: \\\"%s\\\",\\n      state: \\\"%s\\\",\\n      zip_code: \\\"%s\\\",\\n      country: \\\"%s\\\",\\n      photo: \\\"%s\\\"\\n      }\\n      syncMode: NODE_COMMITTED\\n    ) {\\n      result {\\n        ssn\\n        first_name\\n        last_name\\n        dob\\n        passport_num\\n        passport_exp\\n        street_address\\n        city\\n        state\\n        zip_code\\n        country\\n        photo\\n      }\\n    }\\n  }\",\"variables\":{}}" % (ssn,fname,lname,dob,passport_num,passport_exp,street,city,state,zip,country,photo)
  response = requests.request("POST", dos_url, headers=dos_headers, data=payload)
  print(response.text)

for x in range(4):
  #Get random people from random data api
  random_user_api = requests.get('https://random-data-api.com/api/v2/users')
  data = random_user_api.text
  parse_json = json.loads(data)

  dl = chr(random.randrange(65, 65+26)) + str(random.randrange(1000000,9999999))
  passport_num = random.randrange(100000000,999999999)
  passport_exp = str(random.randrange(1, 13)) + '/' + str(random.randrange(2022, 2032))

  #Parsing data from api 
  fname = parse_json['first_name']
  lname = parse_json['last_name']
  ssn = int(parse_json['social_insurance_number'])
  dob = parse_json['date_of_birth']
  phone = parse_json['phone_number']
  street = parse_json['address']['street_address']
  city = parse_json['address']['city']
  state = parse_json['address']['state']
  zip = parse_json['address']['zip_code']
  country = parse_json['address']['country']
  photo = parse_json['avatar']
  job = parse_json['employment']['title']

  mutation_dmv(ssn,fname,lname,dob,dl,phone,street,city,state,zip,country,photo)
  mutation_ss(ssn,fname,lname,dob,street,city,state,zip,country,job)
  mutation_dos(ssn,fname,lname,dob,passport_num,passport_exp,street,city,state,zip,country,photo)



