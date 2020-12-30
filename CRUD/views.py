# GENERICAPI view
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, \
    CreateModelMixin, RetrieveModelMixin, \
    UpdateModelMixin, DestroyModelMixin


# list and create - PK not required
class LCStudentAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# Retrieve, Update and Delete
class RUDStudentAPI(GenericAPIView, RetrieveModelMixin,
                    UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# # from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Student
# from .serializers import StudentSerializer
# from rest_framework import status
# from rest_framework.views import APIView
#
#
# class StudentAPI(APIView):
#     def get(self, request, pk=None, format=None):
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(pk=id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)
#         else:
#             stu = Student.objects.all()
#             serializer = StudentSerializer(stu, many=True)
#             return Response(serializer.data)
#
#
#     def post(self, request, format=None):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#     def put(self, request, pk, format=None):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Complete Data Updated'})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#     def patch(self, request, pk, format=None):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Partial Data Updated'})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#     def delete(self, request, pk, format=None):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg': 'Data Deleted'})
#
#
#
#
# #
# # @api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
# # def student_api(request, pk=None):
# #     if request.method == 'GET':
# #         id = pk
# #         if id is not None:
# #             stu = Student.objects.get(pk=id)
# #             serializer = StudentSerializer(stu)
# #             return Response(serializer.data)
# #         else:
# #             stu = Student.objects.all()
# #             serializer = StudentSerializer(stu, many=True)
# #             return Response(serializer.data)
#
#
#     # if request.method == 'POST':
#     #     serializer = StudentSerializer(data=request.data)
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
#     #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     #
#
#     # if request.method == 'PUT':
#     #     id = pk
#     #     stu = Student.objects.get(pk=id)
#     #     serializer = StudentSerializer(stu, data=request.data)
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response({'msg': 'Complete Data Updated'})
#     #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#     # if request.method == 'PATCH':
#     #     id = pk
#     #     stu = Student.objects.get(pk=id)
#     #     serializer = StudentSerializer(stu, data=request.data, partial=True)
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response({'msg': 'Partial Data Updated'})
#     #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     #
#
#     # if request.method == 'DELETE':
#     #     id = pk
#     #     stu = Student.objects.get(pk=id)
#     #     stu.delete()
#     #     return Response({'msg': 'Data Deleted'})
#
#
#
#
#
#
#
# # @api_view()
# # def hello_world(request):
# #     return Response({'msg': 'Hello World'})
#
#
# # @api_view(['POST'])
# # def hello_world(request):
# #     if request.method == "POST":
# #         print(request.data)
# #         return Response({'msg': 'This is POST Request'})
#
# # @api_view(['GET', 'POST'])
# # def hello_world(request):
# #     if request.method == "GET":
# #         return Response({'msg': 'This is GET Request'})
# #
# #     if request.method == "POST":
# #         print(request.data)
# #         return Response({'msg': 'This is POST Request', 'data': request.data})
# #
#
#
#
#
#
#
#
#
#
#
# # import io
# # from rest_framework.parsers import JSONParser
# # from .models import Student
# # from .serializers import StudentSerializer
# # from rest_framework.renderers import JSONRenderer
# # from django.http import HttpResponse, JsonResponse
# # from django.views.decorators.csrf import csrf_exempt
# # from django.utils.decorators import method_decorator
# # from django.views import View
# #
# #
# # @method_decorator(csrf_exempt, name='dispatch')
# # class StudentAPI(View):
# #     def get(self, request, *args, **kwargs):
# #         json_data = request.body  # catch json data
# #         stream = io.BytesIO(json_data)
# #         python_data = JSONParser().parse(stream)
# #         id = python_data.get('id', None)
# #         if id is not None:
# #             stu = Student.objects.get(id=id)
# #             serializer = StudentSerializer(stu)
# #             json_data = JSONRenderer().render(serializer.data)
# #             return HttpResponse(json_data, content_type='application/json')
# #
# #         stu = Student.objects.all()
# #         serializer = StudentSerializer(stu, many=True)
# #         json_data = JSONRenderer().render(serializer.data)
# #         return HttpResponse(json_data, content_type='application/json')
# #
# #     def post(self, request, *args, **kwargs):
# #         json_data = request.body
# #         stream = io.BytesIO(json_data)
# #         python_data = JSONParser().parse(stream)
# #         serializer = StudentSerializer(data=python_data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             res = {'msg': 'Data Created!'}
# #             json_data = JSONRenderer().render(res)
# #             return HttpResponse(json_data, content_type='application/json')
# #         else:
# #             json_data = JSONRenderer().render(serializer.errors)
# #             return HttpResponse(json_data, content_type='application/json')
# #
# #     def put(self, request, *args, **kwargs):
# #         json_data = request.body
# #         stream = io.BytesIO(json_data)
# #         python_data = JSONParser().parse(stream)
# #         id = python_data.get('id')
# #         stu = Student.objects.get(id=id)
# #         serializer = StudentSerializer(stu, data=python_data, partial=True)
# #         if serializer.is_valid():
# #             serializer.save()
# #             res = {'msg': 'Data Updated!'}
# #             json_data = JSONRenderer().render(res)
# #             return HttpResponse(json_data, content_type='application/json')
# #         else:
# #             json_data = JSONRenderer().render(serializer.errors)
# #             return HttpResponse(json_data, content_type='application/json')
# #
# #     def delete(self, request, *args, **kwargs):
# #         json_data = request.body
# #         stream = io.BytesIO(json_data)
# #         python_data = JSONParser().parse(stream)
# #         id = python_data.get('id')
# #         stu = Student.objects.get(id=id)
# #         stu.delete()
# #         res = {'msg': 'Data Deleted!'}
# #         # json_data = JSONRenderer().render(res)
# #         # return HttpResponse(json_data, content_type='application/json')
# #         return JsonResponse(res, safe=False)
