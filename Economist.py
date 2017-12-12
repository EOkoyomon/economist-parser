from bs4 import BeautifulSoup
# from urllib.request import urlopen
import sys
import json

class Main():
  def __init__(self, path, output_name):
    self.path = path
    self.output_name = output_name
    # self.page = urlopen(self.path)
    #self.soup = BeautifulSoup(self.page, 'html.parser')
    with open(path, 'r') as file:
      self.soup = BeautifulSoup(file.read(), 'html.parser')

  def run(self):
    script = self.soup.find('script', id='preloadedData')
    sections = json.loads(script.text)
    text = []
    for sect in sections:
      if type(sect) == dict:
        if 'response' in sect:
          if 'content' in sect['response']:
            if 'text' in sect['response']['content']:
              text.append(sect['response']['content']['text'])
    if not text:
      print("Sorry, the html file does not have the required sections.")
      exit(2)

    print("Trying all", len(text), "sections")

    for num, txt in enumerate(text, 1):
      print(self.output_name + str(num) + '.html')
      with open(self.output_name + str(num) + '.html', 'w') as out:
        out.write(txt.replace('\/', '/'))
    return

if __name__ == '__main__':
  if len(sys.argv) != 3:
    print("\nUSAGE python3 Economist.py <absolute_path> <output_name>\n\nabsolute_path - full path to saved file. Necessary if script is not in the same directory as the file.\noutput_name - file to be treated as output. Must not have an extension, just the name")
    exit(1)
  parser = Main(sys.argv[1], sys.argv[2])
  parser.run()
