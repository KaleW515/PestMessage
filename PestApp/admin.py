from django.contrib import admin
from PestApp.models import UserInfo, Comments, Donation, Reply, Volunteer, KeyWords
from django_redis import get_redis_connection


# Register your models here.
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['username', 'phoneNumber', 'last_login', 'is_staff', 'date_joined']
    search_fields = ['username', 'phoneNumber']
    actions = ['thaw', 'freeze']

    def thaw(self, request, queryset):
        conn = get_redis_connection()
        for i in range(len(queryset.all())):
            username = queryset.all()[i]
            phoneNumber = UserInfo.objects.get(username=username).phoneNumber
            if phoneNumber != '':
                conn.hset('Info:' + phoneNumber, 'loginCount', 0)
                conn.hset('Info:' + phoneNumber, 'isFreeze', 0)

    def freeze(self, request, queryset):
        conn = get_redis_connection()
        for i in range(len(queryset.all())):
            username = queryset.all()[i]
            phoneNumber = UserInfo.objects.get(username=username).phoneNumber
            if phoneNumber != '':
                conn.hset('Info:' + phoneNumber, 'isFreeze', 1)

    thaw.short_description = '解冻选中条目'
    freeze.short_description = '冻结选中条目'


class CommentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'from_phonenumber', 'likenum', 'dislikenum', 'content', 'date', 'name']
    search_fields = ['id', 'from_phonenumber', 'name']


class KeyWordsAdmin(admin.ModelAdmin):
    list_display = ['keyWord']
    search_fields = ['id', 'keyWord']


class DonationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phonenumber', 'mask', 'suit', 'alcohol', 'instant', 'water']
    search_fields = ['id', 'name', 'phonenumber']


class ReplyAdmin(admin.ModelAdmin):
    list_display = ['id', 'from_phonenumber', 'to_commentsid', 'from_name', 'date', 'content']
    search_fields = ['id', 'from_phonenumber', 'to_commentsid', 'from_name', 'date', 'content']


class VolunteerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phonenumber', 'qqnum', 'date1', 'date2', 'isdoctor', 'advantage', 'words']
    search_fields = ['id', 'name', 'phonenumber', 'qqnum', 'date1', 'date2', 'isdoctor', 'advantage', 'words']


admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(KeyWords, KeyWordsAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Donation, DonationAdmin)
admin.site.register(Reply, ReplyAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
