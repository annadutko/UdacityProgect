import udacity

user = udacity.User('email@example.com', 'password123')
name = user.name()

# print out quiz completion rate in each course
for course in user.enrollments():
    prog = user.progress(course)
    print('Course: ' + prog['title'])
    print('\t' + str(prog['quizzes_completed']) + '/'
            + str(prog['quiz_count']) + ' quizzes completed')
