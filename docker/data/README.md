# Data Directory

[English](#english) | [中文](#中文) | [日本語](#日本語)

---

## English

Place your AI conversation export files in this directory. They will be automatically mounted into the Docker container.

### ChatGPT

1. Settings → Data controls → Export data
2. Unzip to get `conversations.json`
3. Place it in `data/ChatGPT/`

```bash
docker compose exec riverhistory bash -c "cd /app_work && python import_data.py --chatgpt data/ChatGPT/conversations.json"
```

### Claude

1. Settings → Account → Export Data
2. Unzip to get `conversations.json`
3. Place it in `data/Claude/`

```bash
docker compose exec riverhistory bash -c "cd /app_work && python import_data.py --claude data/Claude/conversations.json"
```

### Gemini

1. [Google Takeout](https://takeout.google.com/) → Select "Gemini Apps" → Download
2. Unzip to get the `Gemini Apps` folder (contains `My Activity.html`) or JSON file
3. Place it in `data/Gemini/`

```bash
docker compose exec riverhistory bash -c "cd /app_work && python import_data.py --gemini 'data/Gemini/My Activity.html'"
```

### Process

After importing, run the River Algorithm to extract profiles:

```bash
docker compose exec riverhistory bash -c "cd /app_work && python run.py all max"
```

### Notes

- You don't need all three — import whichever platforms you use
- Duplicate entries are skipped automatically (checksum-based)

---

## 中文

将 AI 对话导出文件放在此目录下，会自动挂载到 Docker 容器中。

### ChatGPT

1. Settings → Data controls → Export data
2. 解压，得到 `conversations.json`
3. 放到 `data/ChatGPT/` 下

```bash
docker compose exec riverhistory bash -c "cd /app_work && python import_data.py --chatgpt data/ChatGPT/conversations.json"
```

### Claude

1. Settings → Account → Export Data
2. 解压，得到 `conversations.json`
3. 放到 `data/Claude/` 下

```bash
docker compose exec riverhistory bash -c "cd /app_work && python import_data.py --claude data/Claude/conversations.json"
```

### Gemini

1. [Google Takeout](https://takeout.google.com/) → 选择 "Gemini Apps" → 下载
2. 解压，得到 `Gemini Apps` 文件夹（里面有 `我的活动记录.html`）或 JSON 文件
3. 放到 `data/Gemini/` 下

```bash
docker compose exec riverhistory bash -c "cd /app_work && python import_data.py --gemini 'data/Gemini/我的活动记录.html'"
```

### 处理

导入后，运行河流算法提取画像：

```bash
docker compose exec riverhistory bash -c "cd /app_work && python run.py all max"
```

### 说明

- 不需要三个平台都导入，导入你用过的就行
- 重复数据会自动跳过（基于 checksum 去重）

---

## 日本語

AI の会話エクスポートファイルをこのディレクトリに配置してください。Docker コンテナに自動的にマウントされます。

### ChatGPT

1. Settings → Data controls → Export data
2. 解凍して `conversations.json` を取得
3. `data/ChatGPT/` に配置

```bash
docker compose exec riverhistory bash -c "cd /app_work && python import_data.py --chatgpt data/ChatGPT/conversations.json"
```

### Claude

1. Settings → Account → Export Data
2. 解凍して `conversations.json` を取得
3. `data/Claude/` に配置

```bash
docker compose exec riverhistory bash -c "cd /app_work && python import_data.py --claude data/Claude/conversations.json"
```

### Gemini

1. [Google Takeout](https://takeout.google.com/) → "Gemini Apps" を選択 → ダウンロード
2. 解凍して `Gemini Apps` フォルダ（`マイ アクティビティ.html` を含む）または JSON ファイルを取得
3. `data/Gemini/` に配置

```bash
docker compose exec riverhistory bash -c "cd /app_work && python import_data.py --gemini 'data/Gemini/マイ アクティビティ.html'"
```

### 処理

インポート後、River Algorithm を実行してプロフィールを抽出：

```bash
docker compose exec riverhistory bash -c "cd /app_work && python run.py all max"
```

### 注意事項

- 3 つすべてのプラットフォームをインポートする必要はありません。使用しているものだけで構いません
- 重複データはチェックサムにより自動的にスキップされます
