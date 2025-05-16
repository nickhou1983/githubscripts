# githubscripts

# 这个脚本用于批量邀请用户加入组织

## 功能说明

`invite-members.py` 是一个用于批量邀请用户加入 GitHub 组织的脚本。它通过读取一个包含用户信息的 CSV 文件（如 `user.csv`），并使用 GitHub API 自动向用户发送邀请。

### CSV 文件格式
CSV 文件应包含以下两列：
- `username`: 用户名
- `email`: 用户邮箱

示例文件内容：
```csv
username,email
user1,example1@example.com
user2,example2@example.com
```


## 如何运行 `invite-members.py` 脚本

### 前置条件
1. **安装 Python**:
   - 确保已安装 Python 3。
   - 如果未安装，请访问 [Python 官方网站](https://www.python.org/) 下载并安装。

2. **安装依赖库**:
   - 在终端中运行以下命令安装 `requests` 库：
     ```bash
     pip3 install requests
     ```

3. **准备 CSV 文件**:
   - 创建一个名为 `user.csv` 的文件，内容格式如下：
     ```csv
     username,email
     user1,example1@example.com
     user2,example2@example.com
     ```

### 配置脚本
1. 打开 `invite-members.py` 文件。
2. 替换以下变量为你的 GitHub 组织名称和个人访问令牌：
   ```python
   GITHUB_ORG = "your-organization-name"  # 替换为你的组织名称
   GITHUB_TOKEN = "your-personal-access-token"  # 替换为你的 GitHub 个人访问令牌
    ```
### 根据这个文档生成GITHUB_TOKEN
https://docs.github.com/zh/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#%E5%88%9B%E5%BB%BA-personal-access-token-classic


