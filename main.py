import requests
import requests_html

def fetch(url):
    response = requests.get(url)
    return response

def get_hot_boards():
    
    url = "https://www.ptt.cc/bbs/index.html"
    resp = fetch(url)
    html = requests_html.HTML(html=resp.text)
    boards = html.find('div.b-ent')

    board_list = []

    for board in boards:
        board_list.append({
            "name": board.find('div.board-name', first=True).text,
            "nuser": board.find('div.board-nuser', first=True).text,
            "class": board.find('div.board-class', first=True).text,
            "title": board.find('div.board-title', first=True).text
        })
    
    return board_list
    
def main():
    board_list = get_hot_boards()
    for board in board_list:
        print('{0: <20}{1: >6} {2: <6}\t{3: <30}'.format(board['name'], board['nuser'], board['class'], board['title']))

if __name__ == "__main__":
    main()