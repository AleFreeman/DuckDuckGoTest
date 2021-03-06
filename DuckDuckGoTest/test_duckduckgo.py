import pytest
import requests
url_ddg = "https://api.duckduckgo.com"
presidents = ["washington", "adams", "jefferson", "madison", "monroe",
              "jackson", "buren", "harrison", "tyler", "polk",
              "taylor", "fillmore", "pierce", "buchanan", "lincoln",
              "grant", "hayes", "garfield", "arthur", "cleveland",
              "harrison", "mckinley", "roosevelt", "taft", "wilson",
              "harding", "coolidge", "hoover", "truman", "eisenhower",
              "kennedy", "johnson", "nixon", "ford", "carter",
              "reagan", "bush", "clinton", "obama", "trump"]

def test_ddg0():
    resp = requests.get(url_ddg + "/?q=presidents of the united states&format=json")
    rsp_data = resp.json()
    topics = rsp_data["RelatedTopics"]
    foundPresidents = 0
    for i in range(len(presidents)):
        for topic in topics:
            if presidents[i] in topic['Text'].lower():
                foundPresidents += 1
                break
    assert foundPresidents == len(presidents)
