from django.contrib import admin
from borrower.models import Borrower as CustomUser, BorrowerFeedItem


admin.site.register(CustomUser)
admin.site.register(BorrowerFeedItem)

