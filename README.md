### Your group members and scrum leader (if applicable) 
N/A

---

### Your project idea 

The BembeChat App will be a real-time user chat App. It will utilize the WebSocket and channels to establish 2 ways of communication. The App will have Rooms/Groups and Users. Users will have to join the group/room in order to chat with others. The app will not mine users' data. The goal is to let users chat with privacy. 

Again, BembeChat App will let users chat without worrying about their data being mined and sent to Data Brokers and Telemarketers. Users will decide on who to chat with by opening the room and letting other (well know) users join the conversation. Only the users who have access to the room will know about the conversation.

---

### Your tech stack (frontend, backend, database)

The front-end will utilize templates: CSS, Vanilla JavaScript, Bootstrap, and Materialize.
The backend will be handled by Django.
WebSocket will be employed to establish two-way communication

---

### List of backend models and their properties

The models.py will have models below:

class Room(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

class Message(models.Model):
    room = models.ForeignKey(Room, related_name = messages, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
 

For the User name, I am going to use the built-in UserCreationForm which will have these fields:

 // This model will be in the forms.py file. Below is the code for the User model. 

Code: 

from django import django.contrib.auth.forms import UserCreationForm
from djanfo.contrib.auth.models import User

class SignUpForm(UserCreationForm):
      class Meta:
      fields = ['username', 'password1', 'password2']


---

### React component hierarchy (if applicable)
N/A

---

### User stories
I would like the  users to be able to
- sign up and sign in,
- sign in to the chat room/group,
- enter their profile pictures,
- see the status of the other users when they are writing, 
- differentiate other users' chats by colors, and
- sign out.

---

### Wireframes

#### 1. Welcome Page
The welcome page will be the front page 
It will have a welcoming message and image.
![Welcome page](https://imgur.com/a/CyjocJR")
URLs used: 
https://ibb.co/5KT03qJ
https://imgur.com/a/CyjocJR

---

#### 2. User Sign Up Page
The use will have to register in order to be able to sign in for accessing other pages of the app.
![Sign Up Page](https://imgur.com/a/cY22GJF)

---

#### 3. Sign In Page
The user will have to sign in in order to access other pages and join conversations.
![Sign In Page](https://imgur.com/a/JWBHGKi)

---

#### 4. Room Sign Up
After the user's successful sign-in, he/she will be redirected to the room sign-up page. On the signup page, the user will sign up for the room, so others can join him/her.
![Room Sign Up Page](https://imgur.com/a/T8fzrHn)

---

#### 5. Room Join
On this page, the user will use the information entered when signing up for the room. Every member who will participate will have to successfully sign in the room.
![Room Sign In Page](https://imgur.com/a/TIUnUMk)

---

#### 6. Chat Board
On this page all users who successfully sign in to the room be able to chat. The room will be able to contain two or more 3 users.
![Two users in the chat room](https://imgur.com/a/EvEmX04)"
![More than 2 users in the chat room](https://imgur.com/a/EvEmX04)

---

### Anything else your squad lead should know
No.
