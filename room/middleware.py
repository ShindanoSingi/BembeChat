import datetime
from django.core.cache import cache
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin


# import datetime
# from django.core.cache import cache
# from django.conf import settings

# class ActiveUserMiddleware(MiddlewareMixin):
#     def process_request(self, request):
#         current_user = request.user
#         if current_user.is_authenticated:
#             now = datetime.datetime.now()
#             cache.set('seen_%s' % (current_user.username), now,
#             settings.USER_LASTSEEN_TIMEOUT)





# class ActiveUserMiddleware(MiddlewareMixin):
#     def process_request(self, request):
#         current_user = request.user
#         if request.user.is_authenticated:
#             now = datetime.datetime.now()
#             cache.set('seen_%s' % (current_user.username), now,
#                 settings.USER_LASTSEEN_TIMEOUT)