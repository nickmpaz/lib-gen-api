import requests, re
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup

class BaseMirror(ABC):

    POSSIBLE_NUM_RESULTS = [25, 50, 100]
    DEFAULT_NUM_RESULTS = 25

    @abstractmethod
    def __init__(self): 
        self.search_page = ""
        self.show_page= ""
        self.show_field = ""
        self.download_page = ""

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def is_active(self ):
        #TODO
        return True

    @abstractmethod
    def search(self, search_term, num_results, debug): 

        if debug: print("Trying search with %s." % str(self))

        book_list = []
    
        # ensure num_results is a valid number
        num_results = num_results if num_results in self.POSSIBLE_NUM_RESULTS else self.DEFAULT_NUM_RESULTS

        if debug: print("Getting search results.")

        payload = {
            "req": search_term,
            "res": num_results
        }
        r = requests.get(self.search_page, params=payload)
        page_content = BeautifulSoup(r.content, "html.parser")
        results = list(page_content.find("table", class_="c").children)[1:]

        if debug: print("Parsing search results.")


        for result in results:

            try:

                id_el = result.td
                author_el = id_el.next_sibling.next_sibling
                title_el = author_el.next_sibling.next_sibling
                publisher_el = title_el.next_sibling.next_sibling
                year_el = publisher_el.next_sibling.next_sibling
                pages_el = year_el.next_sibling.next_sibling
                language_el = pages_el.next_sibling.next_sibling
                size_el = language_el.next_sibling.next_sibling
                extension_el = size_el.next_sibling.next_sibling
                md5 = re.search('md5=([A-Z0-9]*)"', str(title_el)).group(1)
                title = title_el.get_text(separator="\n").splitlines()[0] 
                
                book_list.append({
                    "id": id_el.text,
                    "author": author_el.text,
                    "title": title,
                    "md5": md5,
                    "publisher": publisher_el.text,
                    "year": year_el.text,
                    "pages": pages_el.text,
                    "language": language_el.text,
                    "size": size_el.text,
                    "extension": extension_el.text
                })

            except: continue

        if debug: print("Returning %d results." % len(book_list))

        return book_list

    @abstractmethod
    def download(self, book, filename, debug): 

        if debug: print("Trying download with %s." % str(self))

        # if no filename, set default
        if not filename: filename = book['title']

        r = requests.get(self.show_page % book[self.show_field])
        page_content = BeautifulSoup(r.content, "html.parser")
        download_link = page_content.find('a', href=True)
        download = self.download_page % download_link['href']
        r = requests.get(download, stream = True) 

        if r.status_code != 200: return False

        if debug: print('downloading to "%s"...' % filename)

        with open(filename, "wb") as download: 
            
            total_length = int(r.headers.get('content-length'))
            current_length = 0
            percentage = 0

            for chunk in r.iter_content(chunk_size=64): 
                if chunk: 
                    download.write(chunk)             
                if debug:
                    current_length += 64
                    new_percentage = int((current_length / total_length) * 100)
                    if new_percentage % 10 == 0 and new_percentage != percentage:
                        percentage = new_percentage
                        print("%d%%" % percentage)
                

        return True

class GenLibRus(BaseMirror):

    def __init__(self):
        self.search_page = "http://gen.lib.rus.ec/search.php"
        self.show_page= "http://93.174.95.29/_ads/%s"
        self.show_field = "md5"
        self.download_page = "http://93.174.95.29%s"

    def __str__(self):
        return "http://gen.lib.rus.ec"

    def is_active(self):
        
        return super().is_active()

    def search(self, search_term, num_results, debug):

        return super().search(search_term, num_results, debug)

    def download(self, book, filename, debug):
        
        return super().download(book, filename, debug)



MIRRORS = [GenLibRus()]