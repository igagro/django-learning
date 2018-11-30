# from decouple import config

# import sys
# import psycopg2

# POSTGRE_PASS = config('POSTGRE_PASS')
# con = None

# try:

#     con = psycopg2.connect(database="django-learning", user="postgres",
#                            password=POSTGRE_PASS, host="localhost", port="5432")

#     cur = con.cursor()
#     cur.execute("SELECT * FROM auth_user;")

#     rows = cur.fetchall()

#     for row in rows:
#         print(row)

#     print('end of test.')

# except psycopg2.DatabaseError:
#     print('Error %s' % e)
#     sys.exit(1)

# finally:

#     if con:
#         con.close()


import json
import requests
import os

AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/login/"
REFRESH_ENDPOINT = "http://127.0.0.1:8000/api/auth/jwt/refresh/"
ENDPOINT = "http://127.0.0.1:8000/api/test/"

headers = {
    "Content-Type": "application/json",
    # "Authorization": "JWT " + 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Iml2YW5nYSIsIm9yaWdfaWF0IjoxNTQzNTY5MzY2LCJlbWFpbCI6Iml2YW5nYUBtYWVzdHJhbHNvbHV0aW9ucy5jb20iLCJleHAiOjE1NDM1Njk2NjYsInVzZXJfaWQiOjF9.3PIXJwzuyQ-C7mLi6niaKlN-iRbUKTJiPFBuwCIOBgQ'
}

data = {
    'username': 'ivanga@maestralsolutions.com',
    'password': 'djangoapp'
}

r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
token = r.json()  # ['token']

print(token)

# print(token)

# refresh_data = {
#     'token': token
# }


# new_response = requests.post(
#     REFRESH_ENDPOINT, data=json.dumps(refresh_data), headers=headers)
# new_token = new_response.json()  # ['token']

# print(new_token)
