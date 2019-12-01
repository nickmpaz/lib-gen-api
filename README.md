# LibGenAPI

## About

LibGenAPI is an API for Library Genesis. Library Genesis (LibGen) is a search engine for articles and books on various topics, which allows free access to content that is otherwise paywalled or not digitized elsewhere. More information at [Library Genesis Wikipedia](https://en.wikipedia.org/wiki/Library_Genesis). The API that LibGen provides focuses on mirror site maintenance, and is not suitable for the average user. This API uses Python (Requests + BeautifulSoup4) to provide searching and downloading capabilities.

## Example

### Code
```
from libgenapi import LibGenAPI

api = LibGenAPI(debug=True)
results = api.search("arthur c clarke")
api.download(results[0])
```
### Results
```
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