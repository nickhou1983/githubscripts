import csv
import requests

# GitHub 组织名称和访问令牌
GITHUB_ORG = "your-organization-name"  # 替换为你的组织名称
GITHUB_TOKEN = "your-personal-access-token"  # 替换为你的 GitHub 个人访问令牌

# GitHub API URL
GITHUB_API_URL = f"https://api.github.com/orgs/{GITHUB_ORG}/invitations"

def invite_members(csv_file):
    """
    从 CSV 文件中读取用户信息，并通过 GitHub API 发送邀请。
    :param csv_file: 包含用户信息的 CSV 文件路径
    """
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            username = row.get("username")
            email = row.get("email")
            if username and email:
                send_invitation(username, email)

def send_invitation(username, email):
    """
    通过 GitHub API 发送邀请。
    :param username: 用户名
    :param email: 用户邮箱
    """
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }
    data = {
        "email": email,
        "role": "direct_member"  # 可选值: direct_member, admin
    }
    response = requests.post(GITHUB_API_URL, headers=headers, json=data)
    if response.status_code == 201:
        print(f"成功邀请用户 {username} ({email}) 加入组织。")
    else:
        print(f"邀请用户 {username} ({email}) 失败: {response.status_code} - {response.json()}")

if __name__ == "__main__":
    # 替换为你的 CSV 文件路径
    csv_file_path = "user.csv"
    invite_members(csv_file_path)