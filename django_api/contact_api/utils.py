import json

def parse_json_for_data(request):
    r = json.loads(request.body)
    full_name = r['full_name']
    email = r['email']
    address = r['address']
    phone = r['phone']
    return {'full_name': full_name, 'email': email, 'address': address, 'phone': phone}

def get_user_creds(request):
    username = request.META['HTTP_USERNAME']
    password = request.META['HTTP_PASSWORD']
    return {'username' : username, 'password': password}
