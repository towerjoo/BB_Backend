import urllib, urllib2

url = "http://www.fandura.com/ayo"
register_url = "%s/api/v1/account/register/" % url
login_url = "%s/api/v1/account/login/" % url

data = {
    "username" : "abcdef",
    "password" : "abcdef",
    "email" : "abcdef@gmail.com",
    "firstname" : "test1",
    "lastname" : "test2",
    "gender" : "male",
}

fh = urllib2.urlopen(register_url, data=urllib.urlencode(data))
print fh.read()
fh.close()


fh = urllib2.urlopen(login_url, data="username=abcdef&password=abcdef")
print fh.read()
fh.close()
