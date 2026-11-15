# 🚀 Web Scraping & API Fundamentals

Welcome! If you are new to Data Engineering or Data Analysis, extracting data from the internet is one of the most important skills you can learn. 

This repository is designed to take you from a complete beginner to someone who understands exactly how to pull data from websites and web services using Python.

---

## 📖 What is this project about?

When we need data from the internet, we generally have two ways to get it:
1. **Web Scraping**: Writing code to read the visual "HTML" of a website (just like your browser does) and extracting the text we want. We use this when a website doesn't offer a direct way to download their data.
2. **API (Application Programming Interface)**: Communicating directly with the server's database using structured commands. This is much faster and cleaner, but requires the website to have an API built for public use.

This repository covers both methods in **8 detailed steps**.

---

## 🎯 What You Will Learn (The 8 Steps)

### Phase 1: Web Scraping (Extracting Data from Websites)

#### Step 1: The Core Concepts
We start by understanding the fundamental difference between Scraping and APIs. You will learn when to use which method, and the ethics behind scraping data from public websites.

#### Step 2: HTML Structure (The Skeleton of a Website)
Before we can scrape a website, we must understand how it is built. You will learn about **HTML**:
- **Tags**: The building blocks (like `<div>`, `<h1>`, `<p>`).
- **Attributes**: The labels given to tags (like `id="title"` or `class="price"`). 
*Why is this important? Because our scraper will look for specific `id` and `class` names to find the exact data we want!*

#### Step 3: Understanding the DOM Tree
HTML isn't just a list; it's a family tree called the **DOM (Document Object Model)**. You will learn how elements relate to each other:
- **Parent**: The container holding other elements.
- **Child**: The element inside the container.
- **Sibling**: Elements sitting next to each other.
*Understanding this allows us to tell our scraper: "Find the title, and then grab the price sitting next to it (its sibling)."*

#### Step 4: Static Scraping with BeautifulSoup
We put theory into practice! Using a library called **BeautifulSoup**, we will extract job postings from a static website (Hacker News). You will see how just a few lines of Python can download hundreds of job titles instantly.

#### Step 5: Dynamic Scraping with Selenium
What happens if a website uses heavy animations and JavaScript (like infinite scrolling)? BeautifulSoup will fail because the data isn't in the raw HTML. 
Enter **Selenium**: A virtual "robot browser" that can open a webpage, type in search boxes, click buttons, and scroll down, exactly like a human!

---

### Phase 2: Application Programming Interfaces (APIs)

#### Step 6: API Concepts
Imagine you are at a restaurant. You don't go to the kitchen to cook; you talk to the **Waiter**. The Waiter takes your order to the kitchen and brings your food back. 
An **API** is the waiter. It is the official bridge that allows your Python script to ask another computer for data safely.

#### Step 7: HTTP Methods (How we talk to the API)
When talking to an API, we use specific "Verbs" (HTTP Methods) to tell it what we want to do:
- 🟢 **GET**: "Please give me the data." (Retrieve)
- 🔵 **POST**: "Please save this new data." (Create)
- 🟡 **PUT / PATCH**: "Please update this existing data." (Update)
- 🔴 **DELETE**: "Please remove this data." (Delete)

#### Step 8: Status Codes & Data Formats
When the API replies, it gives us a **Status Code** so we know if it worked, and it returns the data in a format called **JSON**.
- **200 OK**: Success! Here is your data.
- **400 Bad Request**: You sent the wrong information.
- **404 Not Found**: The data you asked for doesn't exist.
- **500 Server Error**: The website's server crashed.

Understanding these codes helps us write Data Engineering pipelines that don't crash when errors happen.

---

## 🛠️ How to Run This Project

The absolute easiest way to learn is by using our **Interactive Jupyter Notebook**. You don't even need to install Python on your computer!

### Method 1: Google Colab (Recommended for Beginners)
1. Go to [Google Colab](https://colab.research.google.com/).
2. Click **File > Upload Notebook** and upload `api_web_scraping.ipynb` from this repository.
3. Run the cells one by one from top to bottom. The first cell will automatically install everything you need!

### Method 2: Running Locally (For Advanced Users)
If you want to run the python scripts directly on your machine:

1. Clone this repository and open your terminal.
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the modular scripts inside the `src/` folder to see each step in action!
   ```bash
   python src/01_html_and_dom/dom_navigation.py
   python src/03_api_fundamentals/http_methods_demo.py
   ```

Enjoy your journey into Data Engineering! 🎉
