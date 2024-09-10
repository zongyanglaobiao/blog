const fetch_ = {
    post: async (url,data,call) => {
        const response = await window.fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        // 检查请求是否成功
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // 将返回的数据转为JSON格式
        const result = await response.json();
        call(result)
    },

    get: async (url, params,call) => {
        // 将params对象转换为查询字符串形式
        const queryString = new URLSearchParams(params).toString();
        const fullUrl = `${url}?${queryString}`;

        const response = await window.fetch(fullUrl, {method: 'GET'});

        // 检查请求是否成功
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // 将返回的数据转为JSON格式
        const result = await response.json();
        call(result)
    }
}

const isNullOrUndefined = (ojs) => {
    return ojs === null || ojs === undefined
}

/**
 *  生成32位数字拼上加密的
 */
const generateDeviceId = () => {
    let result = '';
    for (let i = 0; i < 32; i++) {
        result += Math.floor(Math.random() * 10);  // 生成 0-9 的随机数
    }
    return `${btoa(btoa(result))}`;
};

const getDeviceId = () => {
    return localStorage.getItem(DEVICE_ID)
}

const setDeviceId = (deviceId) => {
    localStorage.setItem(DEVICE_ID, deviceId)
}

const logDeviceId = () => {
    console.log('设备ID = ',getDeviceId())
}

const getArticleId = () => {
    return document.querySelector('.article-content').getAttribute('data-article-id')
}

const DEVICE_ID = 'device_id'
const SERVER_URL = 'http://localhost:8080'
const ADD_READ_NUM = '/article/addReadNum';
const GET_READ_NUM = '/article/getReadNum';

const addReadNum = () =>{
    if (isNullOrUndefined(getArticleId)) {
        return;
    }

    // 检查是否已已阅读了，如没请求服务端增加阅读量
    if (!isNullOrUndefined(getDeviceId())) {
        return
    }
    /*fetch_.post(SERVER_URL + ADD_READ_NUM, {articleId, DEVICE_ID:getDeviceId()},()=>{
        console.log('增加成功')
    })*/
    //生成deviceId
    setDeviceId(generateDeviceId())
}

const setArticleReadNum = (articleId) => {
    let result = '';
    for (let i = 0; i < 4; i++) {
        result += Math.floor(Math.random() * 10);  // 生成 0-9 的随机数
    }

    const element = document.getElementById(articleId);
    if (isNullOrUndefined(element)) {
        return
    }

    document.getElementById(articleId).innerHTML = result
    /*fetch.get(SERVER_URL + GET_READ_NUM,{articleId: getArticleId()},(data)=>{
        document.getElementById('articleReadNum').innerHTML = data
    })*/
}


