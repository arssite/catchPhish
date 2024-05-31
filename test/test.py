import requests
import json

token_api_url = "http://localhost:8000/api/auth/token/"

data = {
    "client_id": "gHidZH6VLygdgfmrY1jknQ09hSk5wDcCVAqK58UM",
    "client_secret": "D4RMv1SAToewQrYhxyCaNNqz0KQG1gmvE6wR9YkUyv0s0sVM0Ph0TUisXPmwu4wJHhP6xX0pOM6ZI4Px5rDOCnmAhggeRvKsTV3ehaQn6S6c7dX5wIRFdzyFcExKveQd",
    "grant_type": "password",
    "username": "a@gmail.com",
    "password": "ankush",
}

# print(requests.post(token_api_url, data=data).text)

google_api = "http://localhost:8000/api/auth/convert-token"

data = {
    "grant_type": "convert_token",
    "backend": "google-oauth2",
    "client_id": "gHidZH6VLygdgfmrY1jknQ09hSk5wDcCVAqK58UM",
    "client_secret": "D4RMv1SAToewQrYhxyCaNNqz0KQG1gmvE6wR9YkUyv0s0sVM0Ph0TUisXPmwu4wJHhP6xX0pOM6ZI4Px5rDOCnmAhggeRvKsTV3ehaQn6S6c7dX5wIRFdzyFcExKveQd",
    "token": "ya29.a0AbVbY6PRaqKnnii_rj1zfNZaWRPd4tpQNLHwJPB0T8LV1Z0I7EkIpDU2git3XJ8Cz09E6WWOcsMzRsdqMy3NrtSI37CO39JzLfPb5BQib2SLKwh20j1GkFFLF54l5nAE9UGUYfvY055B2LKk7_-KiQk_DCUMaCgYKAYASARESFQFWKvPl01pS_O7OwOcCH67BNT-QPA0163",
}

# d = requests.post(google_api, data=data).json()
# print(d)
# access_token = d["access_token"]
# print(access_token)
headers = {
    "content-type": "application/json",
    "Authorization": "Bearer K1gh0tPEv9mmNoVu7WzbO2ZjmPDcJC",
}
# detect = "http://localhost:8000/api/delay/"
# print(requests.get(detect, headers=headers).text)



# detect_url = "http://localhost:8000/api/detect/"

# data = {
#     "url": "http://www.google.com/",
# }

# print(requests.post(detect_url, data=data).text)


# print(requests.get('www.google.com'))

# data = {
#     "client_id": "gHidZH6VLygdgfmrY1jknQ09hSk5wDcCVAqK58UM",
#     "client_secret": "D4RMv1SAToewQrYhxyCaNNqz0KQG1gmvE6wR9YkUyv0s0sVM0Ph0TUisXPmwu4wJHhP6xX0pOM6ZI4Px5rDOCnmAhggeRvKsTV3ehaQn6S6c7dX5wIRFdzyFcExKveQd",
#     "token": f"Bearer {access_token}",
# }

# revoke_url = "http://localhost:8000/api/auth/revoke-token/"


# print(requests.post(revoke_url,headers=headers, data=data).json)


# signup_url = "http://localhost:8000/api/signup/"

# data = {
#     "email": "a@b.com",
#     "password": "ankush",
#     'username': 'ankush37',
# }

# print(requests.post(signup_url, data=data).text)

report_url = "http://localhost:8000/api/report/"

url = {"url": "https://www.google.com/"}

# print(requests.post(report_url,headers=headers, data=json.dumps(url)).text)


page_url = "http://localhost:8000/api/stats/?page=1"
# print(requests.get(page_url, headers=headers).text)


detect = "http://localhost:8000/api/detect/"

data = {
    'url': "https://www.google.com/"
}
# print(requests.post(detect, data=data).text)