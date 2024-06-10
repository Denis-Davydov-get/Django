from django.http import HttpResponse


def index(request):
    html_home = '''
                <h1>Добро пожаловать на главную страницу сайта</h1>
                '''
    return HttpResponse(html_home)


def about(request):
    html_about = '''
                <h1>Добро пожаловать на главную страницу сайта</h1>
                <p>Какой то текст про меня</p>
                '''
    return HttpResponse(html_about)
