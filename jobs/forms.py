from django import forms

class PublishedJobForm(forms.Form):
    title = forms.CharField(label='Who is needed?',
                            max_length=128,
                            error_messages={'required': 'Specify a title for the job, please.',
                                            'max_length': 'The job title must be shorter than 128 symbols.'})
    description = forms.CharField(label='Job description',
                                  max_length=2000,
                                  widget = forms.Textarea,
                                  error_messages={'required': 'Describe the open position in few words, please.',
                                                  'max_length': 'The job description must be shorter than 2000 symbols.'})
    url = forms.URLField(required=False,
                         label='URL (optional)',
                         max_length=128,
                         error_messages={'invalid': 'Check format of the url (http://...), please.',
                                         'max_length': 'The url must be shorter than 128 symbols.'})

class JobForm(PublishedJobForm):
    # user can't change this field for published jobs
    hackernews_login = forms.CharField(label='Your login at <a href="http://news.ycombinator.com/">HN</a>',
                                       max_length=42,
                                       error_messages={'required': 'We need it to verify that job is yours.',
                                                       'max_length': 'Do such long logins really exist?'})
