from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from courses.models import Course

def index(request):
    all_courses = serializers.serialize('json', Course.objects.all())
    return HttpResponse(all_courses, content_type="application/json")

def detail(request, course_id):
    course = serializers.serialize('json',
        get_object_or_404(Course, pk=course_id))
    return HttpResponse(course, content_type="application/json")
