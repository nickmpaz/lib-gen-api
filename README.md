# LibGenAPI

## About

LibGenAPI is an API for Library Genesis. Library Genesis (LibGen) is a search engine for articles and books on various topics, which allows free access to content that is otherwise paywalled or not digitized elsewhere. More information at [Library Genesis Wikipedia](https://en.wikipedia.org/wiki/Library_Genesis). The API that LibGen provides focuses on mirror site maintenance, and is not suitable for the average user. This API uses Python (Requests + BeautifulSoup4) to provide searching and downloading capabilities.

## Example

```
>>> from libgenapi import LibGenAPI

>>> api = LibGenAPI(debug=True)
>>> results = api.search("arthur c clarke")
>>> api.download(results[0])

Trying search with http://gen.lib.rus.ec.
Getting search results.
Parsing search results.
Returning 25 results.
Trying download with http://gen.lib.rus.ec.
downloading to "Interplanetary Flight"...
10%
20%
30%
40%
50%
60%
70%
80%
90%
100%
```

## Usage

LibGenAPI.search(search_term, num_results=25)

- PARAM (string) search_term: The term to search for on LibGen
- PARAM (int) num_results: The maximum number of results to retrieve. Acceptable values are 25, 50, 100.
- RETURNS: A list of results. Results are dictionaries containing information about a book (title, author, etc). 

LibGenAPI.download(book, filename=None)

- PARAM (dict) book: The book to download. This dictionary can be obtained with LibGenAPI.search().
- PARAM (string) filename: The location to download the book to.
- RETURNS: True if download is successful else false.

