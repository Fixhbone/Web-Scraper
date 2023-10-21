from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" class = "special">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""


soup = BeautifulSoup(html_doc,'html.parser')

# d = soup.find_all("div")
# d = soup.find(id="first")
# d = soup.find_all(class_="special")
# d = soup.select(".special")
# print(d)

for el in soup.select(".special"):
    print(el.name)
    print(el.attrs)  


