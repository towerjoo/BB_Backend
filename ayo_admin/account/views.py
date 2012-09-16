# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
import json
from django.views.decorators.csrf import csrf_exempt

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
                    from tastypie.models import ApiKey
                    api = ApiKey.objects.create(user=user)
                    data.update({
                        "message" : "Login successfully",
                        "data" : {
                            "access_token" : api.key,
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


