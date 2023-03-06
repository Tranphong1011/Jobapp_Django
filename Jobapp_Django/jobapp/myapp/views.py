from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template import loader

from myapp.models import JobPost

# Create your views here.

job_title = [
    "engineer",
    "developer",
    "tester"
]
job_description = [
    "11111111111",
    "222222222222222",
    "333333333333333"
]


def hello(request):
    return HttpResponse("hello")


def product(request, id):
    return HttpResponse(f"product {id}")


def link(request):
    text = "<ul>"
    for i in job_title:

        job_id = job_title.index(i)
        print(reverse(('job_detail'), args=(job_id,)))
        text += f"<li><a href= 'job/{job_id}'>{i}</a></li>"

    text += "</ul>"

    return HttpResponse(text)


def job(request, id):
    try:
        if id == 0:
            return redirect(reverse("job_home"))
            # = return redirect("/link") chuyển về trang khác
            # = return redirect("job_home")
        text = f"<b>{job_title[id]}</b> - {job_description[id]}"
        return HttpResponse(text)
    except:
        return HttpResponseNotFound("Not Found")


list_template = ["job", "job_detail"]


class Temp:
    x = 5


def greeting(request):
    template = loader.get_template('app/helloo.html')
    temp = Temp()
    is_authenticated = False
    context = {"name": "Phong", "list": list_template,
               "temp_object": temp, "is_authenticated": is_authenticated}
    return render(request,  'app/helloo.html', context)
    # return HttpResponse(template.render(context, request)) cách khác để return render
    # return HttpResponse("hello")


def test(request, id):
    # template= loader.get_template('app/job_detail.html')

    context = {"job_title": job_title[id],
               "job_description": job_description[id]}
    return render(request, 'app/job_detail.html', context)

jobs = JobPost.objects.all()
def list_job(request):
    
    context = {"jobs": jobs}
    return render(request, 'app/list_job.html', context)


def get_job(request, id):
    context = {"job_detail": jobs[id]}
    return render(request, 'app/list_job_detail.html', context)
