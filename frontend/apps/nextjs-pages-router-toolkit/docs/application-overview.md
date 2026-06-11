# Application Overview

This skeleton demonstrates a small team collaboration product using Next.js Pages Router conventions.

The example domain is intentionally replaceable. It exists to show how thin page entries, `getServerSideProps`, authenticated flows, API calls, MSW mocks, tests, and e2e coverage fit together in a reusable frontend skeleton.

## Example Domain

Users can create teams, join teams, and start discussions with comments.

A team is created during registration when the user does not choose to join an existing team. That user becomes the team admin.

## Data Model

The application contains the following models:

- User: can have one of these roles:
  - `ADMIN` can create, edit, and delete discussions; create and delete all comments; delete users; and edit their own profile.
  - `USER` can edit their own profile and create or delete their own comments.
- Team: has one admin and many users.
- Discussion: represents a topic created by team members.
- Comment: represents messages in a discussion.

## Pages Router Shape

- `src/pages` owns route entries and SSR hooks.
- `src/pages/auth` contains authentication routes.
- `src/pages/app` contains authenticated product routes.
- `src/pages/public` contains public read-only routes.
- `src/app` contains providers, layouts, and page implementation modules.
- `src/features` owns feature behavior used by those routes.

## Get Started

To get started, check [this app's README](../README.md).
