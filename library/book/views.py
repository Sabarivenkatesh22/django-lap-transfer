from rest_framework.decorators import api_view
from rest_framework.response import Response
# from home.serializers import PeopleSerializer
from .models import Book
from .serilalizers import BookSerializer


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
def book_controller(request):
    if request.method == 'GET':
        objs = Book.objects.all()
        serialiser = BookSerializer(objs, many = True)
        return Response(serialiser.data)

    elif request.method == 'POST':
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # print(data)
        # new_book = Book(data)
        # new_book.save()
        
        
        return Response(serializer.errors)