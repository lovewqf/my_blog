from django.contrib import admin
from .models import *
import xadmin
from xadmin import views
# Register your models here.
class GlobalSetting(object):
    #设置后台标题
    site_title = '浅笑安然'
    #设置底部信息
    site_footer = '上海天璨计算机科技公司'
    # 设置菜单可折叠
    menu_style = 'accordion'

class UserAdmin(object):
    model_icon = 'fa fa-home'
class BaseSetting(object):
    #启用主题管理器
    enable_themes = True
    # 使用主题
    use_bootswatch = True
# 注册主题设置


xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSetting)
xadmin.site.register(User,UserAdmin)
# xadmin.site.register(User)