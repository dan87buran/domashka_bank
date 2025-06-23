def filter_by_state(data, state='EXECUTED'):
    return [item for item in data if item['state'] == state]

def sort_by_date(data, reverse=True):
    return sorted(data, key=lambda x: x['date'], reverse=reverse)
