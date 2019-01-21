# free-kindle-books
Returns a list of title, author, and purchase url for all free kindle books in the science-fiction genre.  Requires Scrapy.

Written using Python 3.7 and Scrapy 1.5.1

This is a small sample spider I built in an hour or so while learning Scrapy.  I'm going to go back and write the part 
that "purchases" all of these books for me, but that would need my login credentials, so I may not add that version to 
this repo.

Most of what I used came from https://learn.scrapinghub.com/scrapy/ and was done while I was NOT logged in.

`scrapy crawl -o books.json booklist` to run the spider and create the list of books.
