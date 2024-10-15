---
title: React中身份失效跳转登录页面
description: React中如何感知用户身份失效并跳转到登录页
# 默认url路径是title如果不写slug
slug: React中身份失效跳转登录页面
date: 2024-09-25 09:10:34+0000
toc: true
categories:
  - frontend-category
tags:
  - react
keywords:
  - react
  - 前端
id: d90535fa-3c23-406b-bf9c-5f74baf50038
---

在写React项目的时候在登录这块对于用户身份失效自动跳到登录页这块让我头大，问题在于：我们只知道请求为401的时候才会跳到登录页让用户身份认证，因为不可能在每个请求都要判断一下是否为401于是我们就会在封装axios的地方单独判断**是否为401**，此时问题就出来了如何在请求判断为401时通知组件更新，于是我就通过**redux**来通知因为我们知道redux既可以在**组件中使用**也可以在**js文件中使用**，废话不多说下面就是我的代码，[点击我查看完整代码](https://github.com/zongyanglaobiao/ledger/tree/2e5283eaba752efc69fa3d328e09800c5285678c)

## 第一步

判断是否请求为401,当请求为401时移除已存在的token并且使用redux的action更新store

**http.request.js**

```js
import axios from "axios";
import {store} from "@/redux/store.js";
import {authorizeAction} from "@/redux/feature/authorize.js";
import {getToken, getTokenName, removeToken} from "@/lib/toolkit/local.storage.js";

const URL = import.meta.env.VITE_REACT_APP_PATH

// 创建 axios 请求实例
const serviceAxios = axios.create({
	baseURL:URL, // 基础请求地址
	timeout: 10000, // 请求超时设置
	withCredentials: false, // 跨域请求是否需要携带 cookie
});

// 创建请求拦截
serviceAxios.interceptors.request.use(
	(config) => {
		config.headers = {'Content-Type': 'application/json',...config.headers,[getTokenName()]:getToken()};
		return config;
	},
	(error) => {
		return Promise.reject(error);
	}
);


// 创建响应拦截
serviceAxios.interceptors.response.use(
	(res) => {
		if (res.data.code === 401) {
			//移除之前的token
			removeToken()
			store.dispatch(authorizeAction())
		}
		return res.data;
	},
	(error) => {
		let msg = "网络异常问题，请联系管理员！";
		if (error && error.response) {
			switch (error.response.status) {
				case 302:
					msg = "接口重定向了！";
					break;
				case 400:
					msg = "参数不正确！";
					break;
				case 401:
					msg = "您未登录，或者登录已经超时，请先登录！";
					break;
				case 403:
					msg = "您没有权限操作！";
					break;
				case 404:
					msg = `请求地址出错: ${error.response.config.url}`;
					break;
				case 408:
					msg = "请求超时！";
					break;
				case 409:
					msg = "系统已存在相同数据！";
					break;
				case 500:
					msg = "服务器内部错误！";
					break;
				case 501:
					msg = "服务未实现！";
					break;
				case 502:
					msg = "网关错误！";
					break;
				case 503:
					msg = "服务不可用！";
					break;
				case 504:
					msg = "服务暂时无法访问，请稍后再试！";
					break;
				case 505:
					msg = "HTTP 版本不受支持！";
					break;
				default:
					msg = "异常问题，请联系管理员！";
					break;
			}
		}
		return Promise.reject(msg);
	}
);

const request = {
	post:(url,data = {}) => {
		return serviceAxios({
			url: url,
			method: "post",
			data: data,
			headers: {
				"Content-Type": "application/json"
			}
		})
	},
	get:(url,params = {})=>{
		return serviceAxios({
			url: url,
			method: "get",
			params: params,
			headers: {
				"Content-Type": "application/json"
			}
		})
	}
}



export {URL}

export default request;

```

**store.js: devTools用于浏览器插件，middleware：这是一个配置选项，默认情况下，Redux Toolkit 会检查每个动作和状态是否可序列化（即能被 JSON.stringify 处理），以确保 Redux 状态树的一致性和可预测性。在某些情况下（如使用某些类型的非序列化数据），可能需要关闭此检查**

```js
import {configureStore} from "@reduxjs/toolkit";
import {composeWithDevTools} from "@redux-devtools/extension";
import {authorizeReducer} from "@/redux/feature/authorize.js";

//存储状态
export const store = configureStore({
	reducer:{
		authorize:authorizeReducer
	},
	devTools:composeWithDevTools(),
	middleware : (getDefaultMiddleware) => {
		return getDefaultMiddleware({
			serializableCheck: false
		})
	}
});
```

**authorize.js**

```js
import {isBlank} from "@/lib/toolkit/util.js";
import {generateSlice} from "@/lib/toolkit/redux.util.js";
import {getToken} from "@/lib/toolkit/local.storage.js";

const AUTHORIZE_SUCCESS = true;
const AUTHORIZE_FAIL = false;

/**
 *  用于监控TOKEN失效的state
 *  false 授权异常 true 授权正常
 */
const authorizeProcessor = generateSlice(getRandomId(), {hasAuthorize: AUTHORIZE_FAIL}, {
    authorizeAction() {
        return {hasAuthorize:isBlank(getToken()) ? AUTHORIZE_FAIL : AUTHORIZE_SUCCESS}
    },
});
const authorizeProcessor = createSlice({
		name:'login',
		initialState:AUTHORIZE_FAIL,
		reducers:{
            authorizeAction: ()=>{
                return isBlank(getToken()) ? AUTHORIZE_FAIL : AUTHORIZE_SUCCESS
            }
        }
	})

export const authorizeReducer = authorizeProcessor.reducer
export const {authorizeAction} = authorizeProcessor.actions
export {AUTHORIZE_FAIL,AUTHORIZE_SUCCESS}
```

## 第二步

通知组件更新：封装HOOK放在顶层组件中，

**main.jsx**

```js
import '@/index.css'
import 'virtual:uno.css'
import ReactDOM from 'react-dom/client';
import {RouterProvider} from "react-router-dom";
import {Suspense} from "react";
import {Loading} from "antd-mobile";
import {Provider} from "react-redux";
import router from "@/router/index.jsx";
import {store} from "@/redux/store.js";

//渲染
ReactDOM.createRoot(document.getElementById('root')).render(
    <Suspense fallback={<Loading/>} >
        <Provider store={store}>
            <RouterProvider router={router}/>
        </Provider>
    </Suspense>
)

```

**App.jsx**

```js
import {useEffect} from "react";
import {Outlet, useNavigate} from "react-router-dom";
import {AUTH_PATH, HOME_PATH} from "@/router/index.jsx";
import {useToken} from "@/hook/useToken.jsx";


export default function App() {
    const navigate = useNavigate();
    const {isLogin} = useToken();

    useEffect(() => {
        if (isLogin) {
            navigate(HOME_PATH)
            return
        }
        navigate(AUTH_PATH)
    },[isLogin])
    return (
        <div className='w-full h-full'>
            <Outlet/>
        </div>
    )
}
```

**useToken.jsx：当redux更新了此hook就会被触发并且其中的isLogin会重新计算相当于响应式数据，至于为什么要增加`!isBlank(getToken())`,就在于每次关闭重新打开我们的网站redux都会初始化，导致用户可能是有token也会被重定向到登录页，所以判断的时候还需要加上token是否存在**

```js
import {useDispatch, useSelector} from "react-redux";
import {getToken, removeToken, setToken} from "@/lib/toolkit/local.storage.js";
import {isBlank} from "@/lib/toolkit/util.js";
import {authorizeAction} from "@/redux/feature/authorize.js";

export const useToken = () => {
    const {hasAuthorize} = useSelector(state => state.authorize);
    const dispatch = useDispatch();
    return {
        isLogin: hasAuthorize || !isBlank(getToken()),
        token: getToken(),
        logout: () => {
            removeToken();
            dispatch(authorizeAction())
        },
        login: (token) => {
            setToken(token)
            dispatch(authorizeAction())
        }
    }
}
```

**以上的代码就解决开头提出的问题，但是其中有很多工具类啥的代码不完整，[点击我查看完整代码](https://github.com/zongyanglaobiao/ledger/tree/2e5283eaba752efc69fa3d328e09800c5285678c)**

## 工具类

**local.storage.js**：isBlank为工具类的一个方法，其中的`const TOKEN_NAME = import.meta.env.VITE_REACT_APP_TOKEN_NAME`语法是来自于`dotenv-cli`这个依赖包的可以自行Google查看用法，在这里就是获取存在浏览器token的key

```js
import {isBlank} from "@/lib/toolkit/util.js";

const TOKEN_NAME = import.meta.env.VITE_REACT_APP_TOKEN_NAME

const getTokenName = () => {
    if (isBlank(TOKEN_NAME)) {
        throw new Error('TOKEN_NAME is null or undefined')
    }
    return TOKEN_NAME
}

const getToken = () => {
    return localStorage.getItem(getTokenName()) || ''
}

const setToken = (token) => {
    localStorage.setItem(getTokenName(), token)
}

const removeToken = () => {
    localStorage.removeItem(getTokenName())
}

const get = (key) => {
    return localStorage.getItem(key);
}

const set = (key,value) => {
    localStorage.setItem(key,value)
}

const remove = (key) => {
    localStorage.removeItem(key)
}

export {getTokenName, getToken, setToken, removeToken, get, set, remove}
```

以上只是我自己想的如果有更好的解决方法，愿意请教。谢谢

