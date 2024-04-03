from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views import View


def index(request):
    return render(request, 'index.html')


def programming(request):
    return render(request, 'programming.html')


def layouting(request):
    return render(request, 'layouting.html')


def ratings(request):
    return render(request, 'ratings.html')


def platform(request):
    return render(request, 'platform.html')


def authors(request):
    return render(request, 'authors.html')


def politics(request):
    return render(request, 'politics.html')


def condition(request):
    return render(request, 'condition.html')


def java_main(request):
    return render(request, 'java/lesson-java-main.html')


def javascript_main(request):
    return render(request, 'javascript/lesson-javascript-main.html')


def php_main(request):
    return render(request, 'php/lesson-php-main.html')


def c_main(request):
    return render(request, 'c/lesson-c-main.html')


def c_sharp_main(request):
    return render(request, 'c_sharp/lesson-c_sharp-main.html')


def css_s_main(request):
    return render(request, 'css_s/lesson-css-main.html')


def go_main(request):
    return render(request, 'go/lesson-go-main.html')


def html_main(request):
    return render(request, 'html/lesson-html-main.html')


def python_main(request):
    return render(request, 'python/lesson-python-main.html')


def racket_main(request):
    return render(request, 'racket/lesson-racket-main.html')


def ruby_main(request):
    return render(request, 'ruby/lesson-ruby-main.html')


def typescript_main(request):
    return render(request, 'typescript/lesson-typescript-main.html')


def clesson1(request):
    return render(request, 'c/lesson-1.html')


def clesson2(request):
    return render(request, 'c/lesson-2.html')


def clesson3(request):
    return render(request, 'c/lesson-3.html')


def clesson4(request):
    return render(request, 'c/lesson-4.html')


def clesson5(request):
    return render(request, 'c/lesson-5.html')


def clesson6(request):
    return render(request, 'c/lesson-6.html')


def clesson7(request):
    return render(request, 'c/lesson-7.html')


def clesson8(request):
    return render(request, 'c/lesson-8.html')


# c#
def csharplesson1(request):
    return render(request, 'c_sharp/lesson-1.html')


def csharplesson2(request):
    return render(request, 'c_sharp/lesson-2.html')


def csharplesson3(request):
    return render(request, 'c_sharp/lesson-3.html')


def csharplesson4(request):
    return render(request, 'c_sharp/lesson-4.html')


def csharplesson5(request):
    return render(request, 'c_sharp/lesson-5.html')


def csharplesson6(request):
    return render(request, 'c_sharp/lesson-6.html')


def csharplesson7(request):
    return render(request, 'c_sharp/lesson-7.html')


def csharplesson8(request):
    return render(request, 'c_sharp/lesson-8.html')


def csharplesson9(request):
    return render(request, 'c_sharp/lesson-9.html')


def csharplesson10(request):
    return render(request, 'c_sharp/lesson-10.html')


# html
def htmllesson1(request):
    return render(request, 'html/lesson-1.html')


def htmllesson2(request):
    return render(request, 'html/lesson-2.html')


def htmllesson3(request):
    return render(request, 'html/lesson-3.html')


def htmllesson4(request):
    return render(request, 'html/lesson-4.html')


def htmllesson5(request):
    return render(request, 'html/lesson-5.html')


def htmllesson6(request):
    return render(request, 'html/lesson-6.html')


def htmllesson7(request):
    return render(request, 'html/lesson-7.html')


# css
def css_slesson1(request):
    return render(request, 'css_s/lesson-1.html')


def css_slesson2(request):
    return render(request, 'css_s/lesson-2.html')


def css_slesson3(request):
    return render(request, 'css_s/lesson-3.html')


def css_slesson4(request):
    return render(request, 'css_s/lesson-4.html')


def css_slesson5(request):
    return render(request, 'css_s/lesson-5.html')


def css_slesson6(request):
    return render(request, 'css_s/lesson-6.html')


def css_slesson7(request):
    return render(request, 'css_s/lesson-7.html')


def css_slesson8(request):
    return render(request, 'css_s/lesson-8.html')


# java
def javalesson1(request):
    return render(request, 'java/lesson-1.html')


def javalesson2(request):
    return render(request, 'java/lesson-2.html')


def javalesson3(request):
    return render(request, 'java/lesson-3.html')


def javalesson4(request):
    return render(request, 'java/lesson-4.html')


def javalesson5(request):
    return render(request, 'java/lesson-5.html')


def javalesson6(request):
    return render(request, 'java/lesson-6.html')


# javascript
def javascriptlesson1(request):
    return render(request, 'javascript/lesson-1.html')


def javascriptlesson2(request):
    return render(request, 'javascript/lesson-2.html')


def javascriptlesson3(request):
    return render(request, 'javascript/lesson-3.html')


def javascriptlesson4(request):
    return render(request, 'javascript/lesson-4.html')


def javascriptlesson5(request):
    return render(request, 'javascript/lesson-5.html')


def javascriptlesson6(request):
    return render(request, 'javascript/lesson-6.html')


# ruby
def rubylesson1(request):
    return render(request, 'ruby/lesson-1.html')


def rubylesson2(request):
    return render(request, 'ruby/lesson-2.html')


def rubylesson3(request):
    return render(request, 'ruby/lesson-3.html')


def rubylesson4(request):
    return render(request, 'ruby/lesson-4.html')


def rubylesson5(request):
    return render(request, 'ruby/lesson-5.html')


def rubylesson6(request):
    return render(request, 'ruby/lesson-6.html')


def rubylesson7(request):
    return render(request, 'ruby/lesson-7.html')


def rubylesson8(request):
    return render(request, 'ruby/lesson-8.html')


def rubylesson9(request):
    return render(request, 'ruby/lesson-9.html')


# php
def phplesson1(request):
    return render(request, 'php/lesson-1.html')


def phplesson2(request):
    return render(request, 'php/lesson-2.html')


def phplesson3(request):
    return render(request, 'php/lesson-3.html')


def phplesson4(request):
    return render(request, 'php/lesson-4.html')


def phplesson5(request):
    return render(request, 'php/lesson-5.html')


def phplesson6(request):
    return render(request, 'php/lesson-6.html')


def phplesson7(request):
    return render(request, 'php/lesson-7.html')


def phplesson8(request):
    return render(request, 'php/lesson-8.html')


def phplesson9(request):
    return render(request, 'php/lesson-9.html')


# python
def pythonlesson1(request):
    return render(request, 'python/lesson-1.html')


def pythonlesson2(request):
    return render(request, 'python/lesson-2.html')


def pythonlesson3(request):
    return render(request, 'python/lesson-3.html')


def pythonlesson4(request):
    return render(request, 'python/lesson-4.html')


def pythonlesson5(request):
    return render(request, 'python/lesson-5.html')


def pythonlesson6(request):
    return render(request, 'python/lesson-6.html')


def pythonlesson7(request):
    return render(request, 'python/lesson-7.html')


def pythonlesson8(request):
    return render(request, 'python/lesson-8.html')


class RegisterView(View):
    template_name = 'registration/register.html'

    # Отправка формы регистрации
    def get(self, request):
        context = {'form': UserCreationForm}
        return render(request, self.template_name, context)

    # Добавление в БД
    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')

        context = {'form': UserCreationForm}
        return render(request, self.template_name, context)
