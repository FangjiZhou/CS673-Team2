from datetime import datetime


def parse_date(date_str):
    """
        Helper function to create/parse datetime from string
        Inputs :
            - 2018-11-02T11:54:53.645+00:00
            - 2018-07-11
            - 2019-01-18 13:57:43
        return datetime.datetime()
    """
    try:
        if isinstance(date_str, str) and len(date_str) > 5:
            if '.' in date_str and 'T' in date_str:  # 2018-11-02T11:54:53.645+00:00
                return datetime.strptime(date_str.split('.')[0], '%Y-%m-%dT%H:%M:%S')
            elif ':' in date_str and ' ' in date_str: # 2019-01-18 13:57:43
                return datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
            else:  # 2018-07-11
                return datetime.strptime(date_str.split('.')[0], '%Y-%m-%d')
        else:
            return None
    except Exception as e:
        raise Exception('fail in date parser for :' + date_str + '  ' + str(e))


# print(type(parse_date("2019-01-18 13:57:43")))
