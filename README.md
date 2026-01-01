# arXiv Daily Digest 📚

[English](#english) | [日本語](#japanese)

---

<a name="english"></a>
## English

Automatically fetch and digest new papers from arXiv.org in your areas of interest every day.

### Features

- 🔍 **Automated Fetching**: Automatically retrieves papers from specified arXiv categories
- 📅 **Daily Updates**: Runs daily via GitHub Actions
- 🔄 **Manual Updates**: Trigger updates manually from the web interface
- 📊 **Organized Digests**: Papers are grouped by category in clean Markdown format
- 🌐 **Web UI**: Beautiful, responsive web interface to browse and search papers
- ⚡ **High Performance**: Indexed data structure with lazy loading for fast page loads
- 🔎 **Advanced Search**: Filter by category, date, and search through titles, authors, and summaries
- ⚙️ **Customizable**: Easy configuration of research categories
- 🚀 **No External Dependencies**: Uses only Python standard library

### Quick Start

1. **Fork this repository**

2. **Customize your interests**

   Edit `config.json` to specify your research categories:
   ```json
   {
     "categories": [
       "cs.AI",
       "cs.LG",
       "cs.CL"
     ],
     "max_results": 50,
     "lookback_days": 1
   }
   ```

3. **Available Categories**

   Common arXiv categories:
   - `cs.AI` - Artificial Intelligence
   - `cs.LG` - Machine Learning
   - `cs.CL` - Computation and Language (NLP)
   - `cs.CV` - Computer Vision
   - `cs.NE` - Neural and Evolutionary Computing
   - `cs.RO` - Robotics
   - `stat.ML` - Machine Learning (Statistics)
   - `math.OC` - Optimization and Control
   - `quant-ph` - Quantum Physics

   See [arXiv category taxonomy](https://arxiv.org/category_taxonomy) for all categories.

4. **Run manually or wait for daily automation**

   Manual run:
   ```bash
   python fetch_arxiv.py
   ```

   GitHub Actions will automatically run daily at 9:00 AM UTC (6:00 PM JST).

### How It Works

1. **Fetch**: Retrieves papers from arXiv API based on configured categories
2. **Filter**: Filters papers published within the specified lookback period
3. **Generate**: Creates a formatted Markdown digest
4. **Save**: Stores digests in the `digests/` directory
5. **Commit**: (GitHub Actions) Automatically commits and pushes new digests

### Output Format

Digests are saved in `digests/arxiv_digest_YYYY-MM-DD.md` with the following structure:

```markdown
# arXiv Daily Digest - 2024-01-01

Total papers: 25

---

## cs.AI

**10 papers**

### 1. Paper Title Here

**Authors:** Author One, Author Two, et al.

**Published:** 2024-01-01

🔗 [Paper](https://arxiv.org/abs/2401.00001) | 📄 [PDF](https://arxiv.org/pdf/2401.00001)

**Summary:** Paper summary...

---
```

### Configuration Options

- `categories`: List of arXiv categories to monitor
- `max_results`: Maximum number of papers to fetch per category (default: 50)
- `lookback_days`: How many days back to fetch papers (default: 1)

### Local Development

```bash
# Clone the repository
git clone https://github.com/yourusername/My-arxiv.git
cd My-arxiv

# Run the script
python fetch_arxiv.py

# Check the generated digest
ls digests/
```

### GitHub Actions

The workflow is configured to run daily at 9:00 AM UTC. You can also:
- Manually trigger the workflow from the Actions tab
- Adjust the schedule in `.github/workflows/daily-digest.yml`

### Web UI

A responsive web interface is available to browse and search papers:

1. **Enable GitHub Pages (One-time setup)**
   - Go to your repository Settings → Pages
   - Set Source to "GitHub Actions"
   - Save and wait a few minutes
   - The site will automatically deploy when new papers are fetched or when changes are pushed to the `pages/` folder

2. **Access the UI**
   - Visit: `https://yourusername.github.io/My-arxiv/`
   - The UI will display all your collected papers
   - Updates automatically when new digests are generated

3. **Features**
   - 🔍 **Search**: Search across titles, authors, and summaries
   - 🏷️ **Category Filter**: Click category tags to filter papers
   - 📅 **Date Filter**: Select specific dates to view
   - 📊 **Sorting**: Sort by date or title
   - 🔄 **Manual Update**: Trigger GitHub Actions workflow to fetch latest papers
   - ♻️ **Page Reload**: Refresh the page to load newly updated data
   - ⚡ **Fast Loading**: Indexed data structure with lazy loading
     - Initial load: Only 12 KB index file (vs 7.4 MB previously)
     - Date-specific data loaded on demand (~117 KB per day)
     - Cached in memory for instant subsequent access
   - 📱 **Responsive**: Works perfectly on mobile, tablet, and desktop

4. **Local Testing**
   ```bash
   # Generate JSON data
   python generate_json.py

   # Start local server
   cd pages
   python -m http.server 8000

   # Visit http://localhost:8000 in your browser
   ```

### License

MIT License - Feel free to use and modify!

---

<a name="japanese"></a>
## 日本語

arXiv.orgから興味のある分野の新しい論文を毎日自動で取得してダイジェストを作成します。

### 特徴

- 🔍 **自動取得**: 指定したarXivカテゴリから論文を自動取得
- 📅 **毎日更新**: GitHub Actionsで毎日自動実行
- 🔄 **手動更新**: Webインターフェースから手動で更新をトリガー
- 📊 **整理されたダイジェスト**: カテゴリ別に整理された見やすいMarkdown形式
- 🌐 **Web UI**: 美しいレスポンシブWebインターフェースで論文を閲覧・検索
- ⚡ **高速**: インデックス化されたデータ構造と遅延読み込みで高速なページ読み込み
- 🔎 **高度な検索**: カテゴリ、日付でフィルタリング、タイトル・著者・要約を検索
- ⚙️ **カスタマイズ可能**: 研究カテゴリを簡単に設定可能
- 🚀 **依存関係なし**: Python標準ライブラリのみ使用

### クイックスタート

1. **このリポジトリをフォーク**

2. **興味のある分野をカスタマイズ**

   `config.json`を編集して研究カテゴリを指定:
   ```json
   {
     "categories": [
       "cs.AI",
       "cs.LG",
       "cs.CL"
     ],
     "max_results": 50,
     "lookback_days": 1
   }
   ```

3. **利用可能なカテゴリ**

   主要なarXivカテゴリ:
   - `cs.AI` - 人工知能
   - `cs.LG` - 機械学習
   - `cs.CL` - 計算と言語（自然言語処理）
   - `cs.CV` - コンピュータビジョン
   - `cs.NE` - ニューラルネットワークと進化計算
   - `cs.RO` - ロボティクス
   - `stat.ML` - 機械学習（統計）
   - `math.OC` - 最適化と制御
   - `quant-ph` - 量子物理学

   全カテゴリは[arXivカテゴリ分類](https://arxiv.org/category_taxonomy)を参照。

4. **手動実行または自動実行を待つ**

   手動実行:
   ```bash
   python fetch_arxiv.py
   ```

   GitHub Actionsが毎日午前9時（UTC）/ 午後6時（JST）に自動実行します。

### 動作の仕組み

1. **取得**: 設定されたカテゴリに基づいてarXiv APIから論文を取得
2. **フィルタ**: 指定された期間内に公開された論文を絞り込み
3. **生成**: フォーマットされたMarkdownダイジェストを作成
4. **保存**: `digests/`ディレクトリにダイジェストを保存
5. **コミット**: （GitHub Actions）新しいダイジェストを自動的にコミット＆プッシュ

### 出力形式

ダイジェストは`digests/arxiv_digest_YYYY-MM-DD.md`に以下の形式で保存されます：

```markdown
# arXiv Daily Digest - 2024-01-01

Total papers: 25

---

## cs.AI

**10 papers**

### 1. 論文タイトル

**Authors:** 著者1, 著者2, et al.

**Published:** 2024-01-01

🔗 [Paper](https://arxiv.org/abs/2401.00001) | 📄 [PDF](https://arxiv.org/pdf/2401.00001)

**Summary:** 論文の要約...

---
```

### 設定オプション

- `categories`: 監視するarXivカテゴリのリスト
- `max_results`: カテゴリごとに取得する論文の最大数（デフォルト: 50）
- `lookback_days`: 何日前まで遡って論文を取得するか（デフォルト: 1）

### ローカル開発

```bash
# リポジトリをクローン
git clone https://github.com/yourusername/My-arxiv.git
cd My-arxiv

# スクリプトを実行
python fetch_arxiv.py

# 生成されたダイジェストを確認
ls digests/
```

### GitHub Actions

ワークフローは毎日午前9時（UTC）に実行されるよう設定されています。また以下も可能です：
- Actionsタブから手動でワークフローをトリガー
- `.github/workflows/daily-digest.yml`でスケジュールを調整

### Web UI

論文を閲覧・検索できるレスポンシブWebインターフェースが利用できます：

1. **GitHub Pagesを有効化（初回のみ）**
   - リポジトリの Settings → Pages へ移動
   - Source を "GitHub Actions" に設定
   - 保存して数分待機
   - 新しい論文が取得されたとき、または `pages/` フォルダに変更がプッシュされたときに自動的にデプロイされます

2. **UIにアクセス**
   - `https://yourusername.github.io/My-arxiv/` にアクセス
   - 収集した全ての論文が表示されます
   - 新しいダイジェストが生成されると自動的に更新されます

3. **機能**
   - 🔍 **検索**: タイトル、著者、要約を横断検索
   - 🏷️ **カテゴリフィルター**: カテゴリタグをクリックして絞り込み
   - 📅 **日付フィルター**: 特定の日付を選択して表示
   - 📊 **ソート**: 日付やタイトルで並び替え
   - 🔄 **手動更新**: GitHub Actionsワークフローをトリガーして最新の論文を取得
   - ♻️ **ページ再読み込み**: ページを更新して新しく更新されたデータを読み込み
   - ⚡ **高速読み込み**: インデックス化されたデータ構造と遅延読み込み
     - 初期読み込み: わずか12KBのインデックスファイル（以前は7.4MB）
     - 日付別データをオンデマンドで読み込み（1日あたり約117KB）
     - メモリにキャッシュして即座にアクセス
   - 📱 **レスポンシブ**: スマートフォン、タブレット、PCで完璧に動作

4. **ローカルでのテスト**
   ```bash
   # JSONデータを生成
   python generate_json.py

   # ローカルサーバーを起動
   cd pages
   python -m http.server 8000

   # ブラウザで http://localhost:8000 にアクセス
   ```

### ライセンス

MITライセンス - 自由に使用・改変してください！
