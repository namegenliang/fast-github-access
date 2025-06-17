# 🚀 Fast GitHub Access

解决国内访问 GitHub 慢的问题，自动生成 `hosts` 文件，支持每 2 小时自动更新。

保存地址 防止失联

```https://namegenliang.github.io/fast-github-access/hosts/github-hosts.txt```

## 🛠 功能

- 自动获取 GitHub 相关域名 IP
- 每 2 小时 GitHub Actions 自动更新并提交[hosts.txt](./hosts/github-hosts.txt)
- 你可以直接复制其内容，粘贴到系统的 hosts 文件中以加速访问 GitHub。
- `直接也可手动执行脚本生成最新 hosts`

## 📦 使用方法

### 1. 获取最新 hosts 内容

克隆仓库并运行：

```bash
git clone https://github.com/namegenliang/fast-github-access.git
cd fast-github-access
python scripts/update_hosts.py
```

生成的文件：`hosts/github-hosts.txt`

### 2. 替换系统 hosts（需管理员权限）

将 `github-hosts.txt` 内容追加到系统 hosts 文件：

- Windows: `C:\Windows\System32\drivers\etc\hosts`
- macOS / Linux: `/etc/hosts`

### 3. 自动更新说明

仓库已配置 GitHub Actions，每 2 小时自动更新解析 IP 并推送。

---

## 🔑 LICENSE

MIT License
