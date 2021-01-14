from django.db import models
from LMS_Manager.common.util import ChoiceEnum
from django.utils import timezone
import datetime

# Create your models here.

class EmployeeGenderChoise(ChoiceEnum):
    Male = 'M'
    Female = 'F'

class EmployeeDesignationChoices(ChoiceEnum):
    Employee = 'Employee'
    Manager = 'Manager'
    HR = 'HR'

class EmployeeWorkTypeChoices(ChoiceEnum):
    Permanent = 'Permanent'
    Probationary = 'Probationary'
    Limited_term = 'Limited-term'
    Temporary='Temporary'


class EmpLeaveRequestChoices(ChoiceEnum):
    Sick_Leave = 'Sick'
    Annual_Leave = 'Annual'
    Pregnancy_Disability_Leave = 'PDL'

class EmpLeaveRequestStatus(ChoiceEnum):
    Pending_Status = 'Pending'
    Approved_Status = 'Approved'
    Declined_Status = 'Declined'
    Cancelled_Status = 'Cancelled'


class Employee(models.Model):

    Emp_No = models.AutoField(primary_key=True,help_text='Unique Emp no for employee table')
    First_Name = models.CharField(max_length=14,help_text='employee first name')
    Middle_Name = models.CharField(max_length=14,null=True,help_text='employee middle name')
    Last_Name = models.CharField(max_length=14,help_text='employee last name')
    Birth_Date = models.DateField(help_text='employee birth date')
    Gender = models.CharField(max_length=30, choices=EmployeeGenderChoise.choices())
    Street_Address = models.CharField(max_length=50)
    Address2 = models.CharField(max_length=50, null=True)
    City = models.CharField(max_length=20)
    State = models.CharField(max_length=20)
    Postal_Code = models.PositiveIntegerField(default=0)
    Country = models.CharField(max_length=20)
    Mobile_Number = models.PositiveIntegerField(default=0)
    Email_Address = models.EmailField(max_length=70)
    Hire_Date = models.DateField(help_text='Employee joining date')
    End_Date = models.DateField(null=True,help_text='Employee last working date in organization')
    Designation = models.CharField(max_length=10, choices=EmployeeDesignationChoices.choices())
    Nationality = models.CharField(max_length=50)
    Worktype = models.CharField(max_length=15, choices=EmployeeWorkTypeChoices.choices())
    IsActive = models.BooleanField(null=True)

    def __str__(self):
        return '%s %s %s' % (self.Emp_No, self.First_Name, self.Last_Name)


class EmpLeaveRequest(models.Model):

    EmpLeave_Req_ID = models.AutoField(primary_key=True)
    Emp_ID = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="Emp_ID", default=0)
    Emp_FullName = models.CharField(max_length=50)
    Leave_Type = models.CharField(max_length=30, choices=EmpLeaveRequestChoices.choices())
    Manager_Emp_No = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="Manager_Emp_No", default=0)
    Manager_FullName = models.CharField(max_length=50)
    Begin_Date = models.DateField(help_text='Leave begin date')
    End_Date = models.DateField(help_text='Leave end date')
    Requested_Days = models.PositiveIntegerField(default=0,help_text='Total no of requested leave days')
    Leave_Status = models.CharField(max_length=30, choices=EmpLeaveRequestStatus.choices())
    Emp_Comments = models.CharField(max_length=500, null=True)

    def __str__(self):
        return '%s %s %s' % (self.EmpLeave_Req_ID, self.Emp_ID, self.Emp_FullName)


class LeaveBalance(models.Model):

    LeaveBal_ID = models.AutoField(primary_key=True)
    Emp_No_LeaveBal = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Leave_Type = models.CharField(max_length=30, choices=EmpLeaveRequestChoices.choices())
    Available_Days = models.PositiveIntegerField(default=0, help_text='Remaining/available leave days per employee')
    Allocated_Days = models.PositiveIntegerField(default=0, help_text='No of leave days allocated to a leave type per '
                                                                      'employee per year')

    def __str__(self):
        return '%s %s' % (self.Emp_No_LeaveBal, self.Leave_Type)


class EmpMgrDept(models.Model):
    Emp_MgrDept_ID = models.AutoField(default=0,primary_key=True)
    Emp_No_EmpMgrDept = models.ForeignKey(Employee, on_delete=models.CASCADE,related_name='Emp_No_EmpMgrDept',default=0)
    Dept_ID = models.PositiveIntegerField(default=0)
    Manager_Emp_ID = models.ForeignKey(Employee, on_delete=models.CASCADE,related_name='Manager_Emp_ID',default=0)
    Emp_FullName = models.CharField(max_length=50)
    Dept_Name = models.CharField(max_length=30)
    Manager_FullName = models.CharField(max_length=50)
    Manager_Email_Address = models.EmailField(max_length=70)

    def __str__(self):
        return '%s %s' % (self.Emp_MgrDept_ID, self.Manager_Emp_ID)

class HolidayList(models.Model):
    
    HOLIDAY_TYPE =[
        ('Mandatory','Mandatory'),
        ('Optional','Optional'),
    ]

    Day_List = [
        ('Sunday','Sunday'),
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
    ]

    Date = models.DateField()
    Month = models.CharField(max_length=10)
    Day = models.CharField(max_length=10, choices=Day_List)
    Occasion = models.CharField(max_length=50)
    Location = models.CharField(max_length=30, default='Bangalore')
    Type = models.CharField(max_length=20,choices=HOLIDAY_TYPE)

    def __str__(self):
        return '%s %s %s' % (self.Date, self.Occasion, self.Type)