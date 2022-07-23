#BembeChat App

##Description

#### The goal of creating this app was to let users chat with privacy. In other words, give users total control of their data. Users are able to create, update and delete room with associated messages.

####The BembeChat App is a real-time user chat App. It utilizes the WebSocket and channels to establish 2 ways of communication. The App has Rooms and Users. Users have to join the room in order to chat with others. The app does not mine users' data. Again, BembeChat App lets users chat without worrying about their data being mined and sent to Data Brokers and Telemarketers. Users have the decision on who to chat with by opening the room and letting other (well know) users join the conversation. Only the users who have access to the room will know about the conversation.

---

##Brief Example
![Alt Text](https://i.imgur.com/SwMF5Oa.gif)

---

##User Stories
#### I would like the user to be able to:
#### 1. sign up and sign in,
#### 2. sign in to the chat room,
#### 3. Create, Update and Delete/Destroy the room (CRUD),
#### 4. create/send and delete the message,
#### 5. differentiate other users' chats by colors, and
#### 6. sign out.

---

## Technologies Used

#### Technologies below were used in the BembeChat App. Templates, Vanilla CSS, Vanillas JavaScript, BootStrap, Materialize and TailWind were used for the front-end.
#### Django and sql were used  for the backend.
#### WebSocket and channels were employed to establish two-way communication

----

## Installation

#### Below are the steps to start the project.

#### 1. Fork and clone the repository
#### 2. Open command line or VS Code.
#### 3. If you will use VS Code go the termial tab, and "cd" into the project folder.
#### 4. Once you are in the project folder, type "pipenv";, and press "Enter".
#### 5. After the virtual environment has been activated,
#### 6. Type "python3 manage.py runserver". The app should be running.

---

## Known Bugs
#### 1. Users are re-directeed to rooms page instead of the previous page they were in before deleting the message. This has to do with DeleteView with dynamic path/url. To fix this issue, fix the DeleteView class to have dynalic url after deleting the message.
#### 2. The page reload every time there a message is sent. It should no be reloading. This needs to be fixed.

---

## Wireframes

### 1. Welcome Page
#### The welcome page will be the front page
#### It will have a welcoming message and image.
![Welcome page](https://i.imgur.com/zVsYMB5.png)
#### URLs used:
#### https://ibb.co/5KT03qJ
#### https://imgur.com/a/CyjocJR

---

### 2. User Sign Up Page
#### The use will have to register/signup in order to be able to sign in and access other pages of the app.
![Sign Up Page](https://i.imgur.com/MNJMNSB.png)

---

### 3. Sign In Page
#### The user will have to sign in in order to access other pages and join conversations.
![Sign In Page](https://i.imgur.com/p2EnLJZ.png)

---

### 4. Room Creation
#### The will be able to create the room by entering the room name, password and the user's username. After the user's successful sign-in, he/she will be redirected to the room sign-up page. On the signup page, the user will sign up for the room, so others can join him/her.
![Room Creation](https://i.imgur.com/L3S1UAY.png)

### 5. Entering in the room
#### Users will have to enter the information provided by the one who created the room. That is, the "room name" and "room password"
![Room Sign Up Page](https://i.imgur.com/0dztMcM.png)

---

### 6. Room Join
#### On this page, the user will use the information entered when signing up for the room. Every member who will participate will have to successfully sign in the room.
![Room Joining](https://i.imgur.com/hhCetl9.png)

---

#### 7. Chat Board
#### On this page all users who successfully sign in to the room be able to chat. The room will be able to contain two or more than 2 users.
![Two users in the chat room](https://i.imgur.com/BAVgE7Q.png)"
![More than 2 users in the chat room](https://i.imgur.com/avC7jCq.png)

#### 8. The user who created the room will be will be able to edit and delete the room
![Edit the room](https://i.imgur.com/xaO3PYV.png)"
![More than 2 users in the chat room](https://i.imgur.com/uYtFGP0.png)

---

## Stretch Goals
#### I would like to let the user send an image and emojis
#### I would like to add user's status (Online/Offline)
#### I would like the user fto send a voice message

---

## Sources
#### Url: https://icons8.com/megacreator/illustration/628817cbcd75d20019332988
#### https://icons8.com/mega-creator/illustration/62bcd6094b3ea300168d7a97
#### https://www.fluidui.com/editor/live/
#### https://www..imgur.com
#### https://pandao.github.io/editor.md/en.html
#### To remove background: https://www.remove.bg/upload

---

## About Me
#### https://github.com/ShindanoSingi
#### https://www.linkedin.com/in/shindano/