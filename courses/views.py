from datetime import datetime

from django.core import serializers
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404

from courses.models import Course, InCart, Purchase

def index(request):
    all_courses = serializers.serialize('json', Course.objects.all())
    return HttpResponse(all_courses, content_type="application/json")

def detail(request, course_id):
    course = serializers.serialize('json', Course.objects.get(pk=course_id))
    return HttpResponse(course, content_type="application/json")

def cart(request):
    if (request.method == 'GET'):
        all_in_cart = InCart.objects.all()
        courses_in_cart = []
        for item in all_in_cart:
            courses_in_cart.append(Course.objects.get(pk=item.course.id))
        in_cart_response = serializers.serialize('json', courses_in_cart)
        return HttpResponse(in_cart_response, content_type="application/json")
    if (request.method != 'POST'):
        return HttpResponseForbidden()
    id = request.POST['id']
    course = Course.objects.get(pk=id)
    newInCart = InCart(course=course, in_cart_date=datetime.now())
    newInCart.save()
    return HttpResponse("Course saved in cart", content_type="text/plain")

def purchases(request):
    if (request.method == 'GET'):
        all_purchases = Purchase.objects.all()
        purchased_courses = []
        for item in all_in_cart:
            purchased_courses.append(Course.objects.get(pk=item.course.id))
        purchases_response = serializers.serialize('json', courses_in_cart)
        return HttpResponse(in_cart_response, content_type="application/json")
    if (request.method != 'POST'):
        return HttpResponseForbidden()
    # TODO:instead of just handling an id, iterate over array of ids to create
    # purchase records
    # id = request.POST['id']
    # course = Course.objects.get(pk=id)
    # newPurchase = Purchase(course=course, purchase_date=datetime.now())
    # newPurchase.save()
    return HttpResponse("Course purchased", content_type="text/plain")
