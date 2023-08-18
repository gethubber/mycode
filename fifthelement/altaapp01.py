#!/usr/bin/python3
"""Alta3 Research
All in one Django settings to drive Djanjo webserver"""

DEBUG = True                            # verbose output and prevent config of
                                        # ALLOWED_HOSTS variable

SECRET_KEY = 'Youcandanc3youcanjiv3'    # required for a django app

ROOT_URLCONF = __name__                 # The path to the URIs (called URLs here) with the 'views' in
                                        # the project. The var __name__ means "look in this file"

urlpatterns = []                        # urlpatterns usually defined by ROOT_URLCONF

