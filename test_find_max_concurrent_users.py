import unittest
import datetime
import pandas as pd

def func(timestamps :pd.DataFrame):
    timestamps.sort_values(['start','end'], ascending=[True,True], inplace=True)
    start_times = list(timestamps['start'])
    end_times = list(timestamps['end'])
    print(start_times)
    max_users=0
    curr_users = 0
    end_time_stamp_pointer = 0
    for timestamp in start_times:
        if timestamp < end_times[end_time_stamp_pointer]:
            curr_users += 1
        else:
            max_users = max(max_users, curr_users)
            end_time_stamp_pointer += 1
    return max(max_users, curr_users)


class Tests(unittest.TestCase):

    def test_1(self):
        data = {'start': [Tests.get_dt(15),  Tests.get_dt(19),Tests.get_dt(10)],
                'end': [Tests.get_dt(25), Tests.get_dt(29), Tests.get_dt(20)]
        }

        self.assertEqual(3, func(pd.DataFrame(data=data)))

    @staticmethod
    def get_dt(minute):
        return datetime.datetime(year=2022, month=6, day=25, hour=10, minute=minute)
