from user.models import User
from django.core.cache import cache
from lib.http import render_json
from django.http import HttpResponse
from common import error
from user.logic import send_verify_code, check_vcode, save_upload_file
from user.forms import ProfileForm


def get_verify_code(request):
    '''手机注册'''
    phonenum = request.GET.get('phonenum')
    print(phonenum)
    send_verify_code(phonenum)
    return render_json(None, error.OK)

def login(request):
    '''短信验证登录'''
    phonenum = request.POST.get('phonenum')
    vcode = request.POST.get('vcode')

    if not check_vcode(phonenum, vcode):
        # 获取用户
        user, created = User.objects.get_or_create(phonenum=phonenum)
        # 记录登录状态
        request.session['uid'] = user.id
        return render_json(user.to_dict())
    else:
        return render_json(None, error.OK)


def get_profile(request):
    """获取个人资料"""
    user = request.user
    key = 'Profile-%s' % user.id
    user_profile = cache.get(key)
    print('从缓存获取: %s' % user_profile)

    if not user_profile:
        user_profile = user.profile.to_dict()
        print('从数据库获取: %s' % user_profile)
        cache.set(key, user_profile)
        print('将数据添加到缓存')
    return render_json(user_profile)

def modify_profile(request):
    '''修改个人资料'''
    form = ProfileForm(request.POST)
    if form.is_valid():
        user = request.user
        print('user',user)
        user.profile.__dict__.update(form.cleaned_data)
        user.profile.save()
        print('1234')
        # 修改缓存
        key = 'Profile-%s' % user.id
        cache.set(key, user.profile.to_dict())
        return render_json( user.profile.to_dict())
    else:

        return render_json(form.errors, error.PROFILE_ERROR)

def upload_avatar(request):
    '''头像上传'''
    file = request.FILES.get('avatar')
    if not file:
        save_upload_file(request.user, file)
        return render_json(None)
    else:
        # return render_json(None, error.FILE_NOT_FOUND)
        raise error.FileNotFound     #最终的要写成这样
