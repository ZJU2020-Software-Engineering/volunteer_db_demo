var axios =  require('axios');
var instance=axios.create({
    baseURL:'http://0.0.0.0:4000',//改成服务器的url
    // baseURL:'http://121.199.7.115:4000',//改成服务器的url
    timeout: 10000,
    headers: {'X-Custom-Header': 'foobar'}
});

var data = {
    sql: 'show tables'
}
instance.post('/request/sqlall', data).then(
    (res)=>{
        console.log(res.data);
    }
).catch(
    (error)=>{
        console.log('Failure');
    }
);

