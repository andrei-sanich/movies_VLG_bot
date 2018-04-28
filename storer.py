import shelve


class Storer():



    def __init__(self, filename):

        self.filename = filename

    def save_user(self, key):
        db = shelve.open(self.filename, writeback=True)
        db[key] = []
        db.close()
    
    def check_user(self, key):
        db = shelve.open(self.filename, writeback=True)
        if key in db:
            db.close()
            return True

    def get_keys(self):
    	db = shelve.open(self.filename, writeback=True)
    	res = list(db.keys())
    	db.close()
    	return res
    	
    def add_template(self, key, template):
        db = shelve.open(self.filename, writeback=True)
        data = db[key]
        userset = {
            	    'template_name': template,
                	'set': []
                  }
        data.append(userset)
        db[key] = data
        db.close()

    def add_genre(self, key, template, genre):
        db = shelve.open(self.filename, writeback=True)
        data = db[key]
        for item in data:
            if item['template_name'] == template:
                item['set'].append(genre)
                db[key] = data
        db.close()   

    def save(self, key, data):
        db = shelve.open(self.filename, writeback=True)
        db[key] = data
        db.close()
	
    def get_data(self, key):
	    db = shelve.open(self.filename, writeback=True)
	    data = db[key]
	    db.close()
	    return data

    def get_templates(self, key):
    	db = shelve.open(self.filename, writeback=True)
    	data = db[key]
    	templates = [element['template_name'] for element in data]
    	return templates

    def get_usersets(self, key):
    	db = shelve.open(self.filename, writeback=True)
    	data = db[key]
    	usersets = [element['set'] for element in data]
    	return usersets

    def get_genres(self, key, template):
    	db = shelve.open(self.filename, writeback=True)
    	data = db[key]
    	if data['template_name'] == template:
    		genres = data['set']
    		db.close()
    		return genres

    def del_genre(self, key, template, genre):
        db = shelve.open(self.filename, writeback=True)
        data = db[key]
        for item in data:
            if item['template_name'] == template:
                genres = item['set']
                genres.remove(genre)
                db[key] = data
                db.close()  
