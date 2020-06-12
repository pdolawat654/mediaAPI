from django.shortcuts import render


def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.eyJ1IjoicGRvbGF3YXQ2NTQiLCJhIjoiY2theG0yNTM5MDU5bTMycGk0YzR1Z2xiaCJ9.aFnu0E4s9XXI3MpdnobOUQ'
    return render(request, 'maps/default.html', 
                  { 'mapbox_access_token': mapbox_access_token })