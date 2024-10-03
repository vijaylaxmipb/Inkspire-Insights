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

### User Stories

With an emphasis on delivering a seamless user experience, the goal of this project is to provide a comprehensive platform that serves both visitors and registered users. The platform will allow for the development and maintenance of content, present developer profiles, and provide opportunities for interaction.  The following user stories outline the essential functionalities and the rationale behind them.

*************************************
### Developer Stories

- As a **developer**, I want to **create wireframes** so that I can **visually represent the layout and structure of the application.**

- As a **developer**, I want to **design a database schema**  so that I can **efficiently store and manage platform content, ensuring optimal performance, scalability, and flexibility.**

- As a **developer**, I want to **create visually engaging and responsive designs** so that **users can easily navigate the website and access relevant information**.

- As a **developer**, I want to **adopt Agile methodology** so that **I can deliver high quality product that meets the needs of the user.**

- As a **developer**, I want to **install and add basic configurations to Django** so that **I can create a working app**.

- As a **developer**, I want to **deploy to Heroku** so that **I can verify initial set up**.

- As a **developer**, I want to **the platform to load quickly and respond swiftly to user interactions** so that **users can have a seamless experience**.

- As a **developer**, I want to **ensure that all syntax errors are identified and resolved during the code validation process** so that **the code is free from syntax-related issues**.

- As a **developer**, I want to **maintain thorough documentation** so that **code is maintained seamlessly in future**.

- As a **developer**, I want to **ensure that user stories are thoroughly tested** so that **they meet acceptance criteria and deliver the expected functionality**.

- As a **developer**, I want to **deploy the application to Heroku** so that **it is accessible to users online**.

- As a **developer**, I want to **ensure that application meets performance and accessibility standards** so that **provides a seamless experience for all users and performs optimally**.

- As a **developer**, I want to **update my profile information** so that **I can keep my information current and accurate**.


*************************************************************
### Visitor Stories


- As a **visitor**, I want to **visit the developer's GitHub portfolio** so that **I can view their projects and contributions**.

- As a **visitor**, I want to **download the developer's resume** so that I can **review their qualifications and consider them for a position.**

- As a **visitor**, I want to **view the developer's profile** so that I can **learn more about the developer, contact them, and access their portfolio.**

- As a **visitor**, I want the **accessibility features to be improved** so that **to maintain equal access and usability for all users, including those with disabilities.**

- As a **visitor**, I want to **visual elements across the platform to be consistent** so that **I can have a cohesive and pleasant user interface experience**.

- As a **visitor**, I want to **navigate through the platform effortlessly,** so that **I can find relevant sections and features intuitively.**

- As a **visitor**, I want to **utilize advanced display filtering options** so that **content displayed on the platform according to my preferences and requirements.**

- As a **visitor**, I want to **able to register an account** so **I can create an account**.

- As a **visitor**, I want to **provide feedback, report issues, and suggest improvements through a contact form,** so that I can **actively participate in improving the platform and receive support when needed**.

****************************************************

### Registered User Stories

- As a **registered user**, I want to **be able to log in and out of my account** so that **I can use the platform**.

- As a **registered user**, I want to **to be able to reset my password** so that **I do not loose access to my account**.

- As a **registered user**, I want to **manage my profile** so that **I have control of the information held on the platform**.

- As a **registered user**, I want to **create posts** so that **I can upload them on the platform**.

- As a **registered user**, I want to **edit and delete posts** so that **I can maintain the content up-to-date**.

- As a **registered user**, I want to **to be able to comment on posts** so that **provide feedback to authors**.

- As a **registered user**, I want to **to be able to delete and edit comments** so that I can **control my engagement on the platform**.

- As a **registered user**, I want **the ability to interact with posts and comments by liking, un-liking, and favoriting them,** so that I can **engage with content that resonates with me**.


### Admin User Stories

- As an **admin user**, I want **the ability to perform all CRUD (Create, Read, Update, Delete) operations** so that **manually manage, control and edit content**.

- As an **admin user**, I want to **approve comments and posts** so that **I can ensure content quality and appropriateness before it is published**.


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
