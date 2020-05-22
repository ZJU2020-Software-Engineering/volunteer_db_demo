import random

def get_random_date():
    year = random.randint(2000, 2021)
    month = random.randint(1, 12)
    date = random.randint(1, 28)
    return '{}-{}-{}'.format(year, month, date)

def get_random_time():
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    return '{}:{}:{}'.format(hour, minute, second)

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

def get_merchant_value(key, num):
    if 'account' == key:
        return '{:08}'.format(num)
    elif '_id' in key:
        return '{:08}'.format(num//random.randint(1, 10))
    elif 'password' == key:
        return ''.join(random.sample('abcdefghijklmnopqrstuvwxyz123456789', 10))
    elif 'contact' == key:
        return random.choice(['188', '137', '131', '173', '136']) + ''.join(random.sample('0123456789', 8))
    elif 'address' == key:
        return random.choice(['玉泉校区1食堂', '玉泉校区2食堂', '紫金港校区风味食堂'])
    elif 'payment' == key:
        # return '{} 元'.format(random.randint(0, 100))
        e = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz123456789', 8))
        e += random.choice(['@qq.com', '@zju.edu.cn'])
        return e
    elif 'owner_name' == key:
        return ''.join(random.sample('abcdefghijklmnopqrstuvwxyz123456789', 8))
    elif 'description' == key:
        return '无相关描述'
        # return str(get_random_date())

def get_shoppingorder_value(key, num):
    if 'id' == key:
        return '{:08}'.format(num)
    elif '_id' in key:
        return '{:08}'.format(num//random.randint(1, 10))
    elif 'total_price' == key:
        return '{}'.format(random.randint(0, 100))
    elif 'item_list' == key:
        ret = ''
        length = random.randint(1, 5)
        for i in range(length):
            ret += '{}, '.format(random.randint(1, 100))
        return ret
    elif 'time' in key:
        return get_random_date() + ' ' + get_random_time()
    elif 'stat' == key:
        return random.choice(['配送中', '打包中', '已完成'])


def get_volunteeractivity_value(key, num):
    if 'id' == key:
        return '{:08}'.format(num)
    elif 'name' == key:
        return ''.join(random.sample('abcdefghijklmnopqrstuvwxyz123456789', 10))
    elif 'type' == key:
        return random.choice(['社区', '配送'])
    elif 'location' == key:
        return random.choice(['紫金港校区', '玉泉校区', '华家池校区', '西溪校区'])
    elif 'time' in key:
        return get_random_date() + ' ' + get_random_time()
    elif 'num_recruit' == key:
        return '{}'.format(random.randint(100, 150))
    elif 'remain_recruit' == key:
        return '{}'.format(random.randint(50, 100))

def get_tenant_value(key, num):
    if 'account' == key:
        return '{:08}'.format(num)
    elif 'id' in key:
        return '{:08}'.format(num)
    elif 'password' == key:
        return ''.join(random.sample('abcdefghijklmnopqrstuvwxyz123456789', 10))
    elif 'contact' == key:
        return random.choice(['188', '137', '131', '173', '136']) + ''.join(random.sample('0123456789', 8))
    elif 'address' == key:
        return random.choice(['玉泉校区32舍', '玉泉校区12舍', '玉泉校区图书馆', '紫金港校区图书馆'])

def get_volunteertaken_value(key, num):
    if 'v_id' == key:
        return '{:08}'.format(num)
    elif 'va_id' in key:
        return '{:08}'.format(num//random.randint(1, 10))
    elif 'service_time' == key:
        return '{}'.format(random.randint(1, 10))



_factory = {
        'item': get_item_value,
        'merchant': get_merchant_value,
        'shoppingorder': get_shoppingorder_value,
        'volunteeractivity': get_volunteeractivity_value,
        'tenant': get_tenant_value,
        'volunteertaken': get_volunteertaken_value,
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
            print(keys[j+1])
            sql +=  ', \'' + get_random_value(table, keys[j+1], i) + '\''
        sql += ');'
        lines.append(sql)
    with open('sql/' + table+'.sql', 'w') as f:
        for line in lines:
            f.write(line)
            f.write('\n')

if __name__ == '__main__':
    table = 'item'
    keys = ['id', 'merchant_id', 'weight', 'stock', 'payment', 'production_date', 'shelf_life']
    table = 'merchant'
    keys = ['account', 'password', 'contact', 'payment', 'address', 'owner_name', 'description']
    table = 'shoppingorder'
    keys = ['id', 'm_id', 't_id', 'v_id', 'item_list', 'total_price', 'expected_time', 'order_time', 'stat']
    table = 'volunteeractivity'
    keys = ['id', 'name', 'type', 'location', 'time_', 'num_recruit', 'remain_recruit']
    table = 'tenant'
    keys = ['account', 'password', 'id', 'address', 'contact']
    table = 'volunteertaken'
    keys = ['v_id', 'va_id', 'service_time']
    generate(table, keys)

