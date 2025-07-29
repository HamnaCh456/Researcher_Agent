## Project: Researcher Agent

### Description

**Researcher Agent** is an intelligent Streamlit-based AI assistant that performs real-time research on any given topic using web search and content scraping tools. It uses the **Groq LLM** (LLaMA3) to:

1. Search the web for the topic using a custom search tool.
2. Scrape content from found URLs using a scraper tool.
3. Generate a short, coherent report **based only on the scraped content**.

### Demo
watch the demo [here](https://youtu.be/4kUbIkC-Sbk)

## How to Run

### Prerequisites

* Python 3.8+
* API key for [Groq](https://console.groq.com/)
* Installed dependencies:

  * `streamlit`
  * `groq`
  * `firecrawl`
  * `seper API`

### Installation

1. Clone this repository or copy the files into a folder:

   ```bash
   git clone https://HamnaCh456/Researcher_Agent.git
   
2. Install required packages:

   ```bash
   pip install -r requirements.txt
   ```
3. Add your Groq API key in the script or use environment variables.

---

### Run the App

```bash
streamlit run your_script_name.py
```
---

## Example Usage

* Enter a topic like: `latest AI tools`, or `quantum computing applications`.
* The agent will:

  * Search the web for this topic.
  * Scrape relevant pages.
  * Generate a short, factual report.

---

## File Structure

```
├── researcher_app.py        # Main Streamlit app (your current script)
├── tools.py                 # Contains `searcher` and `scraper` functions
├── README.md                # This file
└── requirements.txt         # Python dependencies
```

---

## Features

* Uses Groq’s LLaMA3 model for generation
* Utilizes structured tool calling with search & scrape functions
* Produces factual, real-world responses from scraped content
* Easy web interface with Streamlit

