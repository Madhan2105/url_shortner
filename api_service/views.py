from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import UrlModel
from .serializers import UrlSerializer
import string
import random



'''
    Route  which redirects the short URL to it's
    original URL when it's valid
'''
@require_http_methods(['GET'])
def redirect_site(request, slug):
    # Check the Table for the token entered by the user
    try:
        service = UrlModel.objects.get(slug=slug)
        url = service.url
        if not url.startswith('http://') and not url.startswith('https://'):
            url = f'http://{url}'
        return HttpResponseRedirect(url)
    #Throw an Error Message when it's not valid
    except Exception as e:      
        return JsonResponse({"error":"No url found"}, safe=False) 

'''
    Route which performs Register,update,delete and fetch URL
'''
@api_view(['GET','POST','PUT','DELETE'])
def url_shortener(request,optional_slug=None):
    try:
        #GET method 
        if request.method == 'GET':
            #Fetch all value from Database when no token is passed
            if optional_slug == None:
                urls = UrlModel.objects.filter()
            else:
                urls = UrlModel.objects.filter(slug=optional_slug)
            data = UrlSerializer(urls, many=True).data
            return JsonResponse(data, safe=False)
        #POST method             
        if request.method == 'POST':
            print("inside request")
            # the URL entered by the User
            users_url = request.data['url']
            #the Domain name in the the URL entered
            domain = request.META['HTTP_HOST']
            # Gets the shortened record and serialize it
            service = shorten_url(users_url, domain)
            service_serializer = UrlSerializer(service, many=False)
            return Response(data={'success': True, 'data': service_serializer.data}, status=status.HTTP_201_CREATED)
        #PUT method             
        elif request.method == 'PUT':
            # the updated URL and the token entered by the User
            users_slug = request.data['slug']
            updated_url = request.data['url']
            service = UrlModel.objects.get(slug=users_slug)
            service.url = updated_url
            #Saving the changes in the database
            service.save()
            service_serializer = UrlSerializer(service, many=False)
            return Response(data={'success': True, 'data': service_serializer.data}, status=status.HTTP_201_CREATED)
        #DELETE Method
        elif request.method == 'DELETE':
            # the token entered by the User
            users_slug = optional_slug
            # Deleting the record from the table
            url = UrlModel.objects.filter(slug=users_slug)
            if(url):
                url.delete()
                return Response(data={'success': True, 'result': "URL deleted successfully"}, status=status.HTTP_201_CREATED)            
            else:
                return Response(data={'success': False, 'message': f'{str("No Url Found to delete")}'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(data={'success': False, 'message': f'{str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

'''
    Function which generates random string and returns it
    usng the built in rando module
'''
def generate_random_string(string_length=6):
    # Generates a random string
    random_string = ''
    alpha_numerals = string.ascii_letters + string.digits
    for _ in range(string_length):
        random_string = random_string + random.choice(alpha_numerals)
    print("random_string",random_string)
    return random_string

'''
    Function which takes url and the domain as a parameter
    and return the short URL
'''
def shorten_url(url, domain):
    # Gets a random string and validates it against the database
    random_string = generate_random_string()
    service, created = UrlModel.objects.get_or_create(slug=random_string)
    if created:
        service.url = url
        short_url = f'http://{domain}/goto/{random_string}/'
        service.short_url = short_url
        service.save()
        return service
    else:
        shorten_url(url, domain)
