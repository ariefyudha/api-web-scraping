from bs4 import BeautifulSoup

def demonstrate_dom_navigation():
    print("=== Step 2 & 3: HTML Structure & DOM Navigation ===\n")
    
    # Simple HTML Document
    html_content = """
    <html>
        <body>
            <div id="job-board">
                <h2>Recent Job Postings</h2>
                <div class="job-item" id="job-1">
                    <h3 class="title">Data Engineer</h3>
                    <p class="company">Tech Corp</p>
                    <span class="location">Remote</span>
                </div>
                <div class="job-item" id="job-2">
                    <h3 class="title">Data Analyst</h3>
                    <p class="company">Data Inc</p>
                    <span class="location">New York</span>
                </div>
            </div>
        </body>
    </html>
    """
    
    print("[INFO] Parsing HTML content...")
    soup = BeautifulSoup(html_content, 'html.parser')
    
    print("\n--- 1. Understanding HTML Tags & Attributes ---")
    job_1 = soup.find('div', id='job-1')
    print("Element Tag   :", job_1.name)
    print("Attributes    :", job_1.attrs)
    
    print("\n--- 2. DOM Parent Relationship ---")
    title_element = job_1.find('h3', class_='title')
    print("Child (Title) :", title_element.text)
    print("Parent Tag    :", title_element.parent.name)
    print("Parent ID     :", title_element.parent.get('id'))
    
    print("\n--- 3. DOM Sibling Relationship ---")
    company_element = title_element.find_next_sibling('p')
    print("Current Child :", title_element.text)
    print("Next Sibling  :", company_element.text)
    
    print("\n--- 4. Extracting Content ---")
    all_jobs = soup.find_all('div', class_='job-item')
    for job in all_jobs:
        title = job.find('h3').text
        company = job.find('p').text
        location = job.find('span').text
        print(f"-> {title} at {company} ({location})")

if __name__ == "__main__":
    demonstrate_dom_navigation()
