# Language Learning Application

## Layout 
Figma project layout:  `https://www.figma.com/design/IwCTsNBYY5zBoNYkyDxnG7/STRONA-DO-%E2%80%A8NAUKI-JĘZYKA?node-id=0-1&t=UefnEItjN9lc1m8n-1`

## Introduction
This project presents a language learning application that allows users to learn new words and review known ones by typing their translations after registering.

## Technologies
- Django
- HTML
- CSS
- JavaScript

## Setup
To set up the project, follow these steps:
1. Install Django using the command: `pip install django`
2. Start the development server: `python manager.py runserver`
There is possibility to create admin: `python manager.py createsuperuser` 

## Functionalities
1. The application includes a built-in Polish-English dictionary.
2. Capability to add new users.
3. All words are marked as "unknown" for new users.
4. In the option to learn new words, users can mark a word as "known".
5. The review functionality displays words previously marked as "known" by the user, along with a text field for typing their translations.

## Purpose of the Application
This application was created to familiarize with the Django framework and basic database relationships.

## Future Plans
Future updates will include additional functionalities for word repetition and introducing other languages.

