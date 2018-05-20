import json
import re

from apiaryProject import processes


class SampleOfSolutions:

    def __init__(self, soup):
        self.soup = soup

    def possible_solution_one(self):
        # search through the text for the text using regex
        text = self.soup.find(text=re.compile('window.Apiary.APPLICATION_DATA ='))
        # remove new line characters
        output = text.split('\n')
        # remove empty white space elements from list
        output = [x.strip(' ') for x in output]
        # remove empty elements from list
        output = filter(None, output)
        # first match out of the list that contain the keyword
        unicode_str = next((s for s in output if "window.Apiary.APPLICATION_DATA" in s))
        # convert unicode to str and also split the str on equal sign first match
        columns = unicode_str.encode('utf-8').split('=', 1)
        # keep first column that we are interested
        string = columns[1]
        # remove first and last character of string
        string = string[1:-1]
        # convert string to json
        parsed = json.loads(string)
        return json.dumps(parsed, indent=4, sort_keys=True)

    def possible_solution_two(self):
        # get only text
        text = self.soup.get_text()
        # decode unicode to string
        text = text.encode('utf8')
        # remove new line characters
        output = text.rstrip().split('\n')
        # remove empty elements
        output = filter(None, output)
        return output

    def possible_solution_three(self):
        # extract matching elements based on regex
        matched_elements = \
            [match.get('id') for match in self.soup.find_all('div',
                                                             id=re.compile("application"))]
        return matched_elements


if __name__ == '__main__':
    # get and parse the page for all solutions
    page = processes.get_page("https://apiary.docs.apiary.io")

    # parse page with Beautiful soup
    soupObject = processes.parse_page(page)

    # instantiate class to be used by all solutions
    sampleOfCodesObject = SampleOfSolutions(soupObject)
    # print(sampleOfCodesObject.possible_solution_one())
    # print(sampleOfCodesObject.possible_solution_two())
    # print(sampleOfCodesObject.possible_solution_three())

    url = "https://api.apiary.io/blueprint/publish/publicpersonalapi"
    file_to_send = "myFile.json"

    postRequest = processes.post_to_page(url, file_to_send)
    print(postRequest.content)
