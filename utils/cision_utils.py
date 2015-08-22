__author__ = 'matt.livingston'

import requests
from datetime import datetime, timedelta
import re
import json

class Toggl:

    api_token = '3bc5405b6a6448dc738679d651572563'
    toggle_url = 'https://www.toggl.com/api/v8/time_entries'
    date = datetime.now()
    content_type = "Content-Type: application/json"
    hours = 0
    toggle_user_id = 1568956
    workspace_id = 831391

    post_template = '{"time_entry": {"duration": %d,"start": "%s","pid": %d,"billable": %s,"created_with": "alfred"}}'

    # curl -v -u 3bc5405b6a6448dc738679d651572563:api_token
    # -H "Content-Type: application/json"
    # -d '{"time_entry":{"duration":28800,"start":"2015-01-01T17:00:00+00:00","pid":10049413,"billable":true,"created_with":"curl"}}'
    # -X POST https://www.toggl.com/api/v8/time_entries

    def format_payload_dict(self, duration, start, pid, billable, created_with):
        payload = {
            "time_entry": {
                "duration": duration,
                "start": start,
                "pid": pid,
                "billable": billable,
                "created_with": created_with
            }
        }
        return payload

    def convert_hours_to_minutes(self, hours):
        return hours * 60

    def format_date_time(self, date):
        split_date = str(date).split(' ')
        return split_date[0] + 'T' + split_date[1] + '+00:00'

    def parse_command(self, command):
        if "today" in command:
            self.date = datetime.now()
            self.date = self.date.replace(hour=8, minute=0, second=0, microsecond=0)
        elif "yesterday" in command:
            day = timedelta(days=1)
            self.date = datetime.now() - day
            self.date = self.date.replace(hour=8, minute=0, second=0, microsecond=0)
        else:
            self.date = datetime.now()
            self.date = self.date.replace(hour=8, minute=0, second=0, microsecond=0)

        self.hours = int(re.search(r'\d+', command).group())

        print("Date is %s" % self.date)
        print("Hours are %d" % self.hours)
        print("Hours converted to minutes are %d" % self.convert_hours_to_minutes(self.hours))

        true = True
        return self.format_payload_dict(28800, self.format_date_time(self.date), 10049413, true, 'Alfred')


    def post_time_entry(self, post):
        headers = {
            'Content-Type': 'application/json'
        }

        print(headers)
        print(post)

        r = requests.post(self.toggle_url, data=json.dumps(post), headers=headers, auth=('3bc5405b6a6448dc738679d651572563', 'api_token'))

        print(r)
        print(r.status_code)
        print(r.text)

    def update_toggl(self, command):
        post_data = self.parse_command(command)
        self.post_time_entry(post_data)


toggl = Toggl()
#toggl.parse_command("Add 8 hours to the Hancock project")
#toggl.parse_command("Add 8 hours to the Hancock project for yesterday")
toggl.update_toggl("Add 8 hours to the Hancock project")
