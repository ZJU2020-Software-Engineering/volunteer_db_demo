var axios =  require('axios');
var instance=axios.create({
    baseURL:'http://0.0.0.0:4000',//改成服务器的url
    // baseURL:'http://121.199.7.115:4000',//改成服务器的url
    timeout: 10000,
    headers: {'X-Custom-Header': 'foobar'}
});

// // order example
// var insert_data={
//     id: 'jams2',
//     m_id: 'jams3',
//     t_id: '14',
//     item_list: '001, 002, 003, 004',
//     total_price: 9.53,
//     v_id: '2',
//     stat: 'done',
//     payment: 'test'
// }
// instance.post('/request/shoppingOrder/insert', insert_data).then(
//     (res)=>{
//         JSON.stringify(res.data);
//         if(res.data.message=='Success'){
//             console.log("OK");
//         }
//         else{
//             console.log("Not OK");
//         }
//     }
// ).catch(
//     (error)=>{}
// );


//
var data={
    account: 'jams3'
}
instance.get('/request/shoppingOrder/selectmid',{params:data}).then(function (response) {
        console.log(response.data.message);
    }).catch(function (error) {
    console.log(error);
});

