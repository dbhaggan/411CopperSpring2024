from django.contrib import admin
from .newmodels import UserProfile, UserType, SchoolProfile, SchoolUser, UserInformation, Subscription, SchoolInformation, Payment, AppSettings, Sheets, Performances, Instruments, Engagements, Feedbacks
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(UserType)
admin.site.register(SchoolProfile)
admin.site.register(SchoolUser)
admin.site.register(UserInformation)
admin.site.register(Subscription)
admin.site.register(SchoolInformation)
admin.site.register(Payment)
admin.site.register(AppSettings)
admin.site.register(Sheets)
admin.site.register(Performances)
admin.site.register(Instruments)
admin.site.register(Engagements)
admin.site.register(Feedbacks)