items = \
"""    {
        "pk": %(id)s,
        "model": "auth.user",
        "fields": {
            "username": "%(username)s",
            "first_name": "",
            "last_name": "",
            "is_active": true,
            "is_superuser": true,
            "is_staff": true,
            "last_login": "2012-09-16T04:13:17.494Z",
            "groups": [],
            "user_permissions": [],
            "password": "pbkdf2_sha256$10000$1kQGUHyYmvYs$Ntv5iN1QrXulSlVesE7xzy2F+onupnVSYODIsTc+jCY=",
            "email": "%(email)s",
            "date_joined": "2012-09-16T04:10:06.540Z"
        }
    },
    {
        "pk": %(id)s,
        "model": "account.account",
        "fields": {
            "facebook_access_token": "",
            "is_facebook_account": true,
            "last_login_time": "2012-09-16T07:13:22.482Z",
            "register_time": "2012-09-16T04:13:32.079Z",
            "longitude": 456.0,
            "user": %(id)s,
            "facebook_id": "",
            "latitude": -234.0,
            "api_access_token": "",
            "type": %(account_type)s,
            "icon": "icons/2012/09/16/icon.gif"
        }
    },
    {
        "pk": %(id)s,
        "model": "account.contactgroup",
        "fields": {
            "owner": %(id)s,
            "create_time": "2012-09-16T04:14:52.954Z",
            "name": "friends",
            "members": "%(group_members)s"
        }
    },
    {
        "pk": %(id)s,
        "model": "notification.shoutnotification",
        "fields": {
            "status": %(note_status)s,
            "shout": %(id)s,
            "receiver": %(id)s 
        }
    },
    {
        "pk": %(id)s,
        "model": "shout.shout",
        "fields": {
            "is_featured": true,
            "group": %(id)s,
            "author": %(id)s,
            "photo": "shouts/2012/09/16/kfc_2.gif",
            "venue": %(id)s,
            "content": "a new movie #bailuyuan# starts.",
            "time": "2012-09-16T07:36:30.558Z",
            "type": %(shout_type)s
        }
    },
    {
        "pk": %(id)s,
        "model": "shout.shoutcomment",
        "fields": {
            "content": "I love this venue",
            "comment_time": "2012-09-16T20:15:14Z",
            "shout": %(id)s,
            "commenter": %(id)s 
        }
    },
    {
        "pk": %(id)s,
        "model": "venue.venue",
        "fields": {
            "name": "KFC",
            "photo": "venues/2012/09/16/kfc.gif",
            "longitude": 112.0,
            "create_time": "2012-09-16T04:14:11.663Z",
            "latitude": 234.5,
            "last_edit_time": "2012-09-16T07:11:39.054Z"
        }
    },
"""
