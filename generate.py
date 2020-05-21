import random

def get_random_date():
    year = random.randint(2000, 2021)
    month = random.randint(0, 13)
    date = random.randint(0, 13)
    return '{}-{}-{}'.format(year, month, date)

def get_item_value(key, num):
    if 'id' == key:
        return '{:08}'.format(num)
    elif '_id' in key:
        return '{:08}'.format(num//random.randint(1, 10))
    elif 'weight' == key:
        return '{} g'.format(random.randint(100, 2000))
    elif 'stock' == key:
        return '{} 件'.format(random.randint(0, 100))
    elif 'payment' == key:
        return '{} 元'.format(random.randint(0, 100))
        # e = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz123456789', 8))
        # e += random.choice(['@qq.com', '@zju.edu.cn'])
        # return e
    elif 'production_date' == key:
        return get_random_date()
    elif 'shelf_life' == key:
        return '{} 天'.format(random.randint(0, 10))
        # return str(get_random_date())

_factory = {
        'item': get_item_value
        }

def get_random_value(table, key, num):
    return _factory[table](key, num)

def generate(table, keys):
    lines = []
    for i in range(100):
        sql = 'INSERT INTO ' + table + ' (' + keys[0]
        for j in range(len(keys)-1):
            sql +=  ', ' + keys[j+1]
        sql += ') VALUES (\'' + get_random_value(table, keys[0], i) + '\''
        for j in range(len(keys)-1):
            sql +=  ', \'' + get_random_value(table, keys[j+1], i) + '\''
        sql += ');'
        lines.append(sql)
    with open(table+'.sql', 'w') as f:
        for line in lines:
            f.write(line)
            f.write('\n')

if __name__ == '__main__':
    table = 'item'
    keys = ['id', 'merchant_id', 'weight', 'stock', 'payment', 'production_date', 'shelf_life']
    # table = 'merchant'
    # keys = ['account', 'password', 'contact', 'payment', '', 'production_date', 'shelf_life']
    generate(table, keys)

