# -*- coding: utf-8 -*-
__author__ = '隋宇飞'
__date__ = '2019/8/6  11:18'

import xadmin

from apps.courses.models import Course, Lesson, Video, CourseResource


# xadmin全局部分属性设置类
class GlobalSettings(object):
    site_title = "慕学后台管理系统"
    site_footer = "暮雪在线网"
    # menu_style = "accordion" 是否收起应用里的管理标题


class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'teacher']
    search_fields = ['name', 'desc', 'detail', 'degree', 'students']
    list_filter = ['name', 'desc', 'teacher__name', 'detail', 'degree', 'learn_times', 'students']
    list_editable = ['degree', 'desc']


class LessonAdmin(object):
    list_display = ['courses', 'name', 'add_time']
    search_fields = ['courses', 'name']
    list_filter = ['courses__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['courses', 'name', 'file', 'add_time']
    search_fields = ['courses', 'name', 'file']
    list_filter = ['courses', 'name', 'file', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
xadmin.site.register(xadmin.views.CommAdminView, GlobalSettings)    # 注册django全局配置
xadmin.site.register(xadmin.views.BaseAdminView, BaseSettings)