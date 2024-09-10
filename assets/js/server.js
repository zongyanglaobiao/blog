const fetch = {
    post: async (url,data,call) => {
        const response = await window.fetch(url, {
            method: 'POST', // 请求方法为POST
            headers: {
                'Content-Type': 'application/json', // 请求的内容类型为JSON
            },
            body: JSON.stringify(data), // 将JavaScript对象转为JSON字符串
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
        const fullUrl = `${url}?${queryString}`; // 拼接完整的URL

        const response = await window.fetch(fullUrl, {
            method: 'GET', // 请求方法为GET
        });

        // 检查请求是否成功
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // 将返回的数据转为JSON格式
        const result = await response.json();
        call(result)
    }
}

const SERVER_URL = 'http://localhost:8080'
const SAVE_ARTICLE = '/save/article';

// 获取博客正文中的ID
const articleId = document.querySelector('.article-content').getAttribute('data-article-id');

