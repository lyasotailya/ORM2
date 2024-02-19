from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    ordering = 'group'
    student = Student.objects.order_by(ordering).all()
    teacher = Teacher.objects.all()
    context = {
        'student': student,
        'teacher': teacher,
    }

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    print(student)
    return render(request, 'students_list.html', context=context)
