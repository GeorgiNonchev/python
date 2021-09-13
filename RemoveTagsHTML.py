# import modules
import bs4, requests
  
# Get html
# Scraping the data from
# example.html

exampleFile = open('example.html')

  
def remove_tags(html):
  
    # parse html content
    soup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
  
    for data in soup(['style', 'script']):
        # Remove tags
        data.decompose()
  
    # return data by retrieving the tag content
    return ' '.join(soup.stripped_strings)
  
  
# Print the extracted data
print(remove_tags(exampleFile))
