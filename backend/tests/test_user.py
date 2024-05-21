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
    register_user('rana', 'rana@example.com', 'pass4rana')
    # register_user('user2', 'user2@example.com', 'passwordabcde')
    # register_user('user1', 'user1@example.com', 'passwordabcd')
    # register_user('user', 'user@example.com', 'passwordabc')
    token = login_user('rana', 'pass4rana')
    if token:
        authenticated_request(token)

        

