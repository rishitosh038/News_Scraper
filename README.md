# 📰 News Headlines Web Scraper

## 📌 Objective
Automate the process of collecting top headlines from a public news website using Python.

## Tools Used
- Python
- [requests](https://pypi.org/project/requests/)
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)

## Project Structure

## How It Works
1. The script sends an HTTP request to a news website (e.g., BBC News).
2. It parses the HTML content using BeautifulSoup.
3. It extracts headlines from `<h2>` (or relevant) tags.
4. It writes the headlines into a `.txt` file.

## Setup Instructions

### 1. Clone this Repository
```bash
git clone https://github.com/yourusername/news-headline-scraper.git
cd news-headline-scraper
