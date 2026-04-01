# GreenCamUz Web Platform: Design, Development, and Deployment of a Sustainability-Focused Content Management System for Higher Education

---

## 1. Introduction

### 1.1 Background

The GreenCamUz project — Green Campus Initiative: Integrating Sustainability into Higher Education in Uzbekistan — is an international initiative funded by the European Union under the Erasmus+ Capacity Building in Higher Education (CBHE) Strand 1 framework. The project unites nine partner higher education institutions from Uzbekistan, Poland, Lithuania, and Turkiye, with the shared goal of embedding sustainability principles into academic life across Central Asia.

A central requirement of the project was the development of a dedicated web platform to serve as the primary digital interface for disseminating project activities, showcasing outcomes, managing events and news, and engaging stakeholders across all partner institutions.

### 1.2 Objectives

The GreenCamUz web platform (https://greencam.uz) was designed and developed to fulfill the following objectives:

- Provide a professional, publicly accessible web presence for the GreenCamUz project;
- Enable dynamic content management for news articles, events, programs, and media galleries;
- Support event registration and contact form submissions;
- Showcase partner institutions and downloadable project materials;
- Deliver a responsive, modern user experience across desktop and mobile devices;
- Ensure secure, reliable, and scalable deployment in a production environment.

### 1.3 Scope of This Paper

This paper presents the technical architecture, design decisions, and implementation details of the GreenCamUz web platform. It covers the frontend design system, backend application logic, database schema, deployment infrastructure, and security considerations. The platform was developed using the Django web framework (Python) and deployed on DigitalOcean using Docker containerization with Nginx reverse proxy and PostgreSQL database.

---

## 2. Technology Stack Overview

The GreenCamUz platform is built on a modern, open-source technology stack selected for reliability, maintainability, and ease of deployment. Table 1 summarizes the key technologies used across each layer of the application.

**Table 1: Technology Stack**

| Layer | Technology | Version | Purpose |
|-------|-----------|---------|---------|
| Backend Framework | Django | 4.2 LTS | Web application framework |
| Programming Language | Python | 3.11 | Server-side logic |
| Database | PostgreSQL | 15 | Relational data storage |
| Application Server | Gunicorn | 23.0 | WSGI HTTP server |
| Web Server | Nginx | Alpine | Reverse proxy, SSL termination |
| Containerization | Docker & Docker Compose | — | Application packaging and orchestration |
| SSL/TLS | Let's Encrypt (Certbot) | — | Automated certificate management |
| Image Processing | Pillow | 11.3 | Image handling and validation |
| Frontend | HTML5, CSS3, JavaScript | — | User interface |
| Typography | Google Fonts (Space Grotesk, Inter) | — | Web typography |
| Hosting | DigitalOcean | — | Cloud infrastructure |

The stack was chosen with the following priorities: Django's mature ORM and admin interface accelerate content management development; PostgreSQL provides robust relational storage with strong data integrity; Docker ensures reproducible deployments; and Nginx offers efficient static file serving with SSL termination.

---

## 3. Frontend Architecture

### 3.1 Design System

The frontend follows a custom design system built with vanilla HTML5, CSS3, and JavaScript — without reliance on external CSS frameworks. This decision was made to maintain full control over the visual identity while keeping the payload minimal.

**Color Palette.** The primary color scheme is rooted in green tones (#2e5b15, #4a8c2a), reflecting the project's sustainability theme. Secondary colors include dark grays (#1a1a2e) for backgrounds and near-white (#fafffe) for content areas, creating a modern, high-contrast aesthetic.

**Typography.** Two Google Fonts families are used: Space Grotesk (weights 400–700) for headings and Inter (weights 300–700) for body text. Heading sizes use CSS `clamp()` functions (e.g., `clamp(42px, 6vw, 72px)`) to ensure fluid, responsive scaling across viewport widths.

**Layout System.** Page layouts are built using CSS Grid and Flexbox. Content grids use `repeat(auto-fill, minmax(280px, 1fr))` patterns to create responsive multi-column layouts that automatically adjust from four columns on desktop to a single column on mobile without explicit media queries for each breakpoint.

### 3.2 Responsive Design

The platform implements a mobile-first responsive strategy with primary breakpoints at 768px (tablet) and 1024px (desktop). Key responsive features include:

- **Navigation:** A fixed-position navigation bar with backdrop blur transitions to a hamburger menu on mobile, with a three-line animated toggle and slide-in menu panel.
- **Grid Layouts:** Program cards render in a 4-column grid on desktop, 2-column on tablet, and single column on mobile. News and event cards follow similar responsive patterns.
- **Touch Optimization:** Interactive elements maintain a minimum touch target of 44px, and the partners carousel supports swipe gestures with momentum-based scrolling.
- **Media:** Images use `object-fit: cover` for consistent aspect ratios, and the lightbox modal scales media to `max-width: 90vw; max-height: 80vh` for optimal viewing on any screen size.

### 3.3 Interactive Components

The frontend includes several custom-built interactive components:

**Lightbox Modal.** A full-screen media viewer supporting both images and videos. Users can click any media item in a gallery to open the lightbox, navigate between items using on-screen arrows or keyboard shortcuts (ArrowLeft, ArrowRight, Escape), and view captions below each media item. Videos play with native HTML5 controls and autoplay on open.

**Image Carousel.** The About page features an auto-advancing image carousel with dot indicators, previous/next navigation buttons, and a 4-second rotation interval. The carousel resets its auto-play timer on manual navigation to avoid disorienting transitions.

**Partners Carousel.** An auto-scrolling horizontal carousel for partner logos with both touch (swipe) and mouse (drag) support. The carousel pauses on user interaction and resumes after a 3-second delay, using CSS transform-based sliding for smooth performance.

**Animated Counters.** The homepage features animated statistical counters that increment from zero to their target values over 2 seconds using 60-step linear interpolation. An Intersection Observer triggers the animation only when the counter section enters the viewport, preventing unnecessary computation.

**Animated Background.** Decorative gradient orbs track the cursor position via mousemove events, and floating shapes with staggered CSS animation delays create a subtle, dynamic background effect.

### 3.4 Stylesheet Architecture

The platform's styling is consolidated into a single CSS file (style.css, approximately 4,300 lines) organized into logical sections:

1. Global resets and CSS custom properties
2. Navigation and header styles
3. Hero section and animations
4. Content sections (About, Programs, News, Events)
5. Card components and grid layouts
6. Form elements and input styling
7. Lightbox and modal components
8. Gallery grid and filter buttons
9. Footer and social links
10. Responsive media queries
11. Utility classes and animation keyframes

Key CSS animations include `fadeInUp` (1s ease-out), `gradientMove` (20s infinite), `floatShape` (8s infinite), and `pulse` (3s infinite), contributing to a lively yet professional user experience.

---

## 4. Backend Architecture

### 4.1 Application Structure

The Django backend is organized into seven distinct applications, each responsible for a specific domain of functionality. This modular architecture promotes separation of concerns and independent development of features.

**Table 2: Django Application Modules**

| Application | Models | Primary Function |
|------------|--------|-----------------|
| core | AboutContent, AboutImage, Material | Homepage, static pages, materials |
| programs | Program, ProgramMedia | Environmental program management |
| news | News, NewsMedia | News article management |
| events | Event, EventMedia, Registration | Event management and registration |
| gallery | Gallery | Unified media gallery |
| contact | Contact | Contact form submissions |
| partners | Partner | Partner organization showcase |

### 4.2 Database Schema

The platform uses PostgreSQL 15 as its production database, with SQLite as a development fallback. The schema comprises 13 models across 7 applications.

**Content Models.** The three primary content types — Programs, News, and Events — follow a consistent pattern: a main model containing textual content and metadata, paired with a related media model (ProgramMedia, NewsMedia, EventMedia) linked via foreign key with CASCADE deletion. Each media model supports both image and video types, includes optional captions and ordering fields, and allows designation of a cover image for card displays.

**Gallery Aggregation.** The Gallery model stores standalone media uploads, but the gallery view aggregates content from three sources: the Gallery model itself, NewsMedia (filtered by published news), and EventMedia (filtered by active events). This aggregation is performed at the view level using Django's `values_list()` queries and Python's `itertools.chain()`, with results sorted by creation date and paginated.

**Registration System.** The Registration model implements a unique constraint on (event, email) pairs to prevent duplicate registrations for the same event. Phone validation enforces a minimum length of 9 characters, and email addresses are normalized to lowercase.

**Contact Management.** Contact form submissions are stored with a status workflow (new → in_progress → resolved), managed through the Django admin with color-coded status badges and bulk actions.

### 4.3 URL Architecture

The platform follows RESTful URL conventions with clean, semantic paths. All URLs are organized under their respective application namespaces (e.g., `news:list`, `events:detail`), enabling reverse URL resolution in templates and views. Content detail pages use slugs (Programs, News) or integer primary keys (Events) for identification.

### 4.4 View Layer

Views are implemented as function-based views (FBVs) for simplicity and readability. Common patterns include:

- **List Views:** Query filtered and ordered model instances, apply pagination (6–12 items per page depending on content type), and render to grid-based templates.
- **Detail Views:** Retrieve single objects via `get_object_or_404()`, passing related media through Django's ORM relationship traversal.
- **Form Views:** Handle both GET (display form) and POST (validate and save) requests within a single view function, with success redirects and error feedback.

### 4.5 Admin Interface

The Django admin is extensively customized to provide a content management experience tailored to non-technical users. Customizations include:

- **Inline Editing:** Media files for Programs, News, and Events are managed through tabular inline editors, allowing content creators to upload and organize multiple images and videos directly from the parent object's edit page.
- **Visual Previews:** Image thumbnails and video play icons are rendered in list views using `format_html()`, giving administrators immediate visual feedback without opening individual records.
- **Status Indicators:** Contact submissions display color-coded status badges (green for new, orange for in-progress, gray for resolved) for at-a-glance workflow tracking.
- **Bulk Actions:** Custom admin actions allow marking multiple contact submissions as read or replied in a single operation.
- **List Editability:** Boolean fields (is_published, is_featured, is_active) and ordering fields are directly editable in list views, reducing the number of clicks required for common operations.

---

## 5. Deployment Architecture

### 5.1 Containerization

The application is fully containerized using Docker and Docker Compose, with four services orchestrated together:

1. **web** — The Django application running on Gunicorn (3 workers, 120s timeout), built from a Python 3.11-slim base image with PostgreSQL client libraries.
2. **db** — PostgreSQL 15 with persistent data stored in a Docker volume (`postgres_data`).
3. **nginx** — Nginx Alpine serving as a reverse proxy, handling SSL termination, static/media file serving, and gzip compression.
4. **certbot** — Let's Encrypt certificate manager running renewal checks every 12 hours.

### 5.2 Startup Sequence

The application's entrypoint script (`entrypoint.sh`) implements a sequential startup process:

1. **Database Readiness Check:** A Python socket connection loop polls PostgreSQL on port 5432 until the database accepts connections, preventing Django from attempting migrations against an unavailable database.
2. **Database Migration:** `manage.py migrate --noinput` applies any pending schema changes automatically on each deployment.
3. **Static File Collection:** `manage.py collectstatic --noinput` gathers static assets from all applications into the serving directory.
4. **Application Start:** Gunicorn launches with 3 worker processes bound to port 8000.

### 5.3 Nginx Configuration

Nginx handles three primary responsibilities:

- **SSL Termination:** TLS certificates from Let's Encrypt are loaded for the greencam.uz domain, with HTTP traffic on port 80 redirected to HTTPS on port 443.
- **Static and Media Serving:** Static files are served with 30-day cache headers and immutable directives; user-uploaded media files use 7-day caching.
- **Gzip Compression:** Enabled for text, CSS, JSON, JavaScript, XML, and SVG content types with a minimum threshold of 256 bytes, reducing bandwidth consumption.
- **Reverse Proxy:** All dynamic requests are forwarded to the Gunicorn upstream with appropriate headers (X-Real-IP, X-Forwarded-For, X-Forwarded-Proto) for correct client identification behind the proxy.

### 5.4 Infrastructure

The platform is hosted on a DigitalOcean droplet with the following specifications:

- **Domain:** greencam.uz (with www subdomain)
- **SSL:** Automated Let's Encrypt certificates with 12-hour renewal checks
- **Upload Limit:** 20MB maximum file size for media uploads
- **Environment Configuration:** All sensitive values (SECRET_KEY, database credentials, allowed hosts) are stored in a `.env` file, loaded via `python-dotenv` at runtime.

---

## 6. Security Considerations

The platform implements multiple layers of security following Django best practices and OWASP guidelines:

**Transport Security.** All traffic is encrypted via TLS 1.2+ with Let's Encrypt certificates. HTTP requests are permanently redirected (301) to HTTPS. Session and CSRF cookies are marked as secure-only, preventing transmission over unencrypted connections.

**Cross-Site Request Forgery (CSRF).** Django's built-in CSRF middleware validates tokens on all POST requests. Trusted origins are explicitly configured for the production domain.

**Clickjacking Protection.** The `X-Frame-Options: DENY` header prevents the site from being embedded in iframes on external domains, mitigating clickjacking attacks.

**XSS Protection.** The `X-XSS-Protection` header is enabled, and Django's template engine auto-escapes all variable output by default, preventing cross-site scripting through user-generated content.

**SSL Proxy Headers.** The `SECURE_PROXY_SSL_HEADER` setting trusts the `X-Forwarded-Proto` header from Nginx, ensuring Django correctly identifies HTTPS requests behind the reverse proxy.

**Environment Isolation.** Production secrets are managed through environment variables rather than hardcoded values. The DEBUG flag defaults to False, ensuring detailed error pages are never exposed in production.

**Input Validation.** Form submissions undergo server-side validation including email normalization, phone number length checks, and unique constraint enforcement for event registrations.

---

## 7. Conclusion

### 7.1 Summary

The GreenCamUz web platform demonstrates how modern open-source technologies can be effectively combined to deliver a professional, feature-rich content management system for international academic projects. By leveraging Django's mature ecosystem, Docker's deployment consistency, and a custom-built responsive frontend, the platform provides a reliable digital presence for the GreenCamUz initiative.

Key technical achievements include:

- A modular Django application architecture with seven specialized apps managing distinct content domains;
- A unified gallery system that aggregates media from multiple content sources with source-based filtering;
- A custom responsive frontend with interactive lightbox, carousel, and animation components — built without external CSS/JS frameworks;
- A fully containerized deployment pipeline with automated SSL certificate management and database migrations;
- Comprehensive security measures following Django and OWASP best practices.

### 7.2 Future Development

Several enhancements are planned for subsequent phases of the project:

- **Multilingual Support:** Implementation of Django's internationalization (i18n) framework to serve content in Uzbek, English, and Russian, reflecting the multilingual nature of the consortium.
- **REST API:** Development of a Django REST Framework API layer to support potential mobile applications and third-party integrations.
- **Analytics Dashboard:** Integration of usage analytics to track visitor engagement, event registration rates, and content performance metrics.
- **Search Functionality:** Implementation of full-text search across all content types using PostgreSQL's built-in search capabilities.
- **CI/CD Pipeline:** Automated testing and deployment through GitHub Actions to further streamline the development workflow.

### 7.3 Acknowledgments

The GreenCamUz web platform was developed as part of the GreenCamUz — Green Campus Initiative: Integrating Sustainability into Higher Education in Uzbekistan project, funded by the European Union under the Erasmus+ Capacity Building in Higher Education (CBHE) Strand 1 framework. The project is implemented by nine partner higher education institutions from Uzbekistan, Poland, Lithuania, and Turkiye.

---

**References**

1. Django Software Foundation. (2024). Django Documentation (Version 4.2 LTS). https://docs.djangoproject.com/en/4.2/
2. Docker, Inc. (2024). Docker Documentation. https://docs.docker.com/
3. PostgreSQL Global Development Group. (2024). PostgreSQL 15 Documentation. https://www.postgresql.org/docs/15/
4. Nginx, Inc. (2024). Nginx Documentation. https://nginx.org/en/docs/
5. Let's Encrypt. (2024). Documentation. https://letsencrypt.org/docs/
6. OWASP Foundation. (2021). OWASP Top Ten Web Application Security Risks. https://owasp.org/www-project-top-ten/
7. Gunicorn. (2024). Gunicorn Documentation. https://docs.gunicorn.org/
8. DigitalOcean. (2024). DigitalOcean Documentation. https://docs.digitalocean.com/
