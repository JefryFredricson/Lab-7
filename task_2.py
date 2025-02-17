import holidayapi
from random import randint
#Выполнен вариант 7 из-за проблем с получением ключа API с сайта с 3-его варианта

def country_name(country_tag):
    dictionary = {'FR':'France', 'GE': 'Germany', 'US': 'USA', 'RU': 'Russia', 'GB': 'Great Britain'}
    return dictionary[country_tag]

def get_api():
    hapi = holidayapi.v1("YOUR_API_KEY")
    tag = ['US', 'RU', 'GE', 'FR', 'GB'][randint(0, 5)]
    param = {'country': tag, 'year': '2024'}
    print(hapi.holidays(parameters=param))
    during_week, on_tuesday, in_may, has_m_in_name, total = 0, 0, 0, 0, 0
    inf = hapi.holidays(parameters=param)['holidays']
    for holiday in inf:
        total += 1
        if holiday['date'] != holiday['observed']: print(holiday['name'])
        if holiday['weekday']['date']['name'] == 'Tuesday': on_tuesday += 1
        if holiday['date'][5:7] == '05': in_may += 1
        if holiday['weekday']['date']['name'] not in ['Saturday', 'Sunday']: during_week += 1
        if 'm' in holiday['name']: has_m_in_name += 1
    return f'{country_name(tag)} celebrated {total} holidays in 2024\n{during_week} were celebrated during weekdays\n{on_tuesday} were celebrated on Tuesday\n{in_may} happened in May\n{has_m_in_name} had m in name'

print(get_api())