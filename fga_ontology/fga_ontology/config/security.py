"""
secret key to the project.
https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/
"""

import os

SECRET_KEY = os.getenv(
    'SECRET_KEY',
    '&wwg1)l64z)^8_z2d!3ik$zcrr5as8)-2!ce)t_s6h(&-9)$!$'
)
