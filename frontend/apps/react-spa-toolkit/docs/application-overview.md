# Application Overview

React SPA Toolkit is a reusable work-bench skeleton for authenticated, API-backed React single-page applications. It uses a team collaboration demo domain to show real route, auth, form, API, mock, and test patterns.

A team is created during registration when the user does not join an existing team, and that user becomes the team admin.

The demo domain is replaceable after the skeleton is copied into a real project.

## Data model

The application contains the following models:

- User - can have one of these roles:

  - `ADMIN` can:
    - create/edit/delete discussions
    - create/delete all comments
    - delete users
    - edit own profile
  - `USER` - can:
    - edit own profile
    - create/delete own comments

- Team: represents a team that has 1 admin and many users that can participate in discussions between each other.

- Discussion: represents discussions created by team members.

- Comment: represents all the messages in a discussion.

## Get Started

To get started, check [this app's README](../README.md).
