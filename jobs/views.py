from django.shortcuts import render_to_response

def list(request):
    return render_to_response('list_jobs.html')

def my(request):
    pass

def create(requrest):
    pass

def show(request, job_id):
    pass

def check(request, job_id):
    pass

def edit(request, job_id):
    pass

def destroy(request, job_id):
    pass
