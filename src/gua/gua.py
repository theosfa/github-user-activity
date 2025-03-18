import requests
import json
import argparse
from gua.printing import printEventDetails

__all__ = ["main", "Gua"]



class Gua:
    def __init__(self,
                 per_page : int = 30,
                 num_page : int = 1,
                 user : str = None,
                 repos : bool = False,
                 activity : bool = False,
                 info : bool = False,
                 ) -> None:
        self.payload = { "per_page" : per_page , "page" : num_page}
        self.user = user
        self.repos = repos
        self.activity = activity
        self.info = info
        self.url_repos = "/repos"
        self.url_activity = "/events"
        self.url = 'https://api.github.com/users'
    
    def run(self) -> None:
        if self.info :
            self.getUserInfo()
        if self.repos :
            self.getUserRepos()
        if self.activity :
            self.getUserActivity()
        
    def getUserRepos(self) -> None:
        url = self.url + "/" + self.user + self.url_repos
        
        r = requests.get(url=url, params=self.payload)
        data = json.loads(r.text)
        
        if r.status_code == 200:
            print(f"\nRepos of {self.user}:")
            for i, d in enumerate(data):
                print(f"  {i+1}{" " if i+1 < 10 else ""} : {d["name"]}")
        else:
            print(f"Error: {data["message"]}.\nTry another nickname")
    
    def getUserActivity(self) -> None:
        url = self.url + "/" + self.user + self.url_activity
        
        r = requests.get(url=url, params=self.payload)
        data = json.loads(r.text)
        
        if r.status_code == 200:
            print(f"\nLast activity of  {self.user}:")
            for i, d in enumerate(data):
                printEventDetails(d)
        else:
            print(f"Error: {data["message"]}.\nTry another nickname")
    
    def getUserInfo(self) -> None:
        url = self.url + "/" + self.user
        
        r = requests.get(url=url, params=self.payload)
        data = json.loads(r.text)
        
        if r.status_code == 200:
            print(f"\nInfo about {self.user}:")
            show_i = [0,1,3,6,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]
            for i, d in enumerate(data):
                if i in show_i:
                    print(f"  {show_i.index(i)+1}{" " if show_i.index(i)+1 < 10 else ""} : {d}{" "*(16-len(d))} -\t{data[d]}")
        else:
            print(f"Error: {data["message"]}.\nTry another nickname")

parser = argparse.ArgumentParser(description="CLI app for gathering info about user on GitHub")

parser.add_argument(
    "user",
    help="user nickname"
)
parser.add_argument(
    "-r",
    "--repos",
    help="shows repos of user",
    action="store_true",
    default=False,
    dest="repos",
)
parser.add_argument(
    "-a",
    "--activity",
    help="shows users activity",
    action="store_true",
    default=False,
    dest="activity",
)
parser.add_argument(
    "-i",
    "--info",
    help="shows users info",
    action="store_true",
    default=False,
    dest="info",
)
parser.add_argument(
    "-p",
    "--per_page",
    help="How many info to show (default:30)",
    nargs=1,
    type=int,
    required=False,
    default=30,
    metavar="<amount>",
    dest="per_page"
)
parser.add_argument(
    "-n",
    "--num_page",
    help="On which page show info (default:1)",
    nargs=1,
    type=int,
    required=False,
    default=1,
    metavar="<amount>",
    dest="num_page"
)

def main(args : list[str]) -> None:
    flags = parser.parse_args(args)
    gua = Gua(per_page=flags.per_page,
              num_page=flags.num_page,
              user=flags.user,
              repos=flags.repos,
              activity=flags.activity,
              info=flags.info)
    gua.run()