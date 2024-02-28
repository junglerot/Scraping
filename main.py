import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

# The target URL
url_initial = 'https://algo.monster/liteproblems'

# Send a GET request to the URL
response_initial = requests.get(url_initial)

# Check if the request was successful
if response_initial.status_code == 200:
    # Use BeautifulSoup to parse the HTML content
    soup_initial = BeautifulSoup(response_initial.content, 'html.parser')
    
    lists = soup_initial.find_all('ul', class_='Toc_articleList__aDF0z')[68].find_all('li')
    for list in lists:
        url = 'https://algo.monster' + list.find('a')['href']
        filename = list.text.replace('/', '-').replace('\\', '-')  # Sanitize filename
        filename = 'output/' + filename + '.md'

        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text.replace('<pre>', '<div>').replace('</pre>', '</div>'), 'html.parser')

            footer_div = soup.find('div', class_='CallToGetPremium_container__an75T')
            footer_ps = soup.find_all('p', class_='RequestClarification_bodytext__5sGkF')
            footer_div.decompose()

            for footer_p in footer_ps:
                footer_p.decompose()
            code_blocks = soup.find_all('code')

            for block in code_blocks:
                # Replace code blocks with Markdown code fence (```) syntax
                # This is a simplistic approach and may need adjustment based on your HTML structure
                spans = block.find_all('span')
                for span in spans:
                    span_text = span.text
                    span.replace_with(span_text) 
                if len(spans) > 0:
                    code_text = block.get_text()
                    markdown_code_block = f"python\n{code_text}\n"
                    block.replace_with(markdown_code_block)               
            # soup.prettify()
            markdown_content = md(str(soup.find('main')), heading_style="ATX")
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(markdown_content)
            print(filename)
        else:
            print("Failed to retrieve the content")
else:
    print("Failed to retrieve the content")
