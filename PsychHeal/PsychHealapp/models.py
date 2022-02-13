from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Signup(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=320,null=False,blank=False)
    first_name = models.CharField(max_length=50,null=False,blank=False)
    last_name = models.CharField(max_length=50,null=False,blank=False)
    gender = models.CharField(default="null",max_length=50,null=False,blank=False)
    mobile_no = models.CharField(max_length=50,null=False,blank=False)
    dob = models.DateField(blank=True, null=True)

    occupation = models.CharField(max_length=50, blank=True, null=True)
    work_schedule_start = models.TimeField(blank=True, null=True)
    work_schedule_end = models.TimeField(blank=True, null=True)

    hobbies = ArrayField(models.IntegerField(), max_length=25, blank=True, null=True)

    exercise = models.BooleanField(blank=True, null=True)
    overweight = models.BooleanField(blank=True, null=True)
    underweight = models.BooleanField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default="True")

    class Meta:
        db_table = 'user_login'

class Passwords(models.Model):

    id = models.AutoField(primary_key=True)
    failed_attempts = models.IntegerField(default=0)
    failed_attempt_time = models.DateTimeField(blank=True, null=True)
    last_login_on = models.DateTimeField(blank=True,null=True)
    last_reset_on = models.DateTimeField(blank=True, null=True)
    last_reset_date = models.DateField(blank=True, null=True)
    last_reset_time = models.TimeField(blank=True, null=True)
    unlocks_on = models.DateTimeField(blank=True,null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    passwords_changed = models.IntegerField(default=0)
    user = models.ForeignKey(Signup,related_name='PASSWORD',on_delete=models.CASCADE)
    isdefault = models.BooleanField(default=True)

    class Meta:
        db_table = 'passwords'

class PasswordHistory(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Signup,on_delete=models.DO_NOTHING,blank=True,null=True)
    changed_on = models.DateTimeField(auto_now_add=True)
    new_password = models.CharField(max_length=255,blank=True, null=True)
    old_password = models.CharField(max_length=255,blank=True, null=True)

    class Meta:
        db_table = 'passwords_history'


class LoginLogs(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Signup, related_name='ATTEMPTS', blank=True, null=True, on_delete=models.CASCADE)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.CharField(max_length=255, blank=True, null=True)
    longitude = models.CharField(max_length=255, blank=True, null=True)
    login_status = models.BooleanField(blank=True, null=True)
    cause = models.CharField(max_length=255, blank=True, null=True)
    log_date = models.DateTimeField(blank=True, null=True)
    org = models.CharField(max_length=255, blank=True, null=True)
    postal = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    region_code = models.CharField(max_length=255, blank=True, null=True)
    request_page = models.CharField(max_length=255, blank=True, null=True)
    time_zone = models.CharField(max_length=255, blank=True, null=True)
    isactive = models.IntegerField(default=1)

    class Meta:
        db_table = 'login_logs'


class PasswordResetLogs(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Signup, related_name='RESETS', blank=True, null=True, on_delete=models.CASCADE)
    forgot_token = models.CharField(max_length=255, blank=True, null=True)
    attempts = models.IntegerField(default=0)
    request_date = models.DateField(blank=True, null=True)
    expires_on = models.DateTimeField(blank=True, null=True)
    isactive = models.IntegerField(default=0)

    class Meta:
        db_table = 'password_reset_logs'

class Tokens(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.CharField(max_length=255)
    valid_upto = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(Signup, related_name='TOKEN', on_delete=models.CASCADE)

    class Meta:
        db_table = 'tokens'

class Hobbies(models.Model):
    id = models.AutoField(primary_key=True)
    hobby = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'hobbies'



