from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Employee)
admin.site.register(EmpLeaveRequest)
admin.site.register(LeaveBalance)
admin.site.register(EmpMgrDept)
admin.site.register(HolidayList)