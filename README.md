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
|Secondary Color |#0f3f86     |         
|Background Color|#f8f9fa     |            
|Accent Color:1  |#445261     |
|Accent Color:2  |#b0b0b0     |
|Teal Accent     |#188181     |
|Bright Cyan     |#23BBBB     |
|Soft Colour     |#F9FAFC     |