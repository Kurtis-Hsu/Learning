# 安装&配置

## 安装

### yum 安装

```bash
sudo yum install redis -y
```

### 启动 Redis 服务

```bash
sudo systemctl start redis
```

### 设置开机自启

```bash
sudo systemctl enable redis
```

### 检查运行状态

```bash
sudo systemctl status redis
```

如果服务正常运行，输出应显示 `active (running)`

****

## 配置

Redis 配置文件一般位于 `/etc/redis.conf`，通过编辑该文件配置 Redis

```bash
sudo vim /etc/redis/redis.conf
# 若该位置没有配置文件，使用 find 命令查找
sudo find / -name redis.conf
```

### 允许远程访问
默认情况下，Redis 只允许本地访问

1. 打开配置文件，找到以下行并注释掉（在行首添加 `#`）

   ```bash
   bind 127.0.0.1
   ```

   或者将其改为：

   ```bash
   bind 0.0.0.0
   ```

2. 修改 `protected-mode` 配置项

   ```bash
   protected-mode no
   ```

3. 保存并退出编辑器

### 设置密码
为了提高安全性，可以为 Redis 设置密码

1. 打开配置文件，找到以下行并取消注释（删除行首的 `#`），然后将 `foobared` 替换为你的密码

   ```bash
   requirepass yourpassword
   ```

3. 保存并退出编辑器

### 修改其他配置
根据需求，可以修改以下配置：

- **端口**：默认端口为 `6379`，可以通过修改 `port` 配置项更改端口
- **日志文件**：通过 `logfile` 配置项指定日志文件路径
- **数据目录**：通过 `dir` 配置项指定数据存储目录

### 重启 Redis
修改配置文件后，重启 Redis 服务才能使更改生效

```bash
sudo systemctl restart redis
```

****

## 测试

### Redis CLI 连接
通过 Redis 命令行工具连接到 Redis 服务器

```bash
redis-cli
```

如果设置了密码，需要进行认证

```bash
AUTH yourpassword
```

### 测试
在 Redis CLI 中测试

```bash
127.0.0.1:6379> set test "Hello, Redis!"
OK
127.0.0.1:6379> get test
"Hello, Redis!"
```

****

## 防火墙配置

如果启用了防火墙，需要允许 Redis 端口（默认 `6379`）的访问

### 开放端口
```bash
sudo firewall-cmd --zone=public --add-port=6379/tcp --permanent
```

### 重新加载防火墙
```bash
sudo firewall-cmd --reload
```

