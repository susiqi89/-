from django.contrib import admin
from .models import *

# Register your models here.
# 课程分类表CourseList
@admin.register(CourseList)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('courseClassifield', 'courseName',)
    fields = ('courseClassifield', 'courseName',)

#教师表 Teach，包含：大照片 teachBigPic、小照片 teachSmallPic、老师姓名 teachName、讲课内容 teachCourse、语录 teachDesc\
@admin.register(Teach)
class TeachAdmin(admin.ModelAdmin):
    list_display = ('teachName', 'teachCourse','teachDesc','teachBigPic','teachSmallPic',)
    fields = ('teachName', 'teachCourse','teachDesc','teachBigPic','teachSmallPic',)

#领导层CEO，包含：照片 ceoImg、名言 ceoDesc、职务 ceoJob、姓名 ceoName
@admin.register(CEO)
class CEOAdmin(admin.ModelAdmin):
    list_display = ('ceoName', 'ceoJob','ceoDesc','ceoImg',)
    fields = ('ceoName', 'ceoJob','ceoDesc','ceoImg',)

#学员表Students，包含：学生姓名 studentName、所学课程 studentStudy、毕业后情况（月薪*K，签约公司）studentDesc、照片 studentIMG
@admin.register(Students)
class studentsAdmin(admin.ModelAdmin):
    list_display = ('studentName', 'studentStudy','studentDesc','studentImg','studentSay',)
    fields = ('studentName', 'studentStudy','studentDesc','studentImg','studentSay',)

#课程表StudyList，包含：课程名称 studyName、课时 studyCourse、学习时长 studyTime、正在学习的人数 studyCounts
@admin.register(StudyList)
class studyAdmin(admin.ModelAdmin):
    list_display = ('studyName', 'studyCourse','studyTime','studyCounts','studyImg',)
    fields = ('studyName', 'studyCourse','studyTime','studyCounts','studyImg',)
