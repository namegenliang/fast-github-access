import socket
from datetime import datetime
import os

github_domains = [
    'github.githubassets.com',
    'central.github.com',
    'desktop.githubusercontent.com',
    'camo.githubusercontent.com',
    'github.map.fastly.net',
    'github.global.ssl.fastly.net',
    'gist.github.com',
    'github.io',
    'github.com',
    'api.github.com',
    'raw.githubusercontent.com',
    'user-images.githubusercontent.com',
    'favicons.githubusercontent.com',
    'avatars5.githubusercontent.com',
    'avatars4.githubusercontent.com',
    'avatars3.githubusercontent.com',
    'avatars2.githubusercontent.com',
    'avatars1.githubusercontent.com',
    'avatars0.githubusercontent.com',
    'avatars.githubusercontent.com',
    'codeload.github.com',
    'github-cloud.s3.amazonaws.com',
    'github-com.s3.amazonaws.com',
    'github-production-release-asset-2e65be.s3.amazonaws.com',
    'github-production-user-asset-6210df.s3.amazonaws.com',
    'github-production-repository-file-5c1aeb.s3.amazonaws.com',
    'githubstatus.com',
    'github.community',
    'media.githubusercontent.com',
    'objects.githubusercontent.com',
    'raw.github.com',
    'copilot-proxy.githubusercontent.com'
]

def get_ip(domain):
    try:
        return socket.gethostbyname(domain)
    except Exception as e:
        print(f"[ERROR] Failed to resolve {domain}: {e}")
        return None

def generate_hosts():
    hosts = [
        f"# Last update: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n",
        "# 请保存https://namegenliang.github.io/fast-github-access/hosts/github-hosts.txt\n"
        "# 请保存https://namegenliang.github.io/fast-github-access/hosts/github-hosts.txt\n"
        "# 请保存https://namegenliang.github.io/fast-github-access/hosts/github-hosts.txt\n"
    ]
    for domain in github_domains:
        ip = get_ip(domain)
        if ip:
            hosts.append(f"{ip}\t{domain}\n")

    # 添加尾注
    hosts.append("\n# 自动更新说明：\n")
    hosts.append("# 本文件由 GitHub Actions 自动生成\n")
    hosts.append("# 项目地址：https://github.com/namegenliang/fast-github-access\n")
    hosts.append("# 每 2 小时自动更新一次，如有问题请namegenliang@gmail.com\n")
    return ''.join(hosts)

def write_hosts_file():
    os.makedirs('hosts', exist_ok=True)
    with open('hosts/github-hosts.txt', 'w', encoding='utf-8') as f:
        f.write(generate_hosts())

if __name__ == '__main__':
    write_hosts_file()
