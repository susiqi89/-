# -*- coding:utf-8 -*-
# @author:sumin
from django.http import HttpResponse, HttpResponseNotFound
from django.template.response import TemplateResponse
from django.shortcuts import render
import logging
from .models import *
logger = logging.getLogger('maizi_app.views')

# Create your views here.
def index(request):
    try:

        # ceolistcon = CEO.objects.all()
        studentlistcon = Students.objects.all()
        studylistcon = StudyList.objects.all()
    except Exception as e:
        logger.error(e)
    return TemplateResponse(request, 'index.html', locals())

