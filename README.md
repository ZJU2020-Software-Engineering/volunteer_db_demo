# volunteer_db_demo

##　用例

```
1. node volunteer.js
2. node client.js
```

volunteer.js作为一个连接远程数据库的服务器.

终端需要通过post和get来获取数据，这两种操作需要一个url和一个body。
我们在client.js中提供了向shoppingOrder进行insert和select的示例代码，
其中insert的url是

```` javascript
'request/shoppingOrder/insert'
````


body的内容是

````javascript
var insert_data={
    id: 'jams2',
    m_id: 'jams3',
    t_id: '14',
    item_list: '001, 002, 003, 004',
    total_price: 9.53,
    v_id: '2',
    stat: 'done',
    payment: 'test'
}
````

select的url是

```javascript
'/request/shoppingOrder/selectmid'
```

body的内容是

```javascript
var data={
    account: 'jams3'
}
```

## 数据表提供的操作

### item

insert、selectid、selectm_id即插入，根据商品id选择，根据商人id选择。

url和body分别为

```javascript
'/request/item/insert'
'/request/item/selectid'
'/request/item/selectm_id'

var insertParams = [   
    id: 'xxx',
    merchant_id: 'xxx',
    weight: 'xxx',
    stock: 'xxx',
    payment: 'xxx',
    production_date: 'xxx',
    shelf_life: 'xxx'
];

var selectidParams = [   
    id: 'xxx'
];

var selectm_idParams = [   
    m_id: 'xxx'
];
```

### merchant

insert和select两种操作。

```javascript
'/request/merchant/insert'
'/request/merchant/select'

var insertParams = [   
    account: 'xxx',
    password: 'xxx',
    contact: 'xxx',
    payment: 'xxx'
];

var selectParams = [   
    account: 'xxx'
]; 
```

### shoppingOrder

insert、selectid、selectm_id即插入，根据商品id选择，根据商人id选择。

```javascript
'/request/shoppingOrder/insert'
'/request/shoppingOrder/selectid'
'/request/shopingOrder/selectmid'

var insertParams = [   
    id: 'xxx',
    m_id: 'xxx',
    t_id: 'xxx',
    item_list: 'xxx',
    total_price: 'xxx',
    v_id: 'xxx',
    stat: 'xxx',
    payment: 'xxx'
];

var selectidParams = [   
    id: 'xxx'
];

var selectmidParams = [   
    account: 'xxx'
];
```



## 其他数据表

```javascript
'/request/sqlall'

var sql = 'show tables'; //任意的sql语句
```



## 数据表的定义

```mysql
    CREATE TABLE item(
        id VARCHAR(20) NOT NULL,
        merchant_id VARCHAR(30) NOT NULL,
        weight VARCHAR(20),
        stock VARCHAR(20),
        payment VARCHAR(30),
        production_date DATE,
        shelf_life VARCHAR(20),
        PRIMARY KEY (id),
    )
    CREATE TABLE merchant(
        account VARCHAR(20) NOT NULL
        password VARCHAR(20) NOT NULL,
        contact VARCHAR(40),
        payment VARCHAR(30),
        PRIMARY KEY ( account )
    )
    CREATE TABLE shoppingOrder(
        id VARCHAR(20) NOT NULL,
        m_id VARCHAR(20) NOT NULL,
        t_id VARCHAR(20),
        item_list text,
        total_price NUMERIC(8, 2),
        v_id VARCHAR(20),
        stat VARCHAR(20),
        payment VARCHAR(20),
        PRIMARY KEY ( id )
    )
    CREATE TABLE volunteerActivity(
        id VARCHAR(20) NOT NULL
        name VARCHAR(20) NOT NULL,
        type VARCHAR(20) NOT NULL,
        location VARCHAR(100),
        time_ TIME,
        num_recruit INTEGER NOT NULL,
        remain_recruit INTEGER NOT NULL,
        pre_part INTEGER,
        already_part INTEGER,
        PRIMARY KEY (id)
    )
    CREATE TABLE tenant(
        account VARCHAR(20) NOT NULL
        password VARCHAR(20) NOT NULL,
        id VARCHAR(20) NOT NULL,
        address VARCHAR(100),
        contact VARCHAR(40),
        payment VARCHAR(30),
        v_id VARCHAR(20),
        PRIMARY KEY (account)
    )
    CREATE TABLE volunteerTaken(
        v_id VARCHAR(20) NOT NULL,
        va_id VARCHAR(20) NOT NULL,
        service_time NUMERIC(6, 2),
        PRIMARY KEY (v_id, va_id)
    )
   
```

