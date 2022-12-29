from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from phmsite.models import engine_base_info, engine_alarm_info
import datetime


def check_login(fn):
    # 检查是否登录
    def wrap(request, *args, **kwargs):
        if 'username' not in request.session or 'uid' not in request.session:
            return HttpResponseRedirect('/login')
        return fn(request, *args, **kwargs)
    return wrap

# Create your views here.
@check_login
def homepage(request):
    # 健康运行天数和距离下次检修剩余天数计算
    engine_base_info_qs = engine_base_info.objects.all()[0]
    now = datetime.datetime.now()
    today = datetime.date.today()
    last_alarm_datetime = engine_base_info_qs.last_alarm_datetime
    next_repair_date = engine_base_info_qs.next_repair_date
    health_running_time = (now - last_alarm_datetime).days
    repair_time = (next_repair_date - today).days


    # 近一年报警次数

    # engine_alarm_info_qs = engine_alarm_info.ob0jects.filter(start_time__gt=2022)

    # 各子系统状态
    color_dic = {0: 'lawngreen', 1: 'orange', 2: 'red'}
    cooling_sys_status = color_dic[0]
    lubrication_sys_color = color_dic[1]
    work_sys_color = color_dic[2]
    print(lubrication_sys_color)

    dic = {'repair_time':repair_time, 'health_running_time':health_running_time,
           'cooling_sys_status':cooling_sys_status, 'lubrication_sys_color':lubrication_sys_color,
           'work_sys_color':work_sys_color}
    return render(request, '../templates/index.html', dic)
