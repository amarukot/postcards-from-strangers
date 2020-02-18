# Postcards from a Stranger || PO Box Zero

Capstone Project for GA Software Engineering Immersive Course.

The idea is to have a website where users can create anonymous postcards/messages/letters to anyone or no one in particular. These postcards could have any message – inspiration, rants, words of advice, or just anything really. I wanted to keep the sender anonymous so that they can be free to express themselves. I also wanted the 'recipients' to not know the senders to make the messages have more meaning to them and interpret them according to their situation.

## User Stories

[Click here](./planning/USER-STORIES.md)

## Wireframe

[Click here.](https://xd.adobe.com/view/d32d9749-1010-4adf-431a-960db3131c8e-a51c/)

## Technologies, Libraries

Backend: Hasura, Apollo, Pillow, GraphQL, PostgreSQL
Frontend: React, Bootstrap

## Setup

Install dependencies  
`pip3 install -r requirements.txt --yes`

OR

`pip3 install django`  
`pip3 install pscyopg2-binary`  
`pip3 install Pillow`

Create database
`psql -U postgres -f settings.sql`

## Models

Postcard

- image
- style (post MVP?)
- message
- datetimestamp (?)
- Sender (ref)
- Recipient (optional? email? multiple?)

Sender

- Name (any text)
- Postcards - (ref) multiple

## Timetable

| Date   | Task/Milestone | Time Alloted | Actual |
| ------ | -------------- | ------------ | ------ |
| Feb 17 | Documentation  | 1 hr         |        |
|        | Wireframe      | 1 hr         |        |
| Feb 18 | Initial Setup  |              |        |
|        | DB, Models     | 1.5 hrs      |        |
| Feb 19 | Reach MVP      | --           |        |
|        | CRUD functions | 2 hrs        |        |
| Feb 20 | Deployment     | 3 hrs        |        |
| Feb 21 |                |              |        |

## Issues
