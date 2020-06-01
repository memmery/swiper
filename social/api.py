from django.shortcuts import render
from lib.http import render_json
from social.logic import get_rcmd_users

# Create your views here.

def get_users(request):

    ''' 获取推荐用户 '''
    per_page = 10
    page = int(request.GET.get('page',1))  #‘页码“
    start = (page - 1)*per_page
    end = start + per_page

    users=get_rcmd_users(request.user)[start:end]  #"匹配的所有用户"
    result = [u.to_dict() for u in users]
    return render_json(result)

def like(request):
    pass

def superlike(request):
    pass

def dislike(request):
    pass

def rewind(request):
    pass

def friends(request):
    pass

