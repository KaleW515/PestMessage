# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserInfo(AbstractUser):
    signature = models.CharField(max_length=50, blank=True, null=True)
    attachment_uuid = models.CharField(max_length=36)

    def __str__(self):
        return self.username


class UserInfoView(models.Model):
    user_id = models.IntegerField(db_column='id', primary_key=True)
    username = models.CharField(max_length=150)
    signature = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'userInfoView'


class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    likenum = models.IntegerField(db_column='likeNum', blank=True, null=True)  # Field name made lowercase.
    dislikenum = models.IntegerField(db_column='disLikeNum', blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'comments'


class Donation(models.Model):
    donation_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    user_id = models.IntegerField()
    mask = models.IntegerField(blank=True, null=True)
    suit = models.IntegerField(blank=True, null=True)
    alcohol = models.IntegerField(blank=True, null=True)
    convenient = models.IntegerField(blank=True, null=True)
    water = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'donation'


class Keywords(models.Model):
    keyword = models.CharField(db_column='keyWord', unique=True, max_length=100, blank=True,
                               null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'keyWords'


class Reply(models.Model):
    reply_id = models.AutoField(primary_key=True)
    from_user_id = models.IntegerField()
    to_comment_id = models.IntegerField()
    date = models.DateTimeField()
    content = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reply'


class Volunteer(models.Model):
    volunteer_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    user_id = models.IntegerField(unique=True)
    qqnum = models.CharField(db_column='qqNum', max_length=10)  # Field name made lowercase.
    date1 = models.CharField(max_length=8)
    date2 = models.CharField(max_length=8)
    isdoctor = models.IntegerField(db_column='isDoctor')  # Field name made lowercase.
    advantage = models.CharField(max_length=20)
    words = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'volunteer'


class Attachment(models.Model):
    attachment_name = models.TextField(db_column='attachment_name')
    attachment_uuid = models.CharField(db_column='attachment_uuid', max_length=36, primary_key=True)

    class Meta:
        managed = False
        db_table = 'attachment'
