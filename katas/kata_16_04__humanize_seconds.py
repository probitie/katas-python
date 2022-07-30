class test:
    @classmethod
    def assert_equals(cls, val1, val2, *args, **kwargs):
        print(val1 == val2)

def _pluralise(s, n):
    return s + 's' if n > 1 else s

def _split_seconds(seconds) -> dict:  # mb from datetime.Datetime()
    dates = {'second': 1000, 'minute': 60, 'hour': 60, 'day': 24, 'year': 365}
    dates_list = list(dates.keys())
    result = {'second': seconds}

    for i in range(len(dates.keys()) - 1):
        prev = dates_list[i]
        curr = dates_list[i + 1]
        result[curr] = result[prev] // dates[curr]
        result[prev] = result[prev] % dates[curr]

    return result


def format_duration(seconds):
    if not seconds:
        return 'now'
    time_from_sec = _split_seconds(seconds)
    _ = _pluralise

    r = _pluralise('second', 1)
    t = _pluralise('second', 13)

    join = [f'{v} {_pluralise(k, v)}' for k, v in time_from_sec.items()]
    join.reverse()
    join = [*filter(lambda s: s[0] != '0', join)]

    return ', '.join(join[:-1]) + (' and ' if len(join) > 1 else '') + join[-1]


if __name__ == '__main__':

    test.assert_equals(format_duration(1), "1 second")
    test.assert_equals(format_duration(62), "1 minute and 2 seconds")
    test.assert_equals(format_duration(120), "2 minutes")
    test.assert_equals(format_duration(3600), "1 hour")
    test.assert_equals(format_duration(3662), "1 hour, 1 minute and 2 seconds")
