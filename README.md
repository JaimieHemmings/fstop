# FStops Professional Photography Services

[**Link to the live website**](www.fstops.co.uk)

# Project Overview

FStops Photography is a website for a freelance professional photographer. The website allows for superusers to manage and edit the content of the website using the bespoke content management system built to replace the django default admin area.

In addition to the  bespoke content management system, superusers are also able to generate invoices that can be sent to clients and then settled through the clients profile page on the website using Stripe as the payment processor. A special area in content management system allows superusers to now only create invoices, but also view the status of all previously generated invoices.

Finally, the websites contact page also allows users, whether they are signed in or not to submit messages to the site superusers. These messages are then stored in the database and can be viewed and deleted by the superusers.

FStops Photography is my fourth project in the Code Institutes level 5 Diploma in Web Application Development (Full Stack Software Development) accredited by East Kent College.

## Table of Contents

- [User Experience](#user-experience)
  - [Strategy Plane](#strategy-plane)
    - [Project Goals](#project-goals)
        - [Problems We Are Trying to Solve](#problems-we-are-trying-to-solve)
        - [Internal Stakeholders' Goals](#internal-stakeholders-goals)
        - [Business Model](#business-model)
        - [Product Goals](#product-goals)
        - [User Research](#user-research)
          - [Discovery Phase](#discovery-phase)
          - [Product Launch - Alpha Testing](#product-launch---alpha-testing)
          - [Product Launch - Beta Testing](#product-launch---beta-testing)
  - [Scope Plane](#scope-plane)
    - [Feature Planning](#feature-planning)
    - [Content Requirement Planning](#content-requirement-planning)
      - [Content Type: Text](#content-type-text)
      - [Content Type: Images](#content-type-images)
      - [Integrating Content Strategy and SEO](#integrating-content-strategy-and-seo)
    - [User Stories](#user-stories)
  - [Structure Plane](#structure-plane)
    - [Interaction Design](#interaction-design)
      - [User Flow Diagram](#user-flow-diagram)
    -  [Information Architecture](#information-architecture)
      - [Site Map](#site-map)
    - [Database Design](#database-design)
    - [Skeleton Plane](#skeleton-plane)
      - [Wireframes](#wireframes)
    - [Surface Plane](#surface-plane)
      - [Typography](#typography)
      - [Colour Palette](#colour-palette)
      - [Imagery](#imagery)
- [Features](#features)
  - [Future Development, Iteration and Implementation](#future-development-iteration-and-implementation)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Frameworks Used](#frameworks-used)
    - [Databases Used](#databases-used)
    - [Libraries and Packages Used](#libraries-and-packages-used)
    - [Programmes and Applications Used](#programmes-and-applications-used)
    - [Payment Processing Platform Used](#payment-processing-platform-used)
    - [Cloud Application Platforms Used](#cloud-application-platforms-used)
    - [Cloud Storage Services Used](#cloud-storage-services-used)
  - [Testing](#testing)
  - [Bugs, Issues and Solutions](#bugs-issues-and-solutions)
  - [Deployment and Local Development](#deployment-and-local-development)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

# USER EXPERIENCE

## Strategy Plane

The goal of this website is to allow FStops Photography to showcase their portfolio and services in an elegant and aesthetically pleasing manner. This is to assist in the primary goal of generating leads through not only the contact form but also direct enquiries by phone or email.

Additionally, FStops Photography would also like a website in which they are able to highlight unique selling points, establish themselves as an authority in the freelance photography market and generate trust with their userbase by displaying their expertise and skills

### Project Goals

- Generate Leads - The website should encourage customers to contact FStop Photography for bookings, enquiries and consultations

- Showcase Expertise - Provide an opportunity and platform for FStops Photography to display their skills, expertise and versatility

- Increase brand visibility - Ensure the site ranks well in search results for local photography services

- Highlight Unique Selling Points - Allow the owner to highlight and distinctive elements in their customer services approach and technical ability by demonstrating their knowledge and previous work

- Collect Revenue - being able to take payments for specific amounts, whether it be a deposit or final payment. The fees charged by FStops Photography are as custom as their projects and therefore are unable to do things based on a "one size fits all" fee, therefore the amount charged for each project needs to be unique. Allowing the option to request and make payments through the website helps establish a more professional brand.

#### Problems We Are Trying to Solve

- Problem 1: FStops Photography currently has no online brand presence
  - Solution: Establish an online presence primarily by building a relevant website

- Problem 2: FStops photography currently requires cash or bank transfer for all project payments
  - Implementing a payment system through the website using Stripe establishes trust and professionalism

- Problem 3: FStops Photography currently relies purely on word of mouth for generating new leads as they has no search engine presence
  - Use search engine optimization (SEO) techniques to increase search rankings, ensuring the website appears prominently for relevant queries.

- Problem 4: The company currently has no way to communicate the available services
  -  Provide well-structured content that clearly describes each service, highlights unique offerings, and presents details or packages in an easy-to-read format.

- Problem 5: A lack of website may hint at a lack of permanence of the company and cause hesitations in clients when reaching out or booking projects
  - Establishing an online presence with real relatable customer feedback will help to build trust and a sense of professionalism

- Problem 6: No differentiation from competitors: The photography market is competitive, and FStop needs a way to stand out among other local photographers.
  - Highlight unique selling points (e.g., specialized equipment, awards, unique styles) prominently throughout the website to set FStop apart from the competition.

- Problem 7: Lead generation and conversion
  - Implement features in the website that make having an account beneficial to the end user, such as the payment system. Additionally a contact form on the website will help to encourage users to enquire about further details and availability.

- Problem 8: Users need to see the quality and versatility of FStop’s photography, but without a well-designed platform, they may not fully appreciate the talent or variety offered.
  - Solution: Create visually appealing galleries organized by category (e.g., weddings, events, portraits), featuring high-quality images to capture users' attention.

#### Internal Stakeholders' Goals

Ultimately the stakeholders goal is generate a return on investment by increasing the amounts of leads and sales they make by the presence of the website enabling additional leads generation and increased visibility via Google. There are a number of other factors that can contribute to this:

- Showcasing quality and style:
  - By showing examples of previous work and generating that "wow" response from the viewer, they are more likely to desire the services rendered by FStops Photography

- Brand Establishment:
  - Individuals and business alike are weary of cowboys who take money and disappear. Hacing a professional website show the business owner has made a significant investment into his company and is more likely to see through any projects that have been undertaken.

- SEO:
  - By establishing an online presence the company becomes more visible. An overwhelming majority of people now instantly turn to Google when they need a product or service so by becoming readily apparent in the search results you increase the likelihood of a sale.

By aligning the website design and content with these stakeholders goals I can create a website that effectively meets the expectations of the client and staisfy expectations.

#### Business Model

The business model of FStops Photography is primarily service based. Key elements of this include:

- Session Fees: Garnered for the rendering of services. A wedding shoot and associated image editing for example.
- Add ons: Generated via upsells such as prints and albums

#### Product Goals

- Reliability, quality and effectiveness as evidenced by user reviews and portfolio examples
- Client-centric approach. Again evidenced by user reviews, additional supplemental information regarding this can be established by an FAQ section

#### User Research

It is important to understand who the end user of the website would be in order to more appropriately target and connect with them. Like any business, it is crucial to understand the target market and align your goals and values with them.

The services rendered by FStops Photography are wide and varied, resulting in a similar client base including couples (wedding photography), small to medium enterprises (Product and Property photography) and young parents (Portrait photography of newborn babies). For this reason it is important to understand that the target demographic is essentially everybody.

For this reason I have opted to keep the style simple yet elegant so as to be attractive and enticing to the majority of users. You can't ever please everyone but you can still try.

The one thing all visitors have in common will be that they are looking for a freelance photographer. For this reason I will implement Google Analytics. This will allow us to closely monitor the bounce rate and most accessed webpages. In conjuction with a blog FStops Photography will be able to tailor the content on the website to best align with the needs of its users encouraging greater engagements rates.

##### Product Launch - Alpha Testing

Alpha Testing is the earliest stage of software testing carried out to identify and fixing crucial bugs in code and ensure optimal functionality of the core components of an application before it is roled out to a wider audience.

###### Purpose

The purpose is generally to identify any major bugs such as broken links, misaligned elements or performance issues. Additionally all core features of the software should be thoroughly tested to ensure any invalid inputs are handled correctly or to prevent the ability to input incorrect data in the first place. Finally, one would assess the basic user journey to ensure that the software application can be navigated and used by end users without any major issues and complete key tasks successfully.

###### Methods

Alpha testing is usually conducted by internal stakeholders of the project, typically the development team or in some cases with larger companies a dedicated software testing team using a test version of the software rather than the production code itself. Testing can be done either manually or by implementing automatic methods, both have their pros and cons.

In my case with FStops Photography I will be implementing unit tests to ensure smooth functionality of the website and it's code as well as manual testing by gathering friends and family to use the website and gather their feedback.

Automatic testing has several pro's compare to manual testing. It is much more efficient and faster resulting in quicker cycles of development between test stages, test scripts can also be rapidly refactored or extended upon to account for additional functionality and reduce the likelihood of human error.

In contrast, manual testing can testing for things that will be missed by automatic testing. For example, errors in usability or design will be missed by automatic testing. Manual testing is also generally cheaper and far more flexible.

##### Product Launch - Beta Testing

Upon identifying and resolving as many issues as possible from the alpha test, the website will then go into beta testing. This is typically done by making the product available in limited amounts to the general public. Either by allowing access for short periods of time or by limiting the number of users who can get access.

In my case I will make the website available to other students in my cohort on the Course I am currently undertaking and request their feedback.

## Scope Plane

### Feature Planning

### Content Requirement Planning

#### Content Type: Text

#### Content Type: Images

#### Integrating Content Strategy and SEO

### User Stories

## Structure Plane

### Interaction Design

#### User Flow Diagram

### Information Architecture

#### Site Map

![Sitemap Visualisation](docs/sitemap-vis.jpg)

Sitemap generated by [Visual Site Maps](https://app.visualsitemaps.com)

### Database Design

## Skeleton Plane

### Wireframes

## Surface Plane

### Typography

I decided not to implement any additional custom fonts for a number of reasons.

- Reduced number of HTTP requests, thereby reducing load times.
- Reduced blocking time
- Improved core web vitals relating to Largest Contentful Paint and Cumulative Layout Shifts etc.
- Fewer FOUT's (Flash of unstyled text)
- Consistent rendering - system fonts are already installed on users devices which guarantees consistent rendering
- Fewer fallback issues in terms of design consistency in case a font fails to load
- SEO improvements relating to the improved core web vitals

I have instead decided to opt for the default use of "Futura" as this already is aesthetically fitting to the rest of the design and have chosen some other fonts as a safe fallback for edge cases where "Futura" does not load for any reason.

![Futura Font Example](docs/futura.png)

### Colour Palette

The website mainly uses a dark theme with highlights of red, as much as possible I made sure to accomodate users with vision impairments or accessability needs by referencing various accessibility check tools online such as Lighthouse and a11y.

![Colour Palette](docs/colour-palette.png)

### Imagery

- Imagery used across the site was sourced either from [Unsplash](https://unsplash.com/) or provided by my brother in law.

# Features

## Future Development, Iteration and Implementation

## Technologies Used

### Languages Used

- HTML - For the front end document structure

- CSS - for the front end styling of the website

- JavaScript - for manipulating dom elements

- Python - for the back end programming of the web site

### Frameworks Used

[django](https://www.djangoproject.com/) - An opensource framework built with Python, based on an MVT (Model, View, Template) model

[Bootstrap5](https://getbootstrap.com/) - Used as a foundation for the visual styling of the website

### Databases Used

- [SQLITE3](https://docs.djangoproject.com/en/5.1/ref/databases/#sqlite-notes) - Used as the database in development

- [Heroku PostgreSQL](https://devcenter.heroku.com/articles/python-concurrency-and-database-connections) - Used as the production server for the live environment

### Libraries and Packages Used

- [django-allauth](https://django-allauth.readthedocs.io/en/latest/) - Used to rapidly integrate prefunctioning account authentication and registration functionality

- [gunicorn](https://gunicorn.org/) - gunicorn is a WSGI HTTP server built with python.

- [pillow](https://pypi.org/project/pillow/) - Used to enable django forms to handle images

- [psycopg2](https://pypi.org/project/psycopg2/) - A database adapter used in python applications to provide compatibility with PostgreSQL databases

- [boto3](https://pypi.org/project/boto3/) - An Amazon SDK used to provide compatibility with AWS buckets

- [pip](https://pip.pypa.io/en/stable/) - a python package manager allowing the easy use and management of packages within a project

- [django storages](https://django-storages.readthedocs.io/en/latest/) - custom storage backends for django, used to more easily integrate the application with AWS functionality

- [Flowbites Icons](https://flowbite.com/icons/) - use for various icons around the website

- [Bootstrap5](https://getbootstrap.com) - For the basic styling library used as the foundation for the websites styling

- [AdminKit](https://adminkit.io/) - Was used to style the control panel of the website.

- [SwiperJS](https://swiperjs.com/) - Used for the carousel upon which the client reviews are based

### Programmes and Applications Used

- [Real Favicon Generator](https://realfavicongenerator.net/) - used to create the site's favicon

- [Git](https://git-scm.com/) - used for version management

- [GitHub](https://github.com) - use for hosting the projects git repository

- [Firefox Inspector](https://www.mozilla.org/en-GB/firefox/new/) - used to aid in debugging and testing compatibility

- [Chrome Dev Tools](https://www.google.com/intl/en_uk/chrome/) - used to aid in debugging and testing compatibility

- [Photoshop](https://www.adobe.com/uk/products/photoshop.html) - Used for the editing of image sizes and formats

- [a11y](https://webaim.org/resources/contrastchecker/) - Used to check for accessibility issues relating to contrast

- [Lighthouse](https://pagespeed.web.dev/) - used to check site performance and compatibility

### Payment Processing Platform Used

- [Stripe](https://stripe.com/gb/payments) - Used for integrating payment functionality to the website

### Cloud Application Platforms Used

- [Heroku](https://www.heroku.com) - Was used for the hosting and deployment of the production website. Through development and deployment I have ensure the version deployed to Heroku is the same as the development codebase as it deploys directly from this repo on GitHub whenever a change is committed.

- [Cloudflare DNS](https://www.cloudflare.com/) - Was used for Domain Name Server management.

### Cloud Storage Services Used

- [Amazons AWS S3 Buckets](https://aws.amazon.com/) - were used for the hosting of static and media files

## Testing

Please reference the [Testing.md](TESTING.md) document for an overview of bugs and solutions

## Bugs, Issues and Solutions

Please reference the [Testing.md](TESTING.md) document for an overview of bugs and solutions

## Deployment and Local Development

Please refer to the [Deployment.md](DEPLOYMENT.md) document for a detailed overview of the deployment process as well as:

- How to Clone
- How to Fork

## Credits

 - [ChatGPT](https://openai.com/chatgpt/) - ChatGPT was used to generator placeholder text during the initial development of the website.

- [ChristopherGS](https://christophergs.com/blog/django-sitemap-tutorial-for-humans) - For a handy tutorial on how to implement sitemaps in the Django Framework

 - [CloudConvert](https://cloudconvert.com/) - Used to convert images to various formats as necassary

 - [TinyPNG](https://tinypng.com/) - Used to compress png images

## Acknowledgements

A big thank you to my mentor, Brian Macharia, for his guidance and support for the duration of this project and a special mention to the team at Code Institute for there amazing, insightful and engaging learning platform and additional support and guidance obtained through the tutoring team. And finally, to the team at East Kent College, especially Rachel Furlong for the guidance and support I received from them all.

# Copyright

&copy; F. Photography by Jaimie Hemmings