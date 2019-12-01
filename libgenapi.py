from mirrors import MIRRORS

class LibGenAPI():


    def __init__(self, debug=False):

        self.debug = debug
        self.mirrors = []

        for mirror in MIRRORS:
            if mirror.is_active():
                self.mirrors.append(mirror)

    def search(self, search_term, num_results=25):

        results = []

        # edge case: search term is <= 2 chars
        if len(search_term) <= 2:
            return results

        # try search with each mirror until results are returned
        for mirror in self.mirrors:
            results = mirror.search(search_term, num_results, self.debug)
            if len(results) > 0:
                break

        return results

    def download(self, book, filename=None):

        for mirror in self.mirrors:
            if mirror.download(book, filename, self.debug):
                return True

        return False