from django.shortcuts import render
from datetime import datetime
# Create your views here.


def myapp(request):
    # uname = False
    # email = 'codemi692@gmail.com'
    # passwd= 'M642orsghgjks4564!'
    # dt = datetime.now()
    # flt = 56.6347
    # content = {'name':uname, 'email':email , 'pwd':passwd, 'd':dt , 'int':flt}

    stu = {'student': {'morsalin':  'rasel',  'key': 'soytsan',   'hello': 'jjkhj'},
           'student1': {'morsalin1':  'rasel1', 'key1': 'soytsan1', 'hello1': 'jjkhj1'},
           'student3': {'morsalin3':  'rasel3', 'key3': 'soytsan3', 'hello3': 'jjkhj3'},
           'student4': {'morsalin4':  'rasel4', 'key4': 'soytsan4', 'hello4': 'jjkhj4'},
           'student5': {'morsalin5':  'rasel5', 'key5': 'soytsan5', 'hello5': 'jjkhj5'},
           'student6': {'morsalin6':  'rasel6', 'key6': 'soytsan6', 'hello6': 'jjkhj6'},
           }

    students = {'student': stu}

    return render(request, 'myapp/index2.html', students)
