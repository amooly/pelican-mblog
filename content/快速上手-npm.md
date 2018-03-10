Title: 快速上手 npm
Date: 2017-02-08 23:56
Category: 快速上手
Summary: npm是node的包管理器

## 常见命令

### 安装模块
模块安装分为“局部安装”和“全局安装”。

- 局部安装
局部安装会将模块安装在指定目录（默认当前目录）的`node_modules`中，使用时，需要制定对应的目录。

```shell
# 安装
npm install {module_name}

# 使用
./node_modules/{module_name}/bin/{module_name}.js 
```

- 全局安装
会安装在系统类库中，供全局使用。使用时直接使用命令即可。

```shell
npm install -g {module_name}
```

## 使用镜像加速下载
使用国内的淘宝镜像可以加速npm下载速度。

安装定制的npm：

```shell
npm install -g cnpm --registry=https://registry.npm.taobao.org
```

安装模块：

```shell
cnpm install -g {module_name}
```

## 资料
1.[淘宝 NPM 镜像](https://npm.taobao.org/)


