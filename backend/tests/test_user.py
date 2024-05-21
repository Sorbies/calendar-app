import requests

BASE_URL = 'http://127.0.0.1:5000/auth'

def register_user(username, email, password):
    response = requests.post(f"{BASE_URL}/register", json={'username': username, 'email': email, 'password': password})
    print("Register:", response.json())

def login_user(username, password):
    response = requests.post(f"{BASE_URL}/login", json={'username': username, 'password': password})
    login_response = response.json()
    print("Login:", login_response)
    if response.status_code == 200 and 'token' in login_response:
        token = login_response['token']
        print("Token:", token)
        return token
    else:
        return None

def authenticated_request(token):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(f"{BASE_URL}/secured_route", headers=headers)
    print("Authenticated Request:", response.json())

if __name__ == '__main__':
    register_user('newuser3', 'newuser3@example.com', 'password123456')
    register_user('newuser2', 'newuser2@example.com', 'password12345')
    register_user('newuser1', 'newuser1@example.com', 'password1234')
    register_user('newuser', 'newuser@example.com', 'password123')
    token = login_user('newuser3', 'password123456')
    if token:
        authenticated_request(token)

        

# import requests

# BASE_URL = 'http://127.0.0.1:5000/auth'

# def register_user(username, email, password):
#     response = requests.post(f"{BASE_URL}/register", json={'username': username, 'email': email, 'password': password})
#     print("Register:", response.json())

# def login_user(username, password):
#     response = requests.post(f"{BASE_URL}/login", json={'username': username, 'password': password})
#     login_response = response.json()
#     print("Login:", login_response)
#     if response.status_code == 200 and 'token' in login_response:
#         token = login_response['token']
#         print("Token:", token)
#         return token
#     else:
#         return None

# def authenticated_request(token):
#     headers = {'Authorization': f'Bearer {token}'}
#     response = requests.get(f"{BASE_URL}/secured_route", headers=headers)
#     print("Authenticated Request:", response.json())

# if __name__ == '__main__':
#     register_user('newuser3', 'newuser3@example.com', 'password123456')
#     token = login_user('newuser3', 'password123456')
#     if token:
#         authenticated_request(token)



# import requests

# BASE_URL = 'http://127.0.0.1:5000/auth'

# def register_user(username, email, password):
#     response = requests.post(f"{BASE_URL}/register", json={'username': username, 'email': email, 'password': password})
#     print("Register:", response.json())

# def login_user(username, password):
#     response = requests.post(f"{BASE_URL}/login", json={'username': username, 'password': password})
#     login_response = response.json()
#     print("Login:", login_response)
#     # Check if login was successful and token is in the response
#     if response.status_code == 200 and 'token' in login_response:
#         token = login_response['token']
#         print("Token:", token)
#         return token
#     else:
#         return None

# def authenticated_request(token):
#     # Example of an authenticated request using the token
#     headers = {'Authorization': f'Bearer {token}'}
#     # Replace '/secured_route' with your actual route that requires authentication
#     response = requests.get(f"{BASE_URL}/secured_route", headers=headers)
#     print("Authenticated Request:", response.json())

# if __name__ == '__main__':
#     register_user('newuser2', 'newuser2@example.com', 'password12345')
#     token = login_user('newuser2', 'password12345')
#     if token:
#         authenticated_request(token)





# import requests

# BASE_URL = 'http://127.0.0.1:5000/auth'

# def register_user(username, email, password):
#     response = requests.post(f"{BASE_URL}/register", json={'username': username, 'email': email, 'password': password})
#     print("Register:", response.json())

# def login_user(username, password):
#     response = requests.post(f"{BASE_URL}/login", json={'username': username, 'password': password})
#     print("Login:", response.json())

# if __name__ == '__main__':
#     register_user('newuser', 'newuser@example.com', 'password123')
# #    login_user('newuser', 'password123')