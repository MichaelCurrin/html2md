# HTML to Markdown
> CLI utility to convert HTML to Markdown

## Use case

Usually you can use a webscraper to download a webpage and then convert that to Markdown. But if you get blocked using a webdriver, you can save the rendered page's DOM and then put it through this CLI tool to convert it to Markdown. If you just copied the content directly and pasted into a text file, you'd lose the formatting, and putting into a rich-text format is not easy to work with from the CLI.

## Steps to download the HTML content

If the page is rendered with HTML and doesn't need JS, you can save the page as an HTML page using File / Save As in your browser.

If it is a JS-based website:

1. Open the devtools inspector.
1. Select the body element.
1. Right-click and copy the element with "Copy outerHTML".
1. Paste the content for use with the CLI tool.

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
