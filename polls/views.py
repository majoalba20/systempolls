from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import CreatePollForm
from .models import Poll

def home(request):
    polls = Poll.objects.all()
    return render(request,'home.html',{'polls' : polls})

def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)    
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreatePollForm()
    return render(request,'create.html',{'form' : form})

def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    return render(request,'results.html',{'poll':poll})

def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    if request.method == 'POST':
        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        else:
            return HttpResponse(400, 'Invalid form')
    
        poll.save()
        return redirect('results',poll.id)

    return render(request,'vote.html',{'poll':poll})