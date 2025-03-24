# 安装&配置

## 安装

### yum 安装

默认情况下，CentOS/RHEL 的官方仓库可能不包含最新版本的 PostgreSQL，须要添加 PostgreSQL 官方仓库以获取最新版本

1. 安装 PostgreSQL 官方仓库 RPM 包

   ```bash
   sudo yum install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-9-x86_64/pgdg-redhat-repo-latest.noarch.rpm
   ```

   > **PS**：地址中的 `EL-9` 对应的是系统版本，如果系统是 CentOS/RHEL 7，须要替换为`EL-7`

2. 更新仓库缓存

   ```bash
   sudo yum makecache
   ```

安装 PostgreSQL 服务器和客户端

```bash
sudo yum install -y postgresql12-server
```

> **PS**：`postgresql12-server` 中的 `12` 是 PostgreSQL 的版本号，12这个版本较稳定

### 初始化
安装完成后，初始化 PostgreSQL

```bash
sudo /usr/pgsql-12/bin/postgresql-12-setup initdb
```

> **注意**：路径中的 `12` 是 PostgreSQL 的版本号，请根据实际安装的版本调整

### 启动 PostgreSQL 服务
```bash
sudo systemctl start postgresql-12
```

### 设置开机自启
```bash
sudo systemctl enable postgresql-12
```

### 检查运行状态
```bash
sudo systemctl status postgresql-12
```

如果服务正常运行，输出应显示 `active (running)`

---

## 配置

PostgreSQL 的配置文件一般位于 `/var/lib/pgsql/12/data/postgresql.conf`，通过编辑该文件配置 PostgreSQL

```bash
sudo vim /var/lib/pgsql/12/data/postgresql.conf
# 若该位置没有配置文件，使用 find 命令查找
sudo find / -name postgresql.conf
```

### 允许远程访问

默认情况下，PostgreSQL 只允许本地访问

1. 打开配置文件，修改 `listen_addresses` 配置项

   ```bash
   listen_addresses = '*'
   ```

2. 保存并退出编辑器

修改访问控制

1. 打开 `pg_hba.conf` 文件

   ```bash
   sudo vim /var/lib/pgsql/12/data/pg_hba.conf
   ```

2. 添加或修改以下行以允许远程访问

   ```bash
   # 允许所有 IP 通过密码访问
   host    all             all             0.0.0.0/0               md5
   ```

3. 保存并退出编辑器

### 重启 PostgreSQL

修改配置文件后，重启 PostgreSQL 服务才能使更改生效

```bash
sudo systemctl restart postgresql-12
```

---

## 设置用户和数据库

### 切换到 PostgreSQL 用户
PostgreSQL 安装后会自动创建一个名为 `postgres` 的系统用户，切换到该用户

```bash
sudo -i -u postgres
```

### 创建新用户
使用 `createuser` 命令创建新用户

```bash
createuser --interactive
```

按照提示输入用户名并选择角色（如超级用户）

### 创建新数据库
使用 `createdb` 命令创建新数据库

```bash
createdb mydatabase
```

### 设置用户密码
使用 `psql` 命令设置用户密码：

```bash
psql -c "ALTER USER myuser WITH PASSWORD 'mypassword';"
```

---

## 测试

### psql 连接
```bash
# 这里的 myuser 使用系统用户，一般为 postgres
psql -U myuser -d mydatabase
```

### 测试
在 `psql` 中测试

```sql
CREATE TABLE test (id SERIAL PRIMARY KEY, name VARCHAR(50));
INSERT INTO test (name) VALUES ('Hello, PostgreSQL!');
SELECT * FROM test;
```

---

## 防火墙配置
如果启用了防火墙，需要允许 PostgreSQL 端口（默认 `5432`）的访问

### 开放端口

由于 `postgres` 用户没有权限，需要使用 `su` 命令回到 `root` 用户才能继续操作

```bash
sudo firewall-cmd --zone=public --add-port=5432/tcp --permanent
```

### 重新加载防火墙
```bash
sudo firewall-cmd --reload
```

## 扩展

```bash
sudo yum install postgresql12-contrib
```

