from user.models import User
from lib.http import render_json
from django.http import HttpResponse
from common import error
# from user.logic import send_verify_code, check_vcode, save_upload_file
from user.logic import send_verify_code,check_vcode


def get_verify_code(request):
    '''手机注册'''
    phonenum = request.GET.get('phonenum')
    print(phonenum)
    send_verify_code(phonenum)
    return render_json(None, error.VCODE_ERROR)

def login(request):
    '''短信验证登录'''
    phonenum = request.POST.get('phonenum')
    vcode = request.POST.get('vcode')

    if check_vcode(phonenum, vcode):
        # 获取用户
        user, created = User.objects.get_or_create(phonenum=phonenum)
        # 记录登录状态
        request.session['uid'] = user.id
        return render_json(user.to_dict())
    else:
        return render_json(None, error.VCODE_ERROR)

