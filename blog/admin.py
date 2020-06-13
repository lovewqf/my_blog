from django.contrib import admin
from .models import *
import xadmin
# Register your models here.

class BlogAdmin(object):
    model_icon = 'fa fa-home'
class CagatoryAdmin(object):
    model_icon = 'fa fa-home'
class TagAdmin(object):
    model_icon = 'fa fa-home'
class CommentAdmin(object):
    model_icon = 'fa fa-home'

xadmin.site.register(Blog,BlogAdmin)
xadmin.site.register(Catagory,BlogAdmin)
xadmin.site.register(Tag,BlogAdmin)
xadmin.site.register(Comment,BlogAdmin)
