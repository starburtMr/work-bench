# Application Overview

This skeleton demonstrates a small team collaboration product using Next.js App Router conventions.

The example domain is intentionally replaceable. It exists to show how route groups, server-capable layouts, client components, authenticated flows, API calls, MSW mocks, tests, and e2e coverage fit together in a reusable frontend skeleton.

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

## App Router Shape

- `src/app` owns layouts, pages, route groups, and providers.
- `src/app/auth` contains authentication routes.
- `src/app/app` contains authenticated product routes.
- `src/app/public` contains public read-only routes.
- `src/features` owns feature behavior used by those routes.

## Get Started

To get started, check [this app's README](../README.md).
