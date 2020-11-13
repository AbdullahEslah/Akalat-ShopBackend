# import json # For showing response result in JSON
from foodtaskerapp.models import Customer, Driver

def create_user_by_type(backend, user, request, response, *args, **kwargs):
    if backend.name == 'facebook':
        # print(json.dumps(response)) # For showing response result in JSON
        avatar = 'https://graph.facebook.com/%s/picture?type=large' % response['id']

    if request['user_type'] == "driver" and not Driver.objects.filter(user_id=user.id):
        Driver.objects.create(user_id=user.id, avatar = avatar)
    elif request['user_type'] == "customer" and not Customer.objects.filter(user_id=user.id):
        Customer.objects.create(user_id=user.id, avatar = avatar)
