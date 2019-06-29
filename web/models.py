from django.db import models

# Create your models here.

class network:
    def __init__(self, ssid):
        self.ssid = ssid

#TODO add the necessary info
class user:
    def __init__(self, mac):
        self.mac = mac