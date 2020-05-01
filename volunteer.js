var http = require('http');
var mysql = require('mysql');
var experss=require('express');
var bodyParser = require('body-parser');
var dateFormat = require('dateformat');
var now = new Date();

//數據庫連接
var connection = mysql.createConnection({
    host: '182.92.243.158',
    user: 'root',
    password: 'cs0000',
    port: '3306',
    database: 'cs'
});

var app = experss();
connection.connect();
app.all('*', function (req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "X-Requested-With");
    res.header("Access-Control-Allow-Methods", "PUT,POST,GET,DELETE,OPTIONS");
    res.header("X-Powered-By", ' 3.2.1')
    //Õâ¶Î½ö½öÎªÁË·½±ã·µ»Øjson¶øÒÑ
    res.header("Content-Type", "application/json;charset=utf-8");
    if (req.method == 'OPTIONS') {
        //ÈÃoptionsÇëÇó¿ìËÙ·µ»Ø
        res.sendStatus(200);
    } else {
        next();
    }
});
// ´´½¨ application/x-www-form-urlencoded ±àÂë½âÎö
app.use(bodyParser.urlencoded({ extended: false }));

app.use(bodyParser.json())

//==============item==============================
app.post('/request/item/insert', function insertItem(req, res) {
    var getObj = req.body;//req
    var insertSQL = "INSERT INTO item(id, merchant_id, weight, stock, payment, production_date, shelf_life) "
        + "VALUES(?, ?, ?, ?, ?, ?, ?)";    //sql語句
    var nowTime = dateFormat(now, "isoDate");
    var insertParams = [    //sql語句參數
        getObj.id,
        getObj.merchant_id,
        getObj.weight,
        getObj.stock,
        getObj.payment,
        getObj.production_date,
        getObj.shelf_life
    ];
    console.log(insertParams)
    //database
    connection.query(insertSQL, insertParams, function (err, result) {
            if (err) {
                console.log('Insert Error\n');
                res.json({ result: 'N', message : err.message });
            }
            else {
                res.json({ result: 'Y', message : 'Success' });
            }
        })
    //SQLReturn('insert');
})

app.get('/request/item/selectid', function selectidItem(req, res) {
    var getObj = req.query;

    selectSQL = 'SELECT * FROM item WHERE id = ?';
    selectParams = [getObj.id];//
    connection.query(selectSQL, selectParams, function (err, result) {
            if (err) {
                res.json({ result: 'N', message : err.message });
            }
            else {
                res.json(
                    {
                        result: 'Y', message: result
                    });
            }
        })
})

app.get('/request/item/selectm_id', function selectmidItem(req, res) {
    var getObj = req.query;
    selectSQL = 'SELECT * FROM item WHERE merchant_id = ?';
    selectParams = [getObj.merchant_id];//
    connection.query(selectSQL, selectParams, function (err, result) {
            if (err) {
                console.log('Select Error\n');
                res.json({ result: 'N', message : err.message });
            }
            else {
                console.log('Select Success\n');
                res.json(
                    {
                        result: 'Y', message: result
                    });
            }
        })
})


//=============================merchant==============================
app.post('/request/merchant/insert', function insertMerchant(req, res) {
    var getObj = req.body;//req
    var insertSQL = "INSERT INTO merchant(account, password, contact, payment) "
        + "VALUES(?, ?, ?, ?)";    //sql語句
    var insertParams = [    //sql語句參數
        getObj.account,
        getObj.password,
        getObj.contact,
        getObj.payment
    ];
    console.log(insertParams)
    //database
    connection.query(insertSQL, insertParams, function (err, result) {
            if (err) {
                console.log('Insert Error\n');
                res.json({ result: 'N', message : err.message });
            }
            else {
                res.json({ result: 'Y', message : 'Success' });
            }
        })
    //SQLReturn('insert');
})

app.get('/request/merchant/select', function selectMerchant(req, res) {
    var getObj = req.query;
    selectSQL = 'SELECT * FROM merchant WHERE account = ?';
    selectParams = [getObj.account];
    console.log(selectParams)
    connection.query(selectSQL, selectParams, function (err, result) {
            if (err) {
                res.json({ result: 'N', message : err.message });
            }
            else {
                res.json(
                    {
                        result: 'Y', message: result
                    });
            }
        })
})


//=============================shoppingOrder==============================
app.post('/request/shoppingOrder/insert', function insertOrder(req, res) {
    var getObj = req.body;//req
    var insertSQL = "INSERT INTO shoppingOrder(id, m_id, t_id, item_list, total_price, v_id, stat, payment) "
        + "VALUES(?, ?, ?, ?, ?, ?, ?, ?)";    //sql語句
    var insertParams = [    //sql語句參數
        getObj.id,
        getObj.m_id,
        getObj.t_id,
        getObj.item_list,
        getObj.total_price,
        getObj.v_id,
        getObj.stat,
        getObj.payment
    ];
    console.log(insertParams)
    //database
    connection.query(insertSQL, insertParams, function (err, result) {
            if (err) {
                console.log('Insert Error\n');
                res.json({ result: 'N', message : err.message });
            }
            else {
                res.json({ result: 'Y', message : 'Success' });
            }
        })
    //SQLReturn('insert');
})

app.get('/request/shoppingOrder/selectid', function selectidOrder(req, res) {
    var getObj = req.query;
    selectSQL = 'SELECT * FROM shoppingOrder WHERE id = ?';
    selectParams = [getObj.id];
    console.log(selectParams)
    connection.query(selectSQL, selectParams, function (err, result) {
            if (err) {
                res.json({ result: 'N', message : err.message });
            }
            else {
                res.json(
                    {
                        result: 'Y', message: result
                    });
            }
        })
})

app.get('/request/shoppingOrder/selectmid', function selectmidOrder(req, res) {
    var getObj = req.query;
    selectSQL = 'SELECT * FROM shoppingOrder WHERE m_id = ?';
    selectParams = [getObj.account];
    console.log(selectParams)
    connection.query(selectSQL, selectParams, function (err, result) {
            if (err) {
                res.json({ result: 'N', message : err.message });
            }
            else {
                res.json(
                    {
                        result: 'Y', message: result
                    });
            }
        })
})



var server = app.listen(4000, function () {

    var host = server.address().address;
    var port = server.address().port;

    //console.log(" http://%s:%s", host, port);
    console.log("Server open on ",server.address());

})

