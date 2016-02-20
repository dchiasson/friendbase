from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. Your're at the poll index.")

def detail(request, poll_id):
    return HttpResponse("You're looking at poll {}.".format(poll_id))

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll {}.".format(poll_id))

def vote(request, poll_id):
    return HttpResponse("You're voting on poll {}".format(poll_id))
