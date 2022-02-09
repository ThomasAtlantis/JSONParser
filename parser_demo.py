from parser import JSONParser
import json


parser = JSONParser(lambda t_id, t_id_str: 
     {"entities": {
    "hashtags": [],
    "symbols": [],
    "user_mentions": [
      {
        "screen_name": "photo_cns",
        "name": "CNS Photo",
        "id": t_id,
        "id_str": t_id_str,
        "indices": [
          3,
          13
        ]
      }
    ],
    "urls": []
  }})

print(json.dumps(parser.roadmaps, indent=2))
print(json.dumps(parser.get_wanted(file="parser_demo.json"), indent=2))
