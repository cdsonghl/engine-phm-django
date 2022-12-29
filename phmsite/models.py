from django.db import models
import datetime

class engine_base_info(models.Model):
    last_alarm_datetime = models.DateTimeField("last_alarm_time", default=datetime.date(1900,1,1))
    next_repair_date = models.DateField("next_repair_time", default=datetime.date(1900,1,1))

    def __str__(self):
        return '%s_%s'%(self.last_alarm_datetime, self.next_repair_date)

class engine_alarm_info(models.Model):
    alarm_datetime = models.DateTimeField("alarm_time", default=datetime.date(1900, 1, 1))
    system = models.CharField('system', max_length=20)
    alarm_class = models.IntegerField('alarm_class')
    events = models.CharField('events', max_length=100)

    def __str__(self):
        return '%s_%s_%s_%s'%(self.alarm_datetime, self.system, self.alarm_class, self.events)