# Postcards from a Stranger || PO Box Zero

Capstone Project for GA Software Engineering Immersive Course.

The idea is to have a website where visitors can pick a random postcard and browse through strangers' letters, notes, messages, etc. Visitors can also sign up as users so that they can create anonymous postcards/messages/letters to anyone or no one in particular. These postcards could have any message – inspiration, rants, words of advice, or just anything really. I wanted to keep the sender anonymous so that they can be free to express themselves. I also wanted the 'recipients' to not know the senders to make the messages have more meaning to them and interpret them according to their situation.

## User Stories

[Click here](./planning/USER-STORIES.md)

## Wireframe

[Click here.](https://xd.adobe.com/view/d32d9749-1010-4adf-431a-960db3131c8e-a51c/)

## Technologies, Libraries

**Backend:** Python, PostgreSQL, Heroku, Pillow, AWS S3

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
- created (date/time stamp) (hidden)
- Author (ref; not displayed on postcard)
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
| Feb 25    | profile page            | 2 hrs        | 1 hr    |
|           | more styling tweaks     | 1 hr         | 2 hr    |
| Feb 19-25 | deploy with DEBUG=False | 6 hrs        | 7~ hrs  |
| TOTAL     | TOTAL                   | 48 hrs       | 49~ hrs |

## Issues

<details><summary>2-18-2020:  </summary>

Error on migration of seed data.

```
django.db.utils.DataError: value too long for type character varying(100)
```

Solution: Changed length in database directly (using Postico), not through models.py because that didn't change anything.</details>

<details><summary>2-19-2020:  </summary>

Trying to deploy using Heroku. Multiple issues, `DEBUG=True` or `False`?
Ended up setting it to `True`, then setting the database entries in settings.py according to config vars in Heroku. Once deployed, will switch back to `False`.</details>

<details><summary>2-20-2020:  </summary>

Error: `Invalid block tag on line 8: 'endblock'. Did you forget to register or load this tag?`  
Solution: `{% load crispy_forms_tags %}` should be right before the `<form>` tags.</details>

<details><summary>2-21-2020:  </summary>

Images were not loading if `DEBUG=False` in settings.py.
Tried `python3 manage.py collectstatic` to put all static files into `STATIC_ROOT`. Didn't work.
Tried to add a key/value entry in Heroku config vars for `MEDIA_URL`.
Didn't work either.</details>

<details><summary>3-17-2020:  </summary>

Resumed working on this project, trying to implement file storage using AWS S3.  
Followed a tutorial and was having trouble deploying to Heroku. Turns out it was just a matter of updating `requirements.txt`.

</details>

<details><summary>3-18-2020:  </summary>

Deploying to Heroku, using AWS, and setting `DEBUG=False` causes so much confusion. Honestly, it's working now, but I've done so much fiddling around that I am not 100% what the solution was. Basically it has definitely something to do with the location of static files, media files, etc.</details>

<details><summary>3-19-2020:  </summary>

Well, image uploaded through web app properly gets uploaded to AWS S3 but trying to display the image is not working `{{ postcard.image.url }}` should work properly, but it's not pointing to the right URL. I think the AWS region has something to do with it.
Added line in settings.py for `AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME` which seems to remove the sensitive data on the URL for the file.
I then hardcoded the region into the AWS_S3_CUSTOM_DOMAIN like so `AWS_S3_CUSTOM_DOMAIN = '%s.s3.us-east-2.amazonaws.com' % AWS_STORAGE_BUCKET_NAME`. This looks like it works... at least it shows the older files already uploaded. Will continue testing on recently uploaded files.</details>

<details>
<summary>3-21-2020:  </summary>

Took a little break from working on this.  
At this point, images are being uploaded to AWS S3 properly. Images are also being displayed...but not after you set the file permission in S3 to public. So what happens is that once a user uploads a photo, the image is not displayed.  
I changed the setting of `AWS_DEFAULT_ACL` to `public-read` so that once an image is uploaded, it can be displayed as well. Not sure what the flaws of this approach is, but I only set the public-read permission on files that were uploaded, not on anything else stored on the AWS S3 bucket. I think this app is ok as far as functionality for now. Next would be to clean up the CSS styling a bit more. Specifically, image sizing, footer placement, and responsiveness. Stay tuned.

</details>

<details>
<summary>7-2-2020: </summary>
Removed Sender model. Not gonna use it.
</details>
