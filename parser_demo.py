from parser import JSONParser
import json


package = r'''
{
  "created_at": "Sat Jan 29 08:00:58 +0000 2022",
  "id": 1487334944699469824,
  "id_str": "1487334944699469824",
  "text": "RT @photo_cns: Some 14,000 college students in Beijing enter the competition zones from January 22 to 23, 2022 and begin to serve Beijing 2\u2026",
  "truncated": false,
  "entities": {
    "hashtags": [],
    "symbols": [],
    "user_mentions": [
      {
        "screen_name": "photo_cns",
        "name": "CNS Photo",
        "id": 819369475153821696,
        "id_str": "819369475153821696",
        "indices": [
          3,
          13
        ]
      }
    ],
    "urls": []
  },
  "metadata": {
    "iso_language_code": "en",
    "result_type": "recent"
  },
  "source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
  "in_reply_to_status_id": null,
  "in_reply_to_status_id_str": null,
  "in_reply_to_user_id": null,
  "in_reply_to_user_id_str": null,
  "in_reply_to_screen_name": null,
  "user": {
    "id": 1484823769478836226,
    "id_str": "1484823769478836226",
    "name": "Arm Saroyan",
    "screen_name": "arm_saroyan",
    "location": "",
    "description": "Easy mother",
    "url": null,
    "entities": {
      "description": {
        "urls": []
      }
    },
    "protected": false,
    "followers_count": 0,
    "friends_count": 18,
    "listed_count": 0,
    "created_at": "Sat Jan 22 09:42:38 +0000 2022",
    "favourites_count": 1,
    "utc_offset": null,
    "time_zone": null,
    "geo_enabled": false,
    "verified": false,
    "statuses_count": 42,
    "lang": null,
    "contributors_enabled": false,
    "is_translator": false,
    "is_translation_enabled": false,
    "profile_background_color": "F5F8FA",
    "profile_background_image_url": null,
    "profile_background_image_url_https": null,
    "profile_background_tile": false,
    "profile_image_url": "http://pbs.twimg.com/profile_images/1484823812696858632/QoKL1fBU_normal.png",
    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1484823812696858632/QoKL1fBU_normal.png",
    "profile_link_color": "1DA1F2",
    "profile_sidebar_border_color": "C0DEED",
    "profile_sidebar_fill_color": "DDEEF6",
    "profile_text_color": "333333",
    "profile_use_background_image": true,
    "has_extended_profile": true,
    "default_profile": true,
    "default_profile_image": false,
    "following": false,
    "follow_request_sent": false,
    "notifications": false,
    "translator_type": "none",
    "withheld_in_countries": []
  },
  "geo": null,
  "coordinates": null,
  "place": null,
  "contributors": null,
  "retweeted_status": {
    "created_at": "Thu Jan 27 08:32:41 +0000 2022",
    "id": 1486618149176840197,
    "id_str": "1486618149176840197",
    "text": "Some 14,000 college students in Beijing enter the competition zones from January 22 to 23, 2022 and begin to serve\u2026 https://t.co/exH76Zbkbc",
    "truncated": true,
    "entities": {
      "hashtags": [],
      "symbols": [],
      "user_mentions": [],
      "urls": [
        {
          "url": "https://t.co/exH76Zbkbc",
          "expanded_url": "https://twitter.com/i/web/status/1486618149176840197",
          "display_url": "twitter.com/i/web/status/1\u2026",
          "indices": [
            116,
            139
          ]
        }
      ]
    },
    "metadata": {
      "iso_language_code": "en",
      "result_type": "recent"
    },
    "source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
    "in_reply_to_status_id": null,
    "in_reply_to_status_id_str": null,
    "in_reply_to_user_id": null,
    "in_reply_to_user_id_str": null,
    "in_reply_to_screen_name": null,
    "user": {
      "id": 819369475153821696,
      "id_str": "819369475153821696",
      "name": "CNS Photo",
      "screen_name": "photo_cns",
      "location": "Beijing",
      "description": "CNSPHOTO is the photo platform of China News Service(CNS). https://t.co/6TVJMvlEhz",
      "url": "https://t.co/6TVJMvlEhz",
      "entities": {
        "url": {
          "urls": [
            {
              "url": "https://t.co/6TVJMvlEhz",
              "expanded_url": "http://www.cnsphoto.com",
              "display_url": "cnsphoto.com",
              "indices": [
                0,
                23
              ]
            }
          ]
        },
        "description": {
          "urls": [
            {
              "url": "https://t.co/6TVJMvlEhz",
              "expanded_url": "http://www.cnsphoto.com",
              "display_url": "cnsphoto.com",
              "indices": [
                59,
                82
              ]
            }
          ]
        }
      },
      "protected": false,
      "followers_count": 29401,
      "friends_count": 4111,
      "listed_count": 34,
      "created_at": "Thu Jan 12 02:24:40 +0000 2017",
      "favourites_count": 680,
      "utc_offset": null,
      "time_zone": null,
      "geo_enabled": false,
      "verified": false,
      "statuses_count": 8289,
      "lang": null,
      "contributors_enabled": false,
      "is_translator": false,
      "is_translation_enabled": false,
      "profile_background_color": "000000",
      "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
      "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
      "profile_background_tile": false,
      "profile_image_url": "http://pbs.twimg.com/profile_images/843732471761981441/zic6NUXB_normal.jpg",
      "profile_image_url_https": "https://pbs.twimg.com/profile_images/843732471761981441/zic6NUXB_normal.jpg",
      "profile_banner_url": "https://pbs.twimg.com/profile_banners/819369475153821696/1489996851",
      "profile_link_color": "0084B4",
      "profile_sidebar_border_color": "000000",
      "profile_sidebar_fill_color": "000000",
      "profile_text_color": "000000",
      "profile_use_background_image": false,
      "has_extended_profile": false,
      "default_profile": false,
      "default_profile_image": false,
      "following": false,
      "follow_request_sent": false,
      "notifications": false,
      "translator_type": "none",
      "withheld_in_countries": []
    },
    "geo": null,
    "coordinates": null,
    "place": null,
    "contributors": null,
    "is_quote_status": false,
    "retweet_count": 9,
    "favorite_count": 6,
    "favorited": false,
    "retweeted": false,
    "possibly_sensitive": false,
    "lang": "en"
  },
  "is_quote_status": false,
  "retweet_count": 9,
  "favorite_count": 0,
  "favorited": false,
  "retweeted": false,
  "lang": "en"
}
'''

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
print(json.dumps(parser.get_wanted(raw=package), indent=2))
