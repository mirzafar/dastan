from django.shortcuts import render
from main.models import *
from django.http.response import JsonResponse
import os, uuid
import random
import re
import smtplib as smtp
from mysite.settings import BASE_DIR
import base64


# Create your views here.
email_regex = re.compile(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$')
def indexHandler(request):
    return render(request, 'index.html',{})

def masterklassHandler(request):
    videos = Video.objects.all()
    return render(request, 'masterklass.html', {"videos": videos})


def masterklassBlogHandler(request, masterklass_id):
    posts = Video.objects.get(id=int(masterklass_id))
    return render(request, 'masterklassblog.html', {"posts": posts})


def contactHandler(request):
    infos = Info.objects.all()[0]
    errors = []
    if request.POST:
        action = request.POST.get('action', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        description = request.POST.get('description', '')
        if action == 'send':
            sm = SendMessage()
            if name:
                sm.name = name
            else:
                errors.append("Name not found")
            if email:
                if email_regex.match(email):
                    sm.email = email
                else:
                    errors.append("Check again email")
            else:
                errors.append("Email not found")
            if description:
                sm.description = description
            else:
                errors.append("Description not found")
            if not errors:
                sm.save()
                response = JsonResponse({'status': True}, status=200)
            else:
                response = JsonResponse({'status': False, 'errors': errors}, status=200)
            return response

    return render(request, 'contact.html', {"infos": infos, "errors": errors})


def obuchenieHandler(request):
    categorys = Category.objects.all()
    ctg = Category2.objects.all()
    return render(request, 'obuchenie.html', {"categorys": categorys, "ctg": ctg})


def mimikaHandler(request):
    categorys = Category.objects.all()
    return render(request, 'mimika.html', {"categorys": categorys,})


def categoryBlogHandler(request, category_id):
    posts = Category2.objects.get(id=int(category_id))
    return render(request, 'ctg.html', {"posts": posts})


def mimikaBlogHandler(request, obuchenie_id):
    posts = Category.objects.get(id=int(obuchenie_id))

    b = random.randint(4,5)

    errors = []
    if request.POST:
        action = request.POST.get('action', '')
        logo = request.POST.get('image', '')
        ctg_id = int(request.POST.get('id', 0))
        if action == 'add':
            cc = Grade()
            cc.photo = logo
            cc.ball = b
            cc.category_id = ctg_id
            if not errors:
                cc.save()
                response = JsonResponse({'status': True, 'ball': b}, status=200)
            else:
                response = JsonResponse({'status': False, 'errors': errors}, status=200)
            return response

    return render(request, 'obuchenieId.html', {"posts": posts, "errors": errors})


def apiUploadHandler(request):
    file_name = ''

    if request.POST:
        fileinfo = request.FILES.get('file')
        if fileinfo:
            fname = fileinfo.name
            extn = os.path.splitext(fname)[1]
            cname = str(uuid.uuid4()) +extn
            FILE_DIR = os.path.join(BASE_DIR, 'media', 'upload/')
            fh = open(FILE_DIR + cname, 'wb')
            print('file size is -> ', fileinfo.size)
            fh.write(fileinfo.read())
            fh.close()
            file_name = cname
        image_base = request.POST.get('image_base', None)
        if image_base:
            image_data = image_base
            format, imgstr = image_data.split(';base64,')
            ext = format.split('/')[-1]
            cname = str(uuid.uuid4()) + '.' + ext
            FILE_DIR = os.path.join(BASE_DIR, 'media', 'upload/')
            fh = open(FILE_DIR + cname, 'wb')
            fh.write(base64.b64decode((imgstr)))
            fh.close()
            file_name = cname

    response = JsonResponse({'success': True, 'file_name': file_name})
    response.status_code = 200
    return response