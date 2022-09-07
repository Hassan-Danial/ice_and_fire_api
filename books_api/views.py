from urllib import request
from django.http.response import JsonResponse
import requests
import json
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import book_serializer
from .models import book

# Create your views here.

def output_data(status_code, status, message=None):
    result={}
    if message==None:
        result = {
        "status_code": status_code,
        "status": status,
        "data":[]
        }
    else:
        result = {
        "status_code": status_code,
        "status": status,
        "message":message,
        "data":[]
        }
    return result


@csrf_exempt
def external_books(request):
    url = "https://www.anapioficeandfire.com/api/books"
    query = request.GET.get('name')
    if request.method == 'GET':
        if query:
            url = "https://www.anapioficeandfire.com/api/books?name={}".format(
                query)
            response = requests.get(url)
            if response.status_code == 200:
                data = json.loads(response.content.decode('utf-8'))
                if data:
                    result = output_data(response.status_code, "success")
                    result['data'].append({
                        "name": data[0].get("name"),
                        "isbn": data[0].get("isbn"),
                        "authors": data[0].get("authors"),
                        "number_of_pages": data[0].get("numberOfPages"),
                        "publisher": data[0].get("publisher"),
                        "country": data[0].get("country"),
                        "release_date": data[0].get("released")
                    })
                    return JsonResponse(result, safe=False)
                else:
                    return JsonResponse(output_data(response.status_code, "success"))
            else:
                return "External Api returned error :{}".format(response.status_code)
        else:
            return "Please provide a valid Book name"


@csrf_exempt
def books(request):
    # return JsonResponse(books_serializer.is_valid(),safe=False)
    if request.method == 'POST':
        books_data = JSONParser().parse(request)
        books_serializer = book_serializer(data=books_data)
        if books_serializer.is_valid():
            status = books_serializer.save()
            if status:
                result = output_data(201, 'success')
                result['data'].append(books_data)
                return JsonResponse(result)
        else:
            return JsonResponse(output_data(200, "fail"))
    if request.method == 'GET':
        books = book.objects.all()
        books_serializer = book_serializer(books, many=True)
        result = output_data(200, 'success')
        result['data'].append(books_serializer.data)
        return JsonResponse(result, safe=False)


@csrf_exempt
def update_book(request,book_id):
    if request.method == 'GET':
        selected_book = book.objects.get(id=book_id)
        result = output_data(200, "success")
        books_serializer = book_serializer(selected_book)
        result['data'] = books_serializer.data
        return JsonResponse(result)

    if request.method == 'PATCH':
        book_data = JSONParser().parse(request)
        selected_book = book.objects.get(id=book_id)
        books_serializer = book_serializer(selected_book, data=book_data)
        if books_serializer.is_valid():
            books_serializer.save()
            message = "The book {} was updated successfully".format(
                book_data['name'])
            result = output_data(200, "success", message)
            result['data']=books_serializer.data
            return JsonResponse(result)
    if request.method == 'DELETE':
        selected_book = book.objects.get(id=book_id)
        if selected_book:
            if selected_book.delete():
                message = "The book {} was deleted successfully".format(
                    book_serializer(selected_book).data.get('name'))
                result = output_data(204, "success", message)
                return JsonResponse(result)
            else:
                result = output_data(200, "fail")
        else:
            message = "Provide a valid book id"
            return JsonResponse(output_data(200, "fail", message))
