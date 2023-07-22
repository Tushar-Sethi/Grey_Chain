# Grey_Chain

# There are two PY Files.

## 1. New_index.py 
This file is the main code with will scrape the data from the URL that will be provided. For this we need to call the endpoint "baseURL/scrape". Here we need to   provide the parameter 	"url" along with it's value that we need to scrape. This end point will return a dictionary with the links associated with the parent page as keys and the text present on all pages 	as there values in a list.
	
This file also contains another endpoint "baseURL/getLinks" which will return the URL's which contains the string that we want to search on all the related pages. Here we need to provide two parameters "url" and "sentence".
"url" -> the URL that we want to scrape data from
"sentence" -> the sentence that we would like to search all the related pages.

## 2. test_app.py
This file is the Unit test file which will test both the end points. We just need to run the py file and it would tell us whether both the end points return a valid response or not.



## To Test the end points in POSTMAN, please follow this structure while posting the data

"baseURL/scrape" -> { 'url' : 'valid url' }
'baseURL/getLinks" -> { 'url' : 'valid url', 'sentence' : 'string' }
