
# <editor-fold desc="Seializer storing">
from news.serializers import NewsSerializer


data = {
    "title": "this is title 1",
    "sentiment": "pn"
}

serializer=NewsSerializer(data=data)
serializer.is_valid()
serializer.save()
serializer.validated_data




data = {
    "title": "Pep Guardiola has played down suggestions that Lionel Messi could join him at Manchester City and believes "
             "the forward will end his playing days at Barcelona",
    "sentiment": "pn",
    "entities4thisnews": [
        {
            "entity": "Pep Guardiola",
        },
        {
            "entity": "Lionel Messi",
        },
        {
            "entity": "Manchester City",
        },
        {
            "entity": "Barcelona",
        }
    ]
}
# </editor-fold>

# <editor-fold desc="request data-News">
import requests
import json

ROOT="http://127.0.0.1:8000/"
POSTS_ENDPOINT="api/news"

data = {
    "title": "Nazdaq Stocks are going down after US China trade talks",
    "sentiment": "pn",
    "entities4thisnews": [

        {
            "entity": "US",
        },
        {
            "entity": "China",
        }
        ,
        {
            "entity": "China",
        }
    ]
}


headers = {
    "Content-Type": "application/json",
}
#post
r = requests.post(ROOT+POSTS_ENDPOINT, data=json.dumps(data), headers=headers)
r.text
r.content
r.status_code

#get all
GETALL_endpoint="api/news"
r = requests.get(ROOT+GETALL_endpoint, headers=headers)
r.status_code
r.content

#get one
GETONE_endpoint="api/news/3"
r = requests.get(ROOT+GETONE_endpoint, headers=headers)
r.status_code
r.content


#PATCH
PATCH_endpoint="api/news/3"

data = {
    "sentiment": "n",
}

r = requests.patch(ROOT+PATCH_endpoint, data=json.dumps(data), headers=headers)
r.status_code
r.content

#DELETE
DELETE_endpoint="api/news/3"
r = requests.delete(ROOT+DELETE_endpoint, headers=headers)
r.status_code
r.text
r.content
# </editor-fold>