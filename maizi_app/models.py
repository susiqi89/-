# -*- coding:utf-8 -*-
# @author:sumin
from django.db import models

#课程分类表CourseList，包含课程方向名称courseClassified、每个方向包含的具体课程名称courseName
class CourseList(models.Model):
    courseClassifield = models.CharField(max_length=50, verbose_name=u'课程方向')
    courseName = models.CharField(max_length=50, verbose_name=u'课程名称')

    class Meta:
        verbose_name = u'课程分类'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.courseName

#教师表 Teach，包含：大照片teachBigPic、小照片teachSmallPic、老师姓名teachName、讲课内容teachCourse、名言teachDesc
class Teach(models.Model):
    teachName = models.CharField(max_length=50, verbose_name=u'老师姓名')
    teachCourse = models.CharField(max_length=50, verbose_name=u'讲授课程')
    teachDesc = models.CharField(max_length=255, verbose_name=u'话录')
    teachBigPic = models.ImageField(verbose_name=u'大照片')
    teachSmallPic = models.ImageField(verbose_name=u'小照片')

    class Meta:
        verbose_name = u'教师表'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.teachCourse

#领导层CEO，包含：照片ceoImg、名言ceoDesc、职务ceoJob、姓名ceoName
class CEO(models.Model):
    ceoName = models.CharField(max_length=50, verbose_name=u'姓名')
    ceoDesc = models.CharField(max_length=255, verbose_name=u'话录')
    ceoJob = models.CharField(max_length=100, verbose_name=u'职务')
    ceoImg = models.ImageField(verbose_name=u'照片')

    class Meta:
        verbose_name = u'领导层寄语'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.ceoName

#学员表Students，包含：学生姓名studentName、所学课程studentStudy、毕业后情况（月薪*K，签约公司）studentDesc、照片studentIMG
class Students(models.Model):
    studentName = models.CharField(max_length=50, verbose_name=u'学生姓名')
    studentStudy = models.CharField(max_length=50, verbose_name=u'所学课程')
    studentDesc = models.CharField(max_length=255, verbose_name=u'毕业后情况')
    # course = models.ForeignKey(StudyList, verbose_name=u'课程表关联')
    studentImg = models.ImageField(verbose_name=u'照片')
    studentSay = models.CharField(max_length=255, blank=True, null=True, verbose_name=u'语录 ')

    class Meta:
        verbose_name = u'学生表'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.studentStudy

#课程表StudyList，包含：课程名称studyName、课时studyCourse、学习时长studyTime、正在学习的人数studyCounts
class StudyList(models.Model):
    studyName = models.CharField(max_length=50, verbose_name=u'课程名称')
    studyCourse = models.CharField(max_length=50, verbose_name=u'总课时')
    studyTime = models.CharField(max_length=255, verbose_name=u'学习时长')
    studyCounts = models.CharField(max_length=100, verbose_name=u'正在学习的人数')
    studyImg = models.ImageField(verbose_name=u'课程图标', blank=True, null=True)

    class Meta:
        verbose_name = u'课程表'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.studyName



