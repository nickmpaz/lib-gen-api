from libgenapi import LibGenAPI

api = LibGenAPI(debug=True)
results = api.search("arthur c clarke")
api.download(results[0])