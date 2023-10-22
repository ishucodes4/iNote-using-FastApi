def noteentity(item)->dict:
    return {
        "id":str(item["_id"]),
        "titles":item["item"],
        "desc":item["desc"],
        "important":item["important"],
    }

def notesentity(item)->lest:
    return [noteentity(item) for item in items]

