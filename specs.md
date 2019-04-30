![Komo Blog](https://neilpatel-qvjnwj7eutn3.netdna-ssl.com/wp-content/uploads/2017/07/corporatepersonalblog.jpg)

This App consumes [Quotes API](http://quotes.stormconsultancy.co.uk/random.json) to display random quotes.

You can see the live Application here [Komo Blog](https://komo-blog.herokuapp.com/)

Author Information
========
James Komo 

Features
========

- Built with Python 3.6, Flask microframework
- Shows 'Blog Posts', 'blog comments','Random Quotes' and sorted by relevancy
- Styled using Bootstrap and Google Fonts
- Handles external get quotes and requests from API
- Get blog posts from various writers (`Choose from landing page`)


Installation
========

    $ git clone https://github.com/jameskomo/personal-blog.git


Usage
========

**NOTE:** You need to have fully cloned it to run it locally.


    $ ./start.sh 

    # it will launch the web page from local server and fetch 
    quotes using api provided. You will also be able to use the blog site after sign up


API Object Reference
========

## Classes: `Blog, Comment, Subscribe`


**Arguments:**

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| `Quote` | string | No | Returns the quotes from the API. | `(empty string)`  |
| `Blog` | integer | No | Returns the articles from this news source only. | `(user's choice)` |



Tests
========

To run the tests locally just do:

    $ cd app
    $ python3.6 test_blog.py


The tests are run on a local test server.

Contribute
========

If you want to add any new features, or improve existing ones, feel free to send a pull request!
