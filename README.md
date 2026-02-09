# HTML to Markdown
> CLI utility to convert HTML to Markdown

[![GitHub tag](https://img.shields.io/github/tag/MichaelCurrin/html2md?include_prereleases=&sort=semver&color=blue)](https://github.com/MichaelCurrin/html2md/releases/)
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)

[![Made with Python](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2FMichaelCurrin%2Fhtml2md%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&query=project.requires-python&label=python&logo=python&logoColor=white)](https://python.org "Go to Python homepage")
[![dependency - poetry](https://img.shields.io/badge/poetry-2.x-blue)](https://pypi.org/project/poetry)


## Use case

Usually you can use a webscraper to download a webpage and then convert that to Markdown easily. 

If it's JS-based Single-Page app, then rather can save the rendered page's DOM and then put it through this CLI tool to convert it to Markdown.

As alternatives, if you just copied the content on the webpage directly and pasted into a plain text file, you'd lose the formatting (like headings and links), and if you pasted it into a rich-text format (like Word or Google Doc) is not easy to work with from the CLI.

## Steps to download the HTML content

### Plain HTML sites

If the page is rendered with HTML and doesn't need JS:

1. Save the page as an HTML page using _File / Save As_ in your browser.
1. Run the Python CLI tool.

### JS web apps

If it is a JS-based website:

1. Open the devtools inspector.
1. Select the body element.
1. Right-click and copy the element with "Copy outerHTML".
1. Paste the content into an HTML file.
1. Run the Python CLI tool.

## Usage

```console
> poetry run python -m html2md --help
```

```console
> poetry run python -m html2md -f in.html
**Hello**
```

```console
> poetry run python -m html2md -v '<b>Hello</b>'
**Hello**
```
