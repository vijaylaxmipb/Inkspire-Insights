# The Inkspire Insights

# Contents
- [Agile Methodology](#agile-methodology)
  * [Overview](#overview)
  * [GitHub Projects](#github-projects)
  * [User Stories](#user-stories)
  * [Developer Stories](#developer-stories)
  * [Visitor Stories](#visitor-stories)
  * [Registered User Stories](#registered-user-stories)
  * [Admin User Stories](#admin-user-stories)
- [Website Goals and Objectives](#website-goals-and-objectives)
- [Target Audience](#target-audience)
- [Wireframes](#wireframes)
- [Database Schema](#database-schema)
- [Design Choices](#design-choices)
  * [Typography](#typography)
  * [Colour Scheme](#colour-scheme)
  * [Images](#images)
  * [Responsiveness](#responsiveness)
- [Security Measures and Protective Design](#security-measures-and-protective-design)
  * [User Authentication](#user-authentication)
  * [Password Management](#password-management)
  * [Form Validation](#form-validation)
  * [Database Security](#database-security)
- [Features](#features)
  * [Header](#header)
  * [Footer](#footer)
  * [Landing Page](#landing-page)
  * [User Account Pages](#user-account-pages)
  * [Profile Page](#profile-page)
  * [Add Insight](#add-insight)
  * [Edit Insight](#edit-insight)
  * [Delete Insight](#delete-insight)
  * [Pending Approvals](#pending-approvals)
  * [Insight Card](#insight-card)
  * [Browse Insights](#browse-insights)
  * [Insight Details](#insight-details)
  * [User Interactions](#user-interactions)
  * [Custom Error Pages](#custom-error-pages)
- [Django Admin Portal](#django-admin-portal)
- [Future Features](#future-features)
    + [Enhanced User Profiles](#enhanced-user-profiles)
    + [Advanced Insights Management](#advanced-insights-management)
    + [Community Interaction](#community-interaction)
    + [Content Discovery](#content-discovery)
    + [Accessibility and Inclusivity](#accessibility-and-inclusivity)
- [Deployment](#deployment)
  * [To deploy the project to Heroku](#to-deploy-the-project-to-heroku)
  * [To fork the project](#to-fork-the-project)
  * [To clone the project](#to-clone-the-project)
- [Testing](#testing)
- [Technology](#technology)
  * [Languages](#languages)
  * [Frameworks](#frameworks)
  * [Python Libraries](#python-libraries)
  * [Programs](#programs)
- [Credits](#credits)
- [Disclaimer](#disclaimer)


## Agile Methodology

### Overview

Agile methodology is a project management approach that emphasizes flexibility, collaboration, and iterative progress towards a well-defined goal. It is particularly effective in software development where requirements and solutions evolve through the collaborative effort of self-organizing cross-functional teams. Agile methodologies aim to deliver small, incremental changes in a product to improve quality and adaptability to changing needs.

### GitHub Projects

Using GitHub Projects, tasks are managed and progress tracked through project boards. In this project represents a key aspect of the platform's development and ensures comprehensive coverage of the required functionalities.

- Github: [Github Projects](https://github.com/users/vijaylaxmipb/projects/6/views/1)

## User Experience

### User Stories




With an emphasis on delivering a seamless user experience, the goal of this project is to provide a comprehensive platform that serves both visitors and registered users. The platform will allow for the development and maintenance of content, present developer profiles, and provide opportunities for interaction.  The following user stories outline the essential functionalities and the rationale behind them.

*************************************

#### New User

1. As a user I want the website to be responsive so I can view it on multiple devices.
2. As a User I can intuitively navigate through the website so that I can view all content with ease. 
3. As a User, I can create an account so that I can post, save and edit content.
4. As a User, I can log out so that I can secure my account from potential hacks.
5. As a User, I can post an article so that I can share my insights with the community.
6. As a User, I can create comments on articles, so that I can engage with the content and share my thoughts. 
7. As a User, I can delete my own comments, so that I can remove unwanted opinions. 
8. As a User, I can view content on the home page so that I can stay informed and explore engaging topics.
9. As a User, I can view a selected article with its comments, as well as related articles, so that I can explore in-depth content and engage with the community. 
10. As a User, I can filter articles to a specific category, so that I can explore content that interests me. 
11. As a User, I can view a user's profile page, displaying their posts, favourites and basic information so that I can learn more about the user and their contributions. 
12. As a User, I can add articles to my favourites so that I can save my most enjoyed articles for future reference. 
13. As a User I can see notification messages when performing CRUD operations or login/logout, signup so that informed about the outcome of the action taken. 
14. As a User, I want to view comments on an article so that I can see the discussions going on a particular topic. 


*************************************************************

#### Existing User

1. As a User, I want to be able to log in and out of my account so that I can use the platform
2. As a User, I want to to be able to reset my password so that I do not loose access to my account.
3. As a User, I want to manage my profile so that I have control of the information held on the platform.
4. As a User, I want to create posts so that I can upload them on the platform. 
5. As a User, I want to edit and delete posts so that I can maintain the content up-to-date.
6. As a User, I want to be able to comment on posts so that **provide feedback to authors.
7. As a User, I want to be able to delete and edit comments so that I can control my engagement on the platform.
8. As a User, I want the ability to interact with posts and comments by liking, un-liking, and favoriting them,so that I can engage with content that resonates with me.
9. As a User, I want to see a user-friendly interface when I have no posts or favourites on my profile page. Additionally, I want to have an option to easily add new content. 

****************************************************

#### Website Owner/Developer

1. As a developer I can layout wireframes so that I have a clear idea of the sites structure and theme 
2. As a Developer I can choose a colour theme so that all pages have a consistent feel and style 
3. As a Developer, I can created a standardised article preview card for each article, providing key information at a glance so that users can quickly understand the context of an article 
4. As a Site Owner, I can have the capability to perform all CRUD (Create, Read, Update, Delete) functionality within the website's admin interface so that I can manually create and edit content. 
5. As the Site Owner, I can approve user created content so that I can manually oversee and manage content creation and edits. 
6. As a Site Owner, I can delete user profiles and all associated content from the platform so I can minimise harmful users.
7. As the Site Owner, I can view users and their profiles/content through the website's admin interface, allowing me to manage site users. 
8. As a Developer, I want to ensure the styling and theme of the website are consistent, free from CSS errors, and provide an intuitive and easy-to-use UI/UX so that users easily digest content and perform all actions with ease. 
9. As a Developer, I can show custom error pages redirect the user to the home page, so that I have a consistent experience even when encountering errors on the website. 
10. As a Developer,I want to ensure that user stories are thoroughly tested so that they meet acceptance criteria and deliver the expected functionality.
11. As a Developer,I want to deploy the application to Heroku so that it is accessible to users online.


****************************************************


### Admin User Stories

- As an admin user, I want the ability to perform all CRUD (Create, Read, Update, Delete) operations so that manually manage, control and edit content.

- As an admin user, I want to approve comments and posts so that I can ensure content quality and appropriateness before it is published.


## Website Goals and Objectives

* Enhance User Experience:
    - Develop a user-friendly interface that is easy to navigate and visually appealing.
    - Ensure the platform is responsive and accessible on all devices.

* Facilitate Developer Showcase:
  -  Allow registered users to create, edit, and manage posts and comments.
  -  Implement features that encourage user interaction, such as liking and favoriting content.

* Support Continuous Improvement and Scalability:
  - Adopt Agile development practices to continuously deliver high-quality features.
  - Design the database and infrastructure to handle growth and increased user activity.

* Ensure Security and Reliability:
  - Implement robust authentication and authorization mechanisms.
  - Regularly validate and test the code to maintain a stable and secure application.

* Encourage Community and Feedback:
  - Provide mechanisms for users to give feedback, report issues, and suggest improvements.
  - Actively engage with user feedback to improve the platform continuously.

* Encourage Collaboration:
  - Provide shared knowledge and collective effort

## Target Audience

- Developers
- General Visitors
- Families and Educators

[Back to top](#contents)

## Database Schema

The database schema outlines the structure and relationships between key tables for the platform. The **User** table stores basic user information and authentication details. The **Post** table manages user-generated content with fields for title, content, author, and metadata. The **Comment** table handles comments on posts, including author information. These tables are designed to ensure efficient data management and robust user interactions on the platform.

This schema was generated using [dbdiagram.io](https://www.lucidchart.com)

![Database Schema](/static/images/database%20schema.PNG)

[Back to top](#contents)

## Design Choices

### Typography

 [Roboto](https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap) was chosen as the primary font to enhance the reading experience and align with the blog's nature-themed aesthetic. Its design features make it highly legible on both screens and printed materials, which is crucial for ensuring that readers can comfortably engage with the contentinspirational gardening stories. This font's traditional yet. By using Roboto, I aim to deliver content that is not only visually appealing but also easy to read, thereby enhancing the overall user experience.

### Colour Scheme

The color scheme aims to create a  the vibrant, nature-inspired elements,reliable tone needed for the about section. By combining these carefully chosen colors, I aim to deliver a visually appealing and user-friendly experience.

![Coolors Scheme](/static/images/colour.png)

| color          |  Hex Code  |  usage
|----------------|------------|---------------------                         
|Primary Color   |#E84610     |This bright red-orange color can be used for attention-grabbing elements like buttons,            
|Secondary Color |#0f3f86     |A deep blue that works well for headings, titles, or branding elements like the logo      
|Background Color|#f8f9fa     |A very light grayish-white, used as a general background color for the body or container elements.            
|Accent Color:1  |#445261     |This muted dark slate gray is ideal for section backgrounds, footer areas, or sidebar navigation.
|Accent Color:2  |#b0b0b0     |Use this as a secondary text color or for borders and dividers. 
|Teal Accent     |#188181     |This deep teal works great for icons, links, or hover effects.It's a fresh, calm color that adds visual interest without being too bold, complementing the rest of the color scheme.
|Bright Cyan     |#23BBBB     |A bright and modern cyan color, useful for hover effects, secondary buttons, or interactive elements.
|Soft Colour     |#F9FAFC     |This very light blue-gray color can be applied to the background of cards, forms, or input fields. 

[Back to top](#contents)

### Images

Combination of images sourced from Pexels(https://www.pexels.com/).
All images are provided under the [Pexels License](https://www.pexels.com/license/), allowing free use for personal and commercial purposes, with no attribution required. However, crediting the photographers is appreciated.

[Back to top](#contents)

### Responsiveness

My website is responsive to different layouts depending on the size of the viewport have been included in the CSS media queries. This allows visitors to experience the website as I intended on device types and screen sizes. The breakpoints I am using are from Bootstrap.

![Breakpoints](/static/images/am_i_responsive.png)

[Back to top](#contents)

## Security Measures and Protective Design

### User Authentication

- The application uses Django's built-in authentication system to manage user access.
- Logged-in users can post comments, and the system allows for post and event management through standard Django views.
- Users must be logged in to submit comments. However, the system currently does not enforce login requirements for viewing posts or events.

## Comment Management

- Users can add comments to posts. The comments are associated with specific posts and are displayed in the post detail view.
- After submitting a comment, the comment is saved and set to await approval by an admin/moderator before being displayed publicly.
- **Edit and Delete Functionality**: There is no explicit enforcement of user-specific permissions on editing or deleting comments in the current implementation. However, the views handle comment editing and deleting through form submission, with logic in place to compare the comment author with the logged-in user. If the logged-in user is the author of the comment, they are allowed to edit or delete the comment.

## Post and Event Management

- The application includes a list of posts and events.
- The posts and events are displayed using Django's `ListView`, and users can view individual post or event details.
- **Post Detail View**: This view displays a single post along with all the comments associated with it. The post detail view also includes the ability to submit a new comment.
- The system currently does not enforce role-based permissions for viewing posts or events.

### Password Management

- Use Django's built-in password management tools to ensure passwords are hashed and stored securely.
- Enforce strong password policies to enhance user account security.
- Users can log in and out of their accounts via Django's authentication system.

### Form Validation

If incorrect or empty data is added to a form, the form won't submit, and a warning will appear to the user informing them which field raised the error.

### Database Security

- The database URL and secret key are stored in the `env.py` file to prevent unwanted connections to the database. This setup was implemented before the first push to GitHub.
- Cross-Site Request Forgery (CSRF) tokens are used on all forms throughout the site to enhance security.
- The application uses a PostgreSQL database, manually configured in the `settings.py` file due to an error where the default database was not being detected or displayed properly.

[Back to top](#contents)

## Features

### Header

![Visitor Large Screen](/static/images/Header.png)

The header of the Inkspire Insights Blog is designed to be both visually appealing and user-friendly. It features a navigation menu, user authentication links, and a search bar. The cohesive color scheme, incorporating primary, secondary, and background colors, ensures a visually harmonious design while maintaining accessibility with strong color contrast and ARIA labels for screen readers.
The responsive design adapts seamlessly to both desktop and mobile devices, ensuring that the navigation remains intuitive and fully functional across all screen sizes. 

### Footer

![Footer](/static/images/footer.png)

The footer maintains consistency with the overall site design, featuring the same font and color scheme, and is fully responsive to adapt to various screen sizes. This attention to detail helps reinforce the site's branding and enhances the user experience by providing clear and accessible navigation options at the bottom of the page. Media links are included. Also, users can contact site owner by clicking on the :envelope: icon is they wish to do so. Instead of generic links, the footer includes 'About Section' link with detailed profile of the developeer of this project.


**About Section:**

The About Me section of Inkspire Insights provides detailed information about the blog creator in a visually appealing format. It includes a brief bio where about the developer, shares their passion for creativity, personal growth, and storytelling. The layout focuses on a user-friendly presentation of the developer’s background and inspirations for the blog. The data is managed via the Django Admin Portal, and the system is scalable to support multiple profiles or further enhancements, offering a clean and structured way to access important information about the blog's creator.

![Landing View Large Screen](/static/images/about.png)

 ### Landing Page

The landing page of Inkspire Insights is designed to welcome visitors with a clean, modern, and engaging layout. The page features a series of blog post cards, each displaying the title, excerpt, publication date, and author, making it easy for users to browse and explore the latest insights. The page is structured with a prominent navigation bar at the top, including options for Home, About, Login/Logout, and a search bar for easy content discovery.The blog post cards feature vibrant images, bold headlines, and brief excerpts that draw the user in. The clean typography and ample spacing ensure that the content is easy to read and visually appealing.


![Landing View Large Screen](/static/images/landing%20page.png)

### Search Feature

Implement a search bar in the navigation menu to allow users to search for specific users or articles by entering text, enhancing content discoverability.

### Password Reset with Email Validation

Introduce a secure and user-friendly password reset system that relies on email validation, making it easier for users to regain access to their accounts.


### User Account Pages

The user account pages ensure a smooth and secure process for managing user access, enhancing the overall user experience on Blossom Therapy Insights.

**Sign Up/Registration Page:**

The Sign Up page features a clean and intuitive form where users can create an account by entering their username, first name, last name, email, and password. The form uses a responsive design, ensuring accessibility and ease of use across devices. By prioritizing user-friendly design, the Sign Up page helps facilitate quick and easy registration, encouraging new users to join the community and start their gardening journey.

![Register](/static/images/sign_up.png)

---

**Sign In Page:**

The Log In page offers a straightforward and secure way for existing users to access their accounts. The page includes fields for the username and password, with clear labels and a prominent login button. The page maintains consistency with the site's overall aesthetic, ensuring a cohesive user experience. The focus on simplicity and security helps users quickly and confidently access their accounts to engage with the Inkspire Insight.

![Sign In](/static/images/sign_in.png)

**Log Out Page:**

The Log Out page provides users with confirmation of a successful logout from their account. It features a brief message indicating that the user has been logged out. The design is minimalistic, reinforcing the action taken and providing a clear path to continue exploring the site or logging in again.


![Log Out View](/static/images/log%20out.png)

### Article Preview Card

The Article Card on Inkspire Insight  is a concise yet informative snapshot of a user's post within a specific tech-related category. It includes the following key elements:

1. Author Profile: A visual representation of the author's Profile and username, providing a quick way to identify the content creator.
2. Likes: The number of likes the post has received, offering a sense of its popularity and engagement.
3. Comments: The count of comments on the post, indicating the level of community discussion and interaction.
4. Post Date: The date when the article was published, offering a reference for the recency of the content.
5. Title: The headline of the post, serving as a captivating entry point to the article's content.
6. Excerpt: A brief summary or excerpt from the article, providing users with a glimpse of the post's key points and enticing them to read further.

Together, these elements create a preview Card that is both visually appealing and informative, allowing users to make informed choices about which posts to explore further within a specific category.

![Article Preview Card](/static/images/article_preview_card.PNG)


### Notification Messages

Notification messages were user every time the user performs CRUD operation, sign in, and sign out.
![Notification Messages ](/static/images/notification_messages.png)


### Comment Card

The comment card elegantly showcases the user's comment, the author's identity, and the date
![Comment Card ](/static/images/comment_card.png)

### Awaiting approval

when a user comment for a blog and click on submit button,notification popup for approval from admin.
![Awaiting approval ](/static/images/awating_approval.png)


## Testing