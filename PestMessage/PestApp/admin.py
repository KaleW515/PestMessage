from django.contrib import admin
from PestApp.models import UserInfo, Comments, Donation, Reply, Volunteer, Keywords
from django_redis import get_redis_connection


# Register your models here.
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['username', 'last_login', 'is_staff', 'date_joined']
    search_fields = ['username']
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
    list_display = ['comment_id', 'user_id', 'likenum', 'dislikenum', 'content', 'date']
    search_fields = ['comment_id', 'user_id', 'name']


class KeyWordsAdmin(admin.ModelAdmin):
    list_display = ['keyword']
    search_fields = ['id', 'keyWord']


class DonationAdmin(admin.ModelAdmin):
    list_display = ['donation_id', 'phone', 'username', 'user_id', 'mask', 'suit', 'alcohol', 'convenient', 'water']
    search_fields = ['donation_id', 'phone', 'username', 'user_id']


class ReplyAdmin(admin.ModelAdmin):
    list_display = ['reply_id', 'from_user_id', 'to_comment_id', 'date', 'content']
    search_fields = ['reply_id', 'from_user_id', 'to_comment_id', 'date', 'content']


class VolunteerAdmin(admin.ModelAdmin):
    list_display = ['volunteer_id', 'username', 'phone', 'user_id', 'qqnum', 'date1', 'date2', 'isdoctor', 'advantage', 'words']
    search_fields = ['volunteer_id', 'username', 'phone', 'user_id', 'qqnum', 'date1', 'date2', 'isdoctor', 'advantage', 'words']


admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(Keywords, KeyWordsAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Donation, DonationAdmin)
admin.site.register(Reply, ReplyAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
