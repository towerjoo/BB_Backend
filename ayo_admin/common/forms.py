from django.forms.util import ErrorList

class RawErrorList(ErrorList):
    def __unicode__(self):
        return self.as_raw_string()
    def as_raw_string(self):
        if not self: return u''
        return '</br>'.join(self)
