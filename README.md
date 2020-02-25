# Postcards from a Stranger || PO Box Zero

Capstone Project for GA Software Engineering Immersive Course.

The idea is to have a website where users can create anonymous postcards/messages/letters to anyone or no one in particular. These postcards could have any message – inspiration, rants, words of advice, or just anything really. I wanted to keep the sender anonymous so that they can be free to express themselves. I also wanted the 'recipients' to not know the senders to make the messages have more meaning to them and interpret them according to their situation.

## User Stories

[Click here](./planning/USER-STORIES.md)

## Wireframe

[Click here.](https://xd.adobe.com/view/d32d9749-1010-4adf-431a-960db3131c8e-a51c/)

## Technologies, Libraries

**Backend:** Python, PostgreSQL, Heroku, Pillow

**Frontend:** Django, Python, Bootstrap, crispy_forms

## Setup

Install dependencies  
`pip3 install -r requirements.txt --yes`

Create database (local staging)  
`psql -U postgres -f settings.sql`

## Models

**Postcard**

- image_url
- style (post MVP?)
- heading
- message
- created (date/time stamp)
- Sender (ref)
- Recipient (optional? email? multiple?)

**Sender** (edit: not really necessary)

- Name (any text)
- Postcards - (ref) multiple (edit: removed this relationship)

## Timetable

| Date      | Task/Milestone          | Time Alloted | Actual  |
| --------- | ----------------------- | ------------ | ------- |
| Feb 17    | Initial README          | 1 hr         | 1 hr    |
|           | Wireframe               | 1 hr         | 1 hr    |
| Feb 18    | Initial Setup           |              |         |
|           | DB, Models              | 2 hrs        | 2 hrs   |
|           | Views, URLs, HTMLs      | 2 hrs        | 1.5 hrs |
|           | Bootstrap               | 2 hrs        | 3 hrs   |
| Feb 19    | Reach MVP               |              |         |
|           | CRUD functions          | 3 hrs        | 2.5 hrs |
|           | Login Auth              | 2 hrs        | 1 hr    |
|           | Heroku deployment       | 2 hrs        | 3 hrs   |
| Feb 20    | Styling                 | 6 hrs        | 7 hrs   |
|           | crispy_forms            | 2 hrs        | 1 hr    |
| Feb 21    | Pillow implement        | 3 hrs        | 1.5 hrs |
|           | carousel image          | 2 hrs        | 1 hr    |
|           | more styling            | 1 hr         | 1 hr    |
|           | clean up code           | 1 hr         | 0.5 hr  |
|           | Misc bug fixes          | 3 hrs        | 3.5 hrs |
| Feb 24    | add favorites           | 3 hr         | 4 hrs   |
|           | misc styling            | 1 hr         | 1.5 hr  |
|           | view favorites          | 2 hrs        | 3 hrs   |
| Feb 25    | profile page            | 2 hrs        |         |
| Feb 19-25 | deploy with DEBUG=False | 6 hrs        |         |
| TOTAL     | TOTAL                   | 47 hrs       | 39 hrs  |

## Issues

2-18-2020:  
Error on migration of seed data.

```
django.db.utils.DataError: value too long for type character varying(100)
```

Solution: Changed length in database directly (using Postico), not through models.py because that didn't change anything.

2-19-2020:
Trying to deploy using Heroku. Multiple issues, DEBUG=True or False?
Ended up setting it to True, then setting the database entries in settings.py according to config vars in Heroku. Once deployed, will switch back to FALSE.

2-20-2020:  
`Invalid block tag on line 8: 'endblock'. Did you forget to register or load this tag?`  
Solution: `{% load crispy_forms_tags %}` should be right before the `<form>` tags.

2-21-2020:  
Images were not loading if `DEBUG=False` in settings.py.

Tried `python3 manage.py collectstatic` to put all static files into STATIC_ROOT. Didn't work.

Tried to add a key/value entry in Heroku config vars for MEDIA_URL.
Didn't work either.
