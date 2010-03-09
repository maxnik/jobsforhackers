from django import template

register = template.Library()

@register.inclusion_tag('job_actions.html')
def show_job_actions(job, current_user, is_current_user_admin):
    if job.owned_by(current_user, is_current_user_admin):
        return {'job': job}
    else:
        return {}

@register.inclusion_tag('job_status.html')
def show_job_status(job, current_user, is_current_user_admin):
    if job.owned_by(current_user, is_current_user_admin):
        return {'job': job}
    else:
        return {}
