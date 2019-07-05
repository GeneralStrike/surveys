from django.shortcuts import render
from .forms import DevSurveyForm


def dev_survey(request):
    if request.method == 'POST':
        form = DevSurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success_dev.html')
    else:
        form = DevSurveyForm()

    return render(request, 'dev_survey.html', {
        'form': form,
    })


def success_dev(request):
    return render(request, 'success_dev.html')
