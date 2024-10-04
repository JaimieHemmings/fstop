# FStops Professional Photography Services

[**Link to the live website**](www.fstops.co.uk)

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
### Project Goals
#### Problems We Are Trying to Solve
#### Internal Stakeholders' Goals
#### Business Model
#### Product Goals
#### User Research
##### Discovery Phase
##### Product Launch - Alpha Testing
##### Product Launch - Beta Testing
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
### Database Design
## Skeleton Plane
### Wireframes
## Surface Plane
### Typography
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