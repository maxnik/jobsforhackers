# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils import simplejson
from jobs.forms import JobForm, PublishedJobForm
from jobs.models import Job
from google.appengine.api import users
from pager import PagerQuery

def list(request):
    PER_PAGE = 10
    bookmark = request.GET.get('bookmark')
    query = PagerQuery(Job).filter('status =', 'published').order('-published_at')
    prev, jobs, next = query.fetch(PER_PAGE, bookmark)
    return _custom_render_to_response('list_jobs.html',
                                      {'jobs': jobs, 'prev': prev, 'next': next, 'title': 'Newest'})

def my(request):
    jobs = Job.all().filter('owner =', users.get_current_user()).order('-created_at')
    return _custom_render_to_response('my_jobs.html', {'jobs': jobs, 'title': 'My jobs'})

def create(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = Job(**form.cleaned_data)
            if users.is_current_user_admin():
                job.publish()
            job.put()
            return HttpResponseRedirect('/jobs/my')
    else:
        form = JobForm()
    return _custom_render_to_response('job_form.html', {'form': form, 'title': 'Add new job'})

def show(request, job_id):
    job = Job.get_by_id(int(job_id)) 
    if not job:
        raise Http404
    if not job.is_published: # only job owner or admin can view unpublished jobs
        if not job.owned_by(users.get_current_user(), users.is_current_user_admin()):
            raise Http404
    return _custom_render_to_response('show_job.html', {'job': job, 'title': job.title})

def edit(request, job_id):
    job = _get_job_or_404(job_id)
    if request.method == 'POST':
        if job.is_published:
            form = PublishedJobForm(request.POST)
        else:
            form = JobForm(request.POST)
        if form.is_valid():
            for (field, value) in form.cleaned_data.items():
                setattr(job, field, value)
            job.put()
            return HttpResponseRedirect('/jobs/my')
    else:
        initial_form_values = {}
        for field in job.properties().keys():
            initial_form_values[field] = getattr(job, field)
        if job.is_published:
            form = PublishedJobForm(initial_form_values)
        else:
            form = JobForm(initial_form_values)
    return _custom_render_to_response('job_form.html', {'form': form, 'job': job, 'title': 'Edit my job'})

def check(request, job_id):
    job = _get_job_or_404(job_id)
    job.queue()
    job.put()
    if request.is_ajax():
        json = {'job-status-%s' % (job_id,): render_to_string('job_status.html', {'job': job})}
        return HttpResponse(simplejson.dumps(json), mimetype='application/javascript')    
    else:
        return HttpResponseRedirect('/jobs/my')

def delete(request, job_id):
    job = _get_job_or_404(job_id)
    job.delete()
    if request.is_ajax():
        json = {'job-status-%s' % (job_id,): '',
                'job-actions-%s' % (job_id,): '<span class="code">Job was deleted.</span>'}
        return HttpResponse(simplejson.dumps(json), mimetype='application/javascript')    
    else:
        return HttpResponseRedirect('/jobs/my')

def _get_job_or_404(job_id):
    job = Job.get_by_id(int(job_id))
    current_user = users.get_current_user() # only job owner or admin can edit, check or delete the job
    if job and job.owned_by(current_user, users.is_current_user_admin()):
        return job
    else:
        raise Http404

def _auth_processor(request):
    # make auth information available in all templates automatically
    return {'current_user': users.get_current_user(),
            'logout_url': users.create_logout_url('/'),
            'is_current_user_admin': users.is_current_user_admin()}

def _custom_render_to_response(template_name, context_dict):
    # we pass RequestContext instance for _auth_processor above to work
    return render_to_response(template_name, context_dict, context_instance=RequestContext({}))
