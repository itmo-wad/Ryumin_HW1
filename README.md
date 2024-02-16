# Profile Page Project

This project is a simple web application that serves a static profile page about myself. The frontend is created using HTML and CSS, and the backend is implemented using Python Flask.

## Frontend

The frontend profile page includes:
- Heading with my name
- Text introducing myself
- Image of myself

## Backend
### Basic Part

- Serves the static profile page at the default route (/)
- Serves images and CSS files as static resources

### Advanced Part

- Serves the profile page using render_template in Flask
- Serves the profile page at /profile and redirects the default route to it
