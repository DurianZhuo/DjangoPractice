from django.db import models

# Create your models here.


class Clazz(models.Model):
    cno = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=30)

    def __str__(self):
        return self.cname


class Course(models.Model):
    courseid = models.AutoField(primary_key=True)
    coursename = models.CharField(max_length=30)

    def __str__(self):
        return self.coursename


class Student(models.Model):
    sno = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=30)
    clazz = models.ForeignKey(Clazz, related_name='students')
    course = models.ManyToManyField(Course)

    def __str__(self):
        return self.sname


def registerOper(sname, cname,coursenames):
    try:
        try:
            clazz = Clazz.objects.get(cname=cname)
        except Clazz.DoesNotExist:
            clazz = Clazz.objects.create(cname=cname)
        courselist = []
        for i in coursenames:
            courseobj = Course.objects.create(coursename=i)
            courselist.append(courseobj)
        stu = Student.objects.create(sname=sname, clazz=clazz)
        stu.course.add(*courselist)
        return True
    except Exception as e:
        print(e)
        return False
