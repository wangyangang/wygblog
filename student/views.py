from django.shortcuts import render, redirect, reverse
from django.views import View
from .models import Student
from .forms import  StudentForm


class IndexView(View):
    template_name = 'index.html'

    def get_context(self):
        i = 1/0
        students = Student.get_all()
        context = {'students': students}
        return context

    def get(self, request):
        # students = Student.objects.all()
        students = Student.get_all()
        form = StudentForm()
        context = self.get_context()
        context.update({'form': form})
        return render(request, self.template_name, context)

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            # cleaded_data = form.cleaned_data
            # student = Student()
            # student.name = cleaded_data['name']
            # student.sex = cleaded_data['sex']
            # student.email = cleaded_data['email']
            # student.profession = cleaded_data['profession']
            # student.qq = cleaded_data['qq']
            # student.phone = cleaded_data['phone']
            # student.save()
            form.save()
            return redirect(reverse('student:index'))

        context = self.get_context()
        context.update({'form': form})
        return render(request, self.template_name, context)
