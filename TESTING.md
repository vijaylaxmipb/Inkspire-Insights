# Table of Contents

- [User Story Testing](#user-story-testing)
- [Code Validation](#code-validation)
  - [HTML](#html)
  - [CSS](#css)
  - [JavaScript](#JavaScript)
  - [Python](#python)
- [Responsiveness](#Responsiveness)
- [Browser Testing](#browser-testing)
- [Device Testing](#device-testing)
- [Lighthouse](#Lighthouse)
- [Manual Testing](#manual-testing)

  - [Site Navigation](#site-navigation)
  - [Home Page](#home-page)
  - [Category Page](#category-page)
  - [Article Preview Card](#article-preview-card)
  - [Post Detail Page](#post-detail-page)
  - [Comment](#comment)
  - [Add Post Page](#add-post-page)
  - [Edit Post Page](#edit-post-page)
  - [Delete Confirmation Modal](#delete-confirmation-modal)
  - [Profile Page](#profile-page)
  - [Update Profile Page](#update-profile-page)
  - [Sign Up Page](#sign-up-page)
  - [Sign In Page](#sign-in-page)
  - [Log Out Page](#log-out-page)
  - [Code of Conduct Page](#code-of-conduct-page)

- [Bugs](#bugs)

## User Story Testing

### Developer Stories

| User Story                                                                                  | Screenshot                                                   | Result           |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | ---------------- |
| As a developer I can setup a new Django project                                              | The project was set up successfully                           | <mark>PASS</mark> |
| As a developer I can connect database and media storage                                      | Database and storage set up successfully                      | <mark>PASS</mark> |
| As a developer, I can perform an early deployment of the application                         | Live site was hosted with no errors                           | <mark>PASS</mark> |
| As a developer I can layout wireframes                                                       | Wireframes were planned and created as referenced in the README| <mark>PASS</mark> |
| As a developer I can choose a colour theme                                                   | A colour theme was chosen for the website as referenced in the README | <mark>PASS</mark> |

### User Stories

### Developer Stories

| User Story                                                                                  | Screenshot                                                   | Result           |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | ---------------- |
| As a developer I can setup a new Django project                                              | The project was set up successfully                           | <mark>PASS</mark> |
| As a developer I can connect database and media storage                                      | Database and storage set up successfully                      | <mark>PASS</mark> |
| As a developer, I can perform an early deployment of the application                         | Live site was hosted with no errors                           | <mark>PASS</mark> |
| As a developer I can layout wireframes                                                       | Wireframes were planned and created as referenced in the [README](./README.md) | <mark>PASS</mark> |
| As a developer I can choose a colour theme                                                   | A colour theme was chosen for the website as referenced in the [Colour Sceme](./README.md#colour-scheme) | <mark>PASS</mark> |

### User Stories

| User Story                                                                                  | Screenshot                                                   | Result           |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | ---------------- |
| As a user I want the website to be responsive so I can view it on multiple devices           | Responsive testing as referenced in the [Responsiveness](./README.md#responsiveness) | <mark>PASS</mark> |
| As a User I can intuitively navigate through the website                                    | Navigation Bar referenced in the [Colour Scheme](./README.md#colour-scheme) | <mark>PASS</mark> |
| As a User, I can create an account                                                          | Registration process detailed in the [Register](./README.md#user-account-pages) | <mark>PASS</mark> |
| As a User, I can access my account                                                          | Profile Edit described in the [Sign in](./README.md#user-account-pages) | <mark>PASS</mark> |
| As a User, I can log out                                                                    | Sign Out functionality detailed in the [Log out view](./README.md#user-account-pages) | <mark>PASS</mark> |
| As a User, I can view content on the home page                                              | Home Page content detailed in the [Content](./README.md#contents) | <mark>PASS</mark> |
| As a User, I can view a selected article                                                    | Post Detail Page in the [Article Preview Card ](./README.md#article-preview-card) | <mark>PASS</mark> |
| As a User, I can view comments on an article                                                | Comments functionality explained in the [Comment](./README.md#comment-card) | <mark>PASS</mark> |
| As a User, I can click on the footer contact social links                                   | Footer social links referenced in the [Footer](./README.md#footer) | <mark>PASS</mark> |

### Admin Stories

| User Story                                                                                  | Screenshot                                                   | Result           |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | ---------------- |
| As a Site Owner, I can perform all CRUD operations in the admin interface                   | Admin CRUD features detailed in the [README](./README.md) | <mark>PASS</mark> |
| As a Site Owner, I can approve user-created content                                          | Approval process explained in the [README](./README.md) | <mark>PASS</mark> |
| As a Site Owner, I can delete user profiles and their content                               | User deletion process in the [README](./README.md) | <mark>PASS</mark> |
| As a Site Owner, I can manage users through the admin interface                             | Admin Content management in the [README](./README.md) | <mark>PASS</mark> |
| As a Site Owner, I can view notifications when performing CRUD operations                   | Notifications feature detailed in the [Notification](./README.md#notification-messages) | <mark>PASS</mark> |

## Code Validation

### HTML

All HTML pages were run through the [W3C HTML Validator](https://validator.w3.org/). See results in below table.

| Page            | Validator                                                                                     | Result              |
| --------------- | --------------------------------------------------------------------------------------------- | ------------------- |
| Home            | <details><summary>Inksight</summary><img src="./static/images/inksight.png"></details>                                   | <mark>ERROR</mark>   |
| Home     | <details><summary>Home</summary>><img src="./static/images/home_w3c.png"></details>                            | <mark>PASS</mark>   |
| About       | <details><summary>about</summary><img src="./static/images/about_w3c_error.png"></details>                                | <mark>ERROR</mark>   |
| Sign In    | <details><summary>Sign In</summary><img src="./static/images/sign_in_w3c.png"></details>                           | <mark>ERROR</mark> |
| Sign Up         | <details><summary>Sign Up</summary><img src="./static/images/sign_up_w3c.png"></details>                                     | <mark>PASS</mark>   |
| Log Out         | <details><summary>Log Out</summary><img src="./static/images/logout_w3c.png"></details>                                     | <mark>PASS</mark>   |

