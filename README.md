Interview
=========


URLSerivces:-
===========

<i class="icon-refresh"></i> **Save a URL with Tags**

Create New URL with Tags and save both Tags and URL

>- Request:- post
>-  class :- Insert_URL
>- URL:- http://127.0.0.1/interview/bookmarks/
>- Rsponse Type :- Json
>- Request Data:-
{
	  "bookmark": "http://abc.com",
	  "urlid": [
     {
	      "tag": "abc"
     }
  ]
}
>- Status:- HTTP_201_CREATED
>-  Response :-  "created"

<i class="icon-upload"></i> **Get  URL**

Fetch all the Tags attached to the URL
>- Request:- GET
>-  class :- Url_Detail_Update
>- URL:- http://127.0.0.1/interview/bookmarks/(id)
>- Request:- id = **some id**(1)
>- Content Type :- application/json
>Response:- 
{
    "Url": "http://facebook.com",
    "tags": [
        "facebook",
        "vis",
        "dron",
        "kai",
        "bk",
        "parlay",
        "fbvish",
        "captain"
    ]
}
status:- HTTP_200_OK
Response Type:- Json

<i class="icon-pencil"></i> **Edit URL**

>- Request:- PUT
>-  class :- Edit_URL
>- URL:- http://127.0.0.1/interview/bookmarks/(id)/edit
>- Request: - id= **some id**
> Content Type:- application/json
>- Rsponse Type :- Json
>- Status:- HTTP_200_OK
>-  Response :- {
    "Url": "http://github.com",
    "tags": [
        "gmail",
        "lnkdn",
        "github",
        "git"
    ]
}
<i class="icon-trash"></i> **Delete URL**

Delete URL.
>- Request:- Delete
>- class:- Url_Detail_Update
>- URL:- http://127.0.0.1/interview/bookmarks/9
>- Request:- id=9
>- Response Type:- Json
>- Status :- HTTP_302_FOUND

Tag Services
============
<i class="icon-refresh"></i> **Save Tag**

Create New Tag and save it.

>- Request:- post
>-  class :- Create_Tag
>- URL:- http://127.0.0.1/interview/tags/new/
>- Request Data:-
{
    "tag": "any tag"
}
>- Content Type :- application/json
>Response:- 
{
	"message": "Tag was successfully created"
    "Name": "ljxnvkjdhnigkhdvnkada"
}
status:- HTTP_201_CREATED
Response Type:- Json 

<i class="icon-upload"></i> **Get  Tag**

Fetch all attached URL with corresponding tag.

>- Request:- GET
>-  class :- Tag_Detail_Upadte
>- URL:- http://127.0.0.1/interview/tags/(id)
>- Request:- id = **some id**(4)
>- Content Type :- application/json
>Response:- 
{
    "bookmarks": [
        {
            "id": 2,
            "bookmark": "http://gmail.com"
        },
        {
            "id": 11,
            "bookmark": "http://yatra.com"
        }
    ],
    "tag": "gmail"
}
status:- HTTP_200_OK
Response Type:- Json

<i class="icon-pencil"></i> **Rename the Tag**

Rename the Tag
>- Request:- GET
>-  class :- Edit_Tag
>- URL:- http://127.0.0.1/interview/tags/7/edit  id=7
>- Request: - id=7
>- Rsponse Type :- Json
>- Status:- HTTP_200_OK
>-  Response :- {
					 Name:  coding+
					Url:- https://www.apple.com
					}
				
<i class="icon-trash"></i> **Delete Tag**
>- Request:- GET
>-  class :- Edit_Tag
>- URL:- http://127.0.0.1/interview/tags/7/edit  id=7
>- Request: - id=7
>- Rsponse Type :- Json
>- Status:- HTTP_200_OK
>-  Response :- {
					 Name:  coding+
					Url:- https://www.apple.com
					}
Delete Tag and free URL attach with Tag.
>- Request:- Delete
>- class:- Tag_Detail_Upadte
>- URL:- http://127.0.0.1/interview/tags/9
>- Request:- id=9
>- Response Type:- Json
>- Status :- HTTP_302_FOUND

