#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests
import random
import pprint
def main():
    """Run time code"""
    # create r, which is our request object
    r = requests.get("https://cat-fact.herokuapp.com/facts")

    # display the methods available to our new object

    max_upvote = -1
    for cats in r.json()["all"]:
        if cats.get("upvotes") >= max_upvote:
            max_upvote = cats["upvotes"]
    print("max upvote is: " , max_upvote)
    pprint.pprint( random.choice(r.json()["all"]))


main()

