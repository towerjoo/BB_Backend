#coding: utf-8

class ChoiceBase(object):
    @classmethod
    def get_value(_class, _key):
        for app in _class.choices:
            _id, _name = app
            if str(_id) == str(_key):
                return _name
        return "a wrong key %s" % str(_key)

class AccountTypeChoices(ChoiceBase):
    individual = 1
    company = 2
    choices = (
        (individual, "individual"),
        (company, "company"),
    )

class ShoutTypeChoices(ChoiceBase):
    group = 1
    billboard = 2
    choices = (
        (group, "group"),
        (billboard, "billboard"),
    )

class ShoutNotificationStatusChoices(ChoiceBase):
    read = 1
    unread = 2
    choices = (
        (read, "read"),
        (unread, "unread"),
    )
