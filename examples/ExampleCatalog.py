import udacity

c = udacity.Catalog()

tracks = c.tracks()

track_names = [t['name'] for t in tracks]
web_dev_teachers = c.instructors('cs253')
nd001_description = c.degree('nd001')['expected_learning']