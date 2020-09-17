# url_shortner
URL shortener  API for transforming long, ugly links into nice, memorable and trackable short URLs

#Prerequisites
1)Docker 
  Refer to the official documentation for the installation and configuration of the docker :- https://docs.docker.com/get-docker/
  
#Installation
1)Clone the repo
  git clone https://github.com/Madhan2105/url_shortner.git
2)Build the Docker
  docker-compose build
3)Run the Docker
  docker-compose up
  
#Usage

URL    :- http://localhost/api/
Method :- GET
Output :- [
            {
              "id": 2,
              "slug": "mNZZot", 
              "url": "https://www.django-rest-framework.org/tutorial/1-serialization/#using-modelserializers1",
              "short_url":"http://0.0.0.0:8000/goto/mNZZot/"
            }
          ]

URL    :- http://localhost:8000/api/
Method :- POST
Body   :- 
          {
            "url" : "https://www.django-rest-framework.org/community/tutorials-and-resources/#videos"
          }
Output :-
          {
              "success": true,
              "data": {
                  "id": 3,
                  "slug": "7FGDd3",
                  "url": "https://www.django-rest-framework.org/community/tutorials-and-resources/#videos",
                  "short_url": "http://0.0.0.0:8000/goto/7FGDd3/"
              }
          }
       
URL    :- http://localhost:8000/api/
Method :- PUT
Body   :- 
          {
             "slug": "7FGDd3",
            "url" : "https://www.django-rest-framework.org/tutorial/1-serialization/#using-modelserializers"
          }
Output :-
          {
              "success": true,
              "data": {
                  "id": 3,
                  "slug": "7FGDd3",
                  "url": "https://www.django-rest-framework.org/tutorial/1-serialization/#using-modelserializers",
                  "short_url": "http://0.0.0.0:8000/goto/7FGDd3/"
              }
          }

URL    :- http://0.0.0.0:0/api/7FGDd3
Method :- DELETE
Output :- 
          {
              "success": true,
              "result": "URL deleted successfully"
          }
          
