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
    phoneNumber = models.CharField(max_length=11)
    signature = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class UserInfoView(models.Model):
    username = models.CharField(max_length=150, null=False, unique=True, primary_key=True)
    phoneNumber = models.CharField(max_length=11)
    signature = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'userInfoView'


class Comments(models.Model):
    id = models.IntegerField(primary_key=True)
    from_phonenumber = models.CharField(db_column='from_phoneNumber', max_length=11)  # Field name made lowercase.
    likenum = models.IntegerField(db_column='likeNum', blank=True, null=True)  # Field name made lowercase.
    dislikenum = models.IntegerField(db_column='disLikeNum', blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(max_length=200, blank=True, null=True)
    date = models.CharField(max_length=10)
    name = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'comments'


class KeyWords(models.Model):
    id = models.IntegerField(primary_key=True)
    keyWord = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'keyWords'


class Donation(models.Model):
    name = models.CharField(max_length=10)
    phonenumber = models.CharField(db_column='phoneNumber', max_length=11)  # Field name made lowercase.
    mask = models.IntegerField(blank=True, null=True)
    suit = models.IntegerField(blank=True, null=True)
    alcohol = models.IntegerField(blank=True, null=True)
    instant = models.IntegerField(blank=True, null=True)
    water = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'donation'


class Reply(models.Model):
    id = models.IntegerField(primary_key=True)
    from_phonenumber = models.CharField(db_column='from_phoneNumber', max_length=11)  # Field name made lowercase.
    to_commentsid = models.IntegerField(db_column='to_commentsId')  # Field name made lowercase.
    from_name = models.CharField(max_length=10)
    date = models.CharField(max_length=10)
    content = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reply'


class Volunteer(models.Model):
    name = models.CharField(max_length=10)
    phonenumber = models.CharField(db_column='phoneNumber', unique=True, max_length=11)  # Field name made lowercase.
    qqnum = models.CharField(db_column='qqNum', max_length=10)  # Field name made lowercase.
    date1 = models.CharField(max_length=8)
    date2 = models.CharField(max_length=8)
    isdoctor = models.IntegerField(db_column='isDoctor')  # Field name made lowercase.
    advantage = models.CharField(max_length=20)
    words = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'volunteer'
