# Imperium
By Team Lisan Al Gaib - Leon Belegu, Selma Doganata, Eric Lo

Contributions:
- Selma: Backend
- Leon: Frontend
- Eric: Integration

## About the Project

Imperium is a productivity app with the sole intent of centralizing many useful tools like a notepad, calendar, and to-do list, all into one site for your convenience.


## Built With

Frontend: Bootstrap, React, Next.js

Backend: Flask, SQLAlchemy

Languages: JS, Python

## Getting Started

#### Note: There are a couple of unnecessary files in our project that may impede first-time setup. Consider deleting `/backend/instance/app.db` before running the backend for the first time. Additionally, delete your localhost cookies in case of conflicts. There may be a slight possibility that we've forgotten to include necessary packages to install in either the front or back end.

### Setting up the front end

1. Open a terminal
2. Run `nvm install 20.9.0`
3. Open a terminal
4. Cd to frontend/task-manager/
5. Run `npm install`
6. Run `npm run dev`
7. Visit http://localhost:3000

### Setting up the back end

1. Open another terminal
2. Cd to `backend/`
3. Run `pip install -r requirements.txt`
4. Run `flask --app app run`

# Final Progress
We didn't finish everything we set out to do, and some new ideas popped up while we were developing the project. We originally intended to include a clock feature in our app, but scrapped it. Some new ideas we had were to add a dashboard to the home page and replace the clock section with a notepad section to take some quick notes.

These are our app's features that we accomplished:
- Users can sign up and login.
- Users can create calendars.
- Users can create events for those calendars, which match the color of those calendars. These events are clickable, but not editable.
- Users can select multiple calendars to view and view events for those calendars in a calendar UI.
- Users can create to-do lists.
- Users can create tasks for those to-do lists.
- Users can select singular to-do lists to view and view tasks for those to-do lists.
- Users can check off tasks in to-do lists and view them in a completed section.

