const fetch= {
    post: (url,data) => {
        console.log('执行post')
    },

    get: (url,params) => {
        console.log('执行get')
    }
}

fetch.post()
fetch.get()