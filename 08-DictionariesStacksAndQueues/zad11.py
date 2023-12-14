import json

movie={"title":"The Hunger Games",
       "Year":2012,
       "actor":{"leading":"Jennifer Lawrence",
                "supporting":"Josh Huterson"},
        "oscar":True,
        "Rating out of 10":9}

with open("favourite.json",'w') as file:
    json.dump(movie, file, indent=2)