These are features we wanted to do, but didn't have time for:
- The dashboard should retrieve and display current and upcoming events and tasks, and also have a quick and dirty notepad widget. Right now, it is hard-coded as a proof-of-concept.
- There is frontend UI to edit, rename, and delete calendars and to-do lists, but this is not integrated to the backend. Support for these operations do exist in the backend, however.
- There is no frontend UI to edit events and tasks, but there is support for these operations in the backend. The reset button on the to-do page doesn't work, either.
- The notepad is not integrated, but it does sorta function on the frontend (it just doesn't persist through refreshes). Support exists on both the frontend and backend, but this isn't integrated.
- The calendar page should feature tasks on their relevant due dates, too.


# Usage

1. Registration or Login: You should automatically be directed to the welcome page. Type in a username and password and you should be good to go. (Third party auth does not work).
2. Signing out: Click the burger button in the top right and click "Sign out" to sign out. The other options in that burger menu do not do anything.
3. Navigating the app: Click any of the buttons on the sidebar to switch pages. Note: the calendar page may take a while.
4. Navigating the calendar: Press "Today" to jump to today. Press "Back" or "Next" to jump back/forward one month/week/day depending on what you select. Click on an event to view it in further detail.
5. Adding a calendar: On the calendar page on the sidebar, click the color picker and choose a color, then enter in a calendar name and press "Add Calendar" to add a calendar to your account. The color of the calendar determines what color events that belong to that calendar show up as.
6. Viewing calendars: On the calendar page on the sidebar, your calendars will be displayed. Check the checkbox next to the calendar you want to view to display its events on the calendar. Note that the three dots beside each calendar display options, and those options have some JS functionality, but they will not change the database.
7. Adding an event: On the calendar page, click on the plus button on the bottom right and select "Add an event" to bring up the event adder UI. Then, specify details about the event and click "Add event". Then the event will show up on the calendar in its color. The "Add a task" button does not do anything.
8. Navigating the to-do list: Press "Todo" on the sidebar.
9. Adding a to-do list: On the todo page on the sidebar, type in a name where it says "New List Name" and then press "Add List" to add a new to-do list.
10. Viewing a to-do list: On the todo page on the sidebar, select one of the radio options to show a to-do list's tasks.
11. Adding a task to a to-do list: On the todo page with a to-do list selected, press the button in the top left that has a circled plus icon to add a task. Note: In the event that an alert does not pop up after submission, you may need to refresh the page for the to-do list to update. This is a bug. Another note: the other two buttons in the top left don't do anything.
12. Completing a task: Check the checkbox next to a task to complete it. Click on the "Show/Hide Completed" button to show/hide completed tasks.
13. Taking notes: You can click on the "Notes" on the sidebar and fill out some notes, but it'll only remember what you wrote on the frontend and will go away next refresh, so this feature is not that finished.



# Breakdown of Rubric Categories

This section is meant to assist the professor in determining what parts of the project exist to fulfill which categories.

- Architecture - MVC: **Done**.
    - The `/backend` folder contains models in the `/backend/models` folder.
    - The `/frontend` folder has server components (acting like controllers to fetch data) and client components (acting like views to display HTML). Inside the `/frontend/task-manager/src/app` folder:
        - Some server components are scattered among `/lib` and `/(pages)` in the `page.js` files.
        - Some client components are scattered among `/components` and `/(pages)` as the non-`page.js` files.
        - Some components are a hybrid between controller logic and view logic, like `sidebarTodo.js`.
- API - API: **Done**.
    - We integrated ZenQuotes API to provide inspirational quotes at the top of the calendar page. This logic is found at `/frontend/task-manager/src/app/(pages)/calendar/page.js` and `/frontend/task-manager/src/app/lib/getRandomQuotes.js`.
- Backend - Database: **Done**.
    - The backend utilizes a SQLAlchemy database, which is a relational database.
- Backend - Python, Flask, 10 API Routes: **Done**.
    - The backend is written in Python and is served with Flask.
    - 10 example API routes (all of them are in the `/backend/routes` folder):
        - `/auth/register` in `auth_routes.py`
        - `/auth/login` in `auth_routes.py`
        - `/auth/secured_route` in `auth_routes.py`
        - `/calendars` (POST) in `calendar_routes.py`
        - `/calendars` (GET) in `calendar_routes.py`
        - `/events` (POST) in `event_routes.py`
        - `/events` (GET) in `event_routes.py`
        - `/calendars/<int:calendar_id>/events` (GET) in `event_routes.py`
        - `/todo_lists` (POST) in `todo_lists_routes.py`
        - `/todo_lists` (GET) in `todo_lists_routes.py`
- Frontend - Framework: **Done**.
    - We use Bootstrap (specifically, `react-bootstrap`) to style our app.
- Frontend - React, React Router, 10 Components, 5 Pages: **Done**.
    - We use React (specifically, Next.js) and Next.js's App Router to handle our routing.
    - 10 example components (split between `/(pages)` and `/components` in the `/frontend/task-manager/src/app` folder):
        - `calendar.js`
        - `todo.js`
        - `notes.js`
        - `BigPlus.js`
        - `EventAdder.js`
        - `Header.js`
        - `sidebar.js`
        - `sidebarCalendar.js`
        - `sidebarTodo.js`
        - `SignUp.jsx`
    - 5 example pages (split between `/(pages)` and `/(nonauth pages)` in the `/frontend/task-manager/src/app` folder):
        - `/welcome/page.js` navigable through `<URL>/welcome`
        - `/home/page.js` navigable through `<URL>/home`
        - `/calendar/page.js` navigable through `<URL>/calendar`
        - `/todo/page.js` navigable through `<URL>/todo`
        - `/notes/page.js` navigable through `<URL>/notes`
- Authentication - Local Strategy: **Done** using **JWT tokens**.
    - We used JWT tokens (added to browser cookies) to authenticate and specify the specific user in our API routes. Look at `/backend/models/user.py`, `/backend/routes/auth_routes`, and `/frontend/task-manager/src/app/lib` to see us use it in action.
- Authentication - Third Party Authentication: **Partially done**.
    - We attempted to integrate 3rd party authentication with Google, and it almost works. We were able to make a "Login with Google" button in our `SignUp.jsx` component, and this button successfully redirects you to a Google login popup, however, once you provide your account information, this causes a CSRF error in our backend that says that the state of the request and response do not match. We weren't able to figure out why this was happening, so we didn't push the finished code to the main branch. (Some of it still exists on `main`, but the developmental code is in another branch.) **However, you can still view this code in the `leon-3` branch.**
- Deployment - Cloud Providers: **Not done**.
    - We didn't have time to deploy our app.
- Testing - API: **Done**.
    - There is testing available for our backend in the `/backend/tests` folder. These do not make use of Python's `UnitTest` library, by the way. They are just regular Python scripts that set up example databases and call the routes.
    - 5 example tests:
        - `test_calendar.py`
        - `test_event.py`
        - `test_notepad.py`
        - `test_task.py`
        - `test_todo_list.py`
- Testing - Client: **Done**.
    - There is testing available for our frontend in the `/frontend/task-manager/e2e/auth.test.js` file. This makes use of Next.js's Playwright library for end-to-end testing and can be run with `npx playwright test`. 
    - 5 example tests:
        - `login error page has an alert`
        - `signout page has an alert`
        - `welcome page doesnt start with an alert`
        - `redirects back to sign in if unauthorized`
        - `login redirects to home`
- Misc - README: **Done**.
    - You're looking at it!
- Bonus - Continuous Deployment: **Not Done**.
    - We didn't have time to look at this.
- Bonus - Continuous Integration: **Done?**
    - When we set up Playwright for Next.js, it created a Github Actions for us at `/frontend/task-manager/.github/workflows/playwright.yml`. We think that we set up continuous integration like this, but we're not sure how to use it.
