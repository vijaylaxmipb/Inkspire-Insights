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
| As a developer I can choose a colour theme                                                   | A colour theme was chosen for the website as referenced in the [README](./README.md) | <mark>PASS</mark> |

### User Stories

| User Story                                                                                  | Screenshot                                                   | Result           |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | ---------------- |
| As a user I want the website to be responsive so I can view it on multiple devices           | Responsive testing as referenced in the [Responsiveness](./README.md#responsiveness)(./README.md) | <mark>PASS</mark> |
| As a User I can intuitively navigate through the website                                    | Navigation Bar referenced in the [README](./README.md) | <mark>PASS</mark> |
| As a User, I can create an account                                                          | Registration process detailed in the [README](./README.md) | <mark>PASS</mark> |
| As a User, I can access my account                                                          | Profile Edit described in the [README](./README.md) | <mark>PASS</mark> |
| As a User, I can log out                                                                    | Sign Out functionality detailed in the [README](./README.md) | <mark>PASS</mark> |
| As a User, I can view my profile page                                                       | Profile Page details referenced in the [README](./README.md) | <mark>PASS</mark> |
| As a User, I can post an article                                                            | Post article functionality in the [README](./README.md) | <mark>PASS</mark> |
| As a User, I can edit my articles                                                           | Edit Post option explained in the [README](./README.md) | <mark>PASS</mark> |
| As a User, I can create comments                                                            | Comment creation detailed in the [README](./README.md) | <mark>PASS</mark> |
| As a User, I can delete my own comments                                                     | Delete Comment functionality in the [README](./README.md) | <mark>PASS</mark> |
| As a User, I can view content on the home page                                              | Home Page content detailed in the [README](./README.md) | <mark>PASS</mark> |
| As a User, I can view a selected article                                                    | Post Detail Page in the [README](./README.md) | <mark>PASS</mark> |
| As a User, I can view articles in a specific category                                       | Category Page explained in the [README](./README.md) | <mark>PASS</mark> |
| As a User, I can view a user's profile page                                                 | Profile Page description in the [README](./README.md) | <mark>PASS</mark> |
| As a User, I can view my favourites                                                         | Favourites functionality detailed in the [README](./README.md) | <mark>PASS</mark> |
| As a User, I can add articles to my favourites                                              | Toggle Favourites feature explained in the [README](./README.md) | <mark>PASS</mark> |
| As a User, I can view comments on an article                                                | Comments functionality explained in the [README](./README.md) | <mark>PASS</mark> |
| As a Developer, I can ensure consistent styling and theme                                   | Website theme detailed in the [README](./README.md) | <mark>PASS</mark> |
| As a User, I can level up based on the number of posts                                      | Level Up feature described in the [README](./README.md) | <mark>PASS</mark> |
| As a User, I can delete my account                                                          | Delete Account functionality in the [README](./README.md) | <mark>PASS</mark> |
| As a Developer, I can show custom error pages                                               | Error Page details in the [README](./README.md) | <mark>PASS</mark> |
| As a User, I can click on the footer contact social links                                   | Footer social links referenced in the [README](./README.md) | <mark>PASS</mark> |
| As a User, I can initiate contact with the developer                                        | Contact via email described in the [README](./README.md) | <mark>PASS</mark> |

### Admin Stories

| User Story                                                                                  | Screenshot                                                   | Result           |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | ---------------- |
| As a Site Owner, I can perform all CRUD operations in the admin interface                   | Admin CRUD features detailed in the [README](./README.md) | <mark>PASS</mark> |
| As a Site Owner, I can approve user-created content                                          | Approval process explained in the [README](./README.md) | <mark>PASS</mark> |
| As a Site Owner, I can delete user profiles and their content                               | User deletion process in the [README](./README.md) | <mark>PASS</mark> |
| As a Site Owner, I can manage users through the admin interface                             | Admin Content management in the [README](./README.md) | <mark>PASS</mark> |
| As a Site Owner, I can view notifications when performing CRUD operations                   | Notifications feature detailed in the [README](./README.md) | <mark>PASS</mark> |
| As a Site Owner, I can enforce a Code of Conduct                                             | Code of Conduct detailed in the [README](./README.md) | <mark>PASS</mark> |
