from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.serializers import PeopleSerializer
from .models import Person


@api_view(['GET', 'POST', 'PUT'])
def index(request):
    if request.method == 'GET':
        params = request.query_params
        # print(params['param1'])
        courses = {
            'course_name' : 'Python',
            'learn' : ['flask', 'Django', 'Tornodo', 'FastAPi']
        }
        return Response(courses)
    elif request.method == 'POST':
        data = request.data
        print("from post request")
        return Response(data)

@api_view(['GET', 'POST'])
def person(request):
    if request.method == 'GET':
        objs = Person.objects.all()
        serializer = PeopleSerializer(objs, many=True)
        return Response(serializer.data)

    else:
        data = request.data
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)