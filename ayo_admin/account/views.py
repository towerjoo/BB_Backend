# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as UserLogin, logout
import json
from django.views.decorators.csrf import csrf_exempt
from common.utils import is_valid_email
from account.models import Account

@csrf_exempt
def login(request):
    data = {
        "status" : "success",
        "message" : "",
    }
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username:
            if password:
                user = authenticate(username=username, password=password)
                if user and user.is_active:
                    UserLogin(request, user)
                    from tastypie.models import ApiKey
                    api = ApiKey.objects.create(user=user)
                    data.update({
                        "message" : "Login successfully",
                        "data" : {
                            "api_key" : api.key,
                            "username" : user.username,
                        }
                    })
                    return HttpResponse(json.dumps(data), mimetype="application/json")
                else:
                    data.update({"status" : "error", "message":"incorrect username or password"})
                    return HttpResponse(json.dumps(data), mimetype="application/json")
            else:
                data.update({"status" : "error", "message":"password can't be blank"})
                return HttpResponse(json.dumps(data), mimetype="application/json")
        else:
            data.update({"status" : "error", "message":"username can't be blank"})
            return HttpResponse(json.dumps(data), mimetype="application/json")
    else:
        data.update({"status" : "error", "message":"only support POST calling"})
    return HttpResponse(json.dumps(data), mimetype="application/json")



@csrf_exempt
def register(request):
    data = {
        "status" : "success",
        "message" : "",
    }
    if request.method == "POST":
        username = request.POST.get("username")
        user_firstname = request.POST.get("firstname")
        user_lastname = request.POST.get("lastname")
        password = request.POST.get("password")
        email = request.POST.get("email")
        user_gender = request.POST.get("gender")
        if username and user_firstname and user_lastname and password and email and user_gender:
            if not is_valid_email(email):
                data.update({
                    "status" : "error",
                    "message" : "An invalid email"
                })
                return HttpResponse(json.dumps(data), mimetype="application/json")

            flag, acct = Account.objects.new_user(username, user_firstname, user_lastname, password, \
                            email, user_gender)
            if flag:
                user = authenticate(username=username, password=password)
                UserLogin(request, user)
                from tastypie.models import ApiKey
                api = ApiKey.objects.create(user=acct.user)
                data.update({
                    "message" : "Register successfully",
                    "data" : {
                        "api_key" : api.key,
                        "username" : username,
                    }
                })
            else:
                data.update({
                    "status" : "error",
                    "message" : "The user with this username already exists"
                })
            return HttpResponse(json.dumps(data), mimetype="application/json")
        else:
            data.update({"status" : "error", "message":"username or user_firstname or user_lastname or password or email or user_gender is null"})
            return HttpResponse(json.dumps(data), mimetype="application/json")
    else:
        data.update({"status" : "error", "message":"only support POST calling"})
    return HttpResponse(json.dumps(data), mimetype="application/json")



@csrf_exempt
def facebook_connection(request):
    data = {
        "status" : "success",
        "message" : "",
    }
    if request.method == "POST":
        user_firstname = request.POST.get("firstname")
        user_lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        user_gender = request.POST.get("gender")
        facebook_id = request.POST.get("facebook_id")
        facebook_token = request.POST.get("facebook_token")
        if  user_firstname and user_lastname and email and user_gender and \
                facebook_id and facebook_token:
            if not is_valid_email(email):
                data.update({
                    "status" : "error",
                    "message" : "An invalid email"
                })
                return HttpResponse(json.dumps(data), mimetype="application/json")

            flag, acct = Account.objects.facebook_connection(facebook_id, facebook_token, user_firstname, user_lastname, email, user_gender)
            if flag:
                user = authenticate(username=facebook_id, password=facebook_id)
                UserLogin(request, user)
                from tastypie.models import ApiKey
                api = ApiKey.objects.create(user=acct.user)
                data.update({
                    "message" : "Facebook connection successfully",
                    "data" : {
                        "api_key" : api.key,
                        "username" : facebook_id,
                    }
                })
            else:
                data.update({
                    "status" : "error",
                    "message" : "user's account has issues"
                })
            return HttpResponse(json.dumps(data), mimetype="application/json")
        else:
            data.update({"status" : "error", "message":"username or user_firstname or user_lastname or password or email or user_gender is null"})
            return HttpResponse(json.dumps(data), mimetype="application/json")
    else:
        data.update({"status" : "error", "message":"only support POST calling"})
    return HttpResponse(json.dumps(data), mimetype="application/json")


