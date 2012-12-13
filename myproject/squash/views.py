from squash.models import *
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count


def index(request):
	matches_list = MatchTwo.objects.all()
	return render_to_response('squash/base_matches.html', {'matches_list': matches_list}, context_instance = RequestContext(request))
	return HttpResponse(output)

def match(request, match_id):
    return HttpResponse("You're looking at squash %s." % match_id)

def edit_match(request, match_id):
    return HttpResponse("You want to edit a match for %s?" % match_id)

def add_match(request, match_id):
	return HttpResponse("You want to edit a match for %s?" % match_id)
	
def event_list(request):
	events_list = Attend.objects.all()
	return render_to_response('squash/base_events_list.html', {'events_list': events_list}, context_instance = RequestContext(request))
	return HttpResponse(output)
    
def event_add(request):
	if request.method == 'POST':
		form = AttendForm(request.POST)
		if form.is_valid():
			form.save()
			return render_to_response('squash/base_events_list.html', {'form': form}, context_instance = RequestContext(request))
	else:
		form = AttendForm()	
	return render_to_response('squash/base_add_match.html', {'form': form}, context_instance = RequestContext(request))

def auth_login(request):
	state = "Please log in below..."
	username = password = ''
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				state = "You're successfully logged in!"
			else:
				state = "Your account is not active, please contact the site admin."
		else:
			state = "Your username and/or password were incorrect."
			
	return render_to_response('squash/base_login.html',{'state':state, 'username': username}, context_instance = RequestContext(request))
	
def auth_logout(request):
	logout(request)
	return HttpResponse("You are now logged out")