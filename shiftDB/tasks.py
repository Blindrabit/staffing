from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from calendar_app.models import Event
from user_app.models import Profile
from .models import Shifts
from django.forms.models import model_to_dict
from datetime import datetime, timedelta


from celery import task


@task()
def shift_book():
    print('it run')
    shifts_needing_fill = Shifts.objects.filter(start_time__gte=datetime.now()).filter(manage=None)
    for s in shifts_needing_fill:
        shift_dict = model_to_dict(s)
        staff_avilible = Event.objects.filter(start_time__gte=datetime.now()).filter(title='free')
        for e in staff_avilible:
            staff_avilible_dict = model_to_dict(e)
            if shift_dict['start_time'] >= staff_avilible_dict['start_time'] and shift_dict['end_time'] <= staff_avilible_dict['end_time']:
                profile_dict = model_to_dict(Profile.objects.get(user=staff_avilible_dict['manage']))
                if shift_dict['area'][0] in profile_dict['area']:
                    Shifts.objects.filter(pk=model_to_dict(s)['id']).update(manage=profile_dict['user'])
                    Event.objects.filter(pk=model_to_dict(e)['id']).update(title=str(s))
                    break   


