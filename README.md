# Google Forms Bot

Automatically fill out a single-page google form with multiple choice answers based on a given list of questions and answers.

`form_url` must be a string with the url to the google form

`data` must be a dictionary with string keys and values, such that the key is the question text and value is the desired response selection.

For any required questions without given answers in `data`, the selected answer will be chosen at random.

A file named chromedriver.exe with the appropriate chrome driver must be present
