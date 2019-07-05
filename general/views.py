from django.shortcuts import render
from .forms import UserSurveyForm


def user_survey(request):
    if request.method == 'POST':
        form = UserSurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success_user.html')
    else:
        form = UserSurveyForm()

    return render(request, 'user_survey.html', {
        'form': form,
    })


def success_user(request):
    return render(request, 'success_user.html')
