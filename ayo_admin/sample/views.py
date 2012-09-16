# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from common.forms import RawErrorList
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

def index(request, template="sample/index.html"):
    return render_to_response(template, {}, context_instance=RequestContext(request))
