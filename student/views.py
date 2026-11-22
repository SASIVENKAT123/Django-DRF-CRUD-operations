from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Student
from django.shortcuts import get_object_or_404

import json
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def student_create(request):

    if request.method!="POST":
        return JsonResponse({"error":"Only POST method is allowed"},status=405)

    try:
        data=json.loads(request.body)

        name=data["name"]
        age=int(data["age"])
        course=data["course"]

    except(json.JSONDecodeError, KeyError, TypeError, ValueError):
        return JsonResponse({"error":"Please provide a valid name, age and course"},status=400)

    student=Student.objects.create(
        name=name,
        age=age,
        course=course
    )

    return JsonResponse({
        "message":"Student created successfully",
        "Student":{
            "id":student.id,
            "name":student.name,
            "age":student.age,
            "course":student.course
        }
    },status=201)






def student_list(request):
    students=Student.objects.all()
    student_data=[]
    for student in students:
        student_data.append({
            "id":student.id,
            "name":student.name,
            "age":student.age,
            "course":student.course
        })

    return JsonResponse({"students":student_data})

@csrf_exempt
def student_detail(request, student_id):

    student = get_object_or_404(Student, id=student_id)

    # Get - retreive student data

    if request.method =="GET":
        return JsonResponse({
            "id":student.id,
            "name":student.name,
            "age":student.age,
            "course":student.course
        })

    # put - to update student details

    elif request.method == "PUT":
        try:
            data = json.loads(request.body)
            student.name = data["name"]
            student.age = int(data["age"])
            student.course = data["course"]

            student.save()

            return JsonResponse({"message":"Student updated successfully"})
        except(json.JSONDecodeError, KeyError, ValueError, TypeError):
            return JsonResponse({"error":"please provide a valid name , age and course"},status= 400)

    # PATCH - to update only student's specific details

    elif request.method == "PATCH":
        try:
            data=json.loads(request.body)

            if "name" in data:
                student.name = data["name"]
            if "age" in data:
                student.age = int(data["age"])

            if "course" in data:
                student.course = data["course"]

            student.save()
            return JsonResponse({"message":"Student detail updated successfully"})

        except(json.JSONDecodeError, KeyError, ValueError, TypeError):
            return JsonResponse({"error":"Please provide valid details"},status = 400)


    # DELETE

    elif request.method == "DELETE":
        student.delete()

        return JsonResponse({"message":"Student deleted successfully"})


    return JsonResponse({"error":"Method not allowed"},status=405)




  
