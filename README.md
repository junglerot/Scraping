# Advanced Web Scraping Project: Algo Monster Problem Solutions Collector

This README outlines an advanced web scraping project designed to collect solutions from the Algo Monster website and convert them into markdown files for easy reference and study. The project leverages Python, with `requests` for web requests, `BeautifulSoup` for HTML parsing, and `markdownify` for converting HTML to markdown. Additionally, a project demonstration video is included to showcase the process and functionality.

## Project Overview

The goal of this project is to automate the process of fetching programming problem solutions from a specific section of the Algo Monster website, sanitize the content, and save it as markdown files. This process involves sending HTTP requests, parsing the HTML content, cleaning and reformatting the data, and finally, writing the output in a structured markdown format.

## Tools and Libraries Used

- **requests**: For sending HTTP requests to the target URL.
- **BeautifulSoup**: For parsing HTML content and extracting necessary data.
- **markdownify**: For converting HTML content to markdown format.

## Implementation Details

1. **Fetching Data**: The script sends a GET request to the Algo Monster 'liteproblems' section. It checks for a successful response before proceeding.

2. **HTML Parsing**: Using BeautifulSoup, the script parses the HTML content to identify and iterate through the list of problems.

3. **URL and Filename Sanitization**: For each problem, the script constructs the URL and sanitizes the filename to ensure it is compatible with the file system.

4. **Content Extraction and Cleaning**: The script makes a request to each problem's URL, parses the HTML content, removes unnecessary elements (e.g., footers, ads), and prepares the content for conversion.

5. **Code Block Formatting**: Code blocks within the content are specifically formatted to markdown syntax to ensure readability and proper formatting in the output files.

6. **Markdown Conversion**: Using markdownify, the script converts the cleaned HTML content into markdown format, applying ATX style for headings.

7. **File Writing**: The markdown content is written to a file named after the problem, organized in an 'output' directory for easy access.

8. **Error Handling**: The script includes basic error handling for HTTP request failures, ensuring robustness in data collection.

## Project Demonstration Video

A comprehensive video demonstration of the project in action is available to illustrate the scraping process, the challenges encountered, and the solutions implemented. The video includes a step-by-step walkthrough of the script's execution, showcasing the extraction of problem solutions and their conversion into markdown format.

[Link to Project Demonstration Video](#)

## Running the Project

To run this project, ensure you have Python installed and the necessary libraries (`requests`, `beautifulsoup4`, `markdownify`). Clone the project, navigate to the project directory, and execute the script. The output markdown files will be saved in the designated output directory.

## Contribution and Customization

Contributions are welcome. The project can be customized for different sections of the Algo Monster website or adapted for other websites with similar needs for content collection and conversion.
