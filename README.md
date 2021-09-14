# Portfolio 

----

This is [my personal space on the web](https://tech-with.me). Hosted on Amazon AWS


# Screenshots
<p float="left">
  <img src="https://github.com/github-localhost/portfolio/blob/b39074cd0c47b8c791ea7aae0c9ba7d262667d32/image.png" width="400">
  <img src="https://github.com/github-localhost/portfolio/blob/22598e5ec7941273496dfc0eb4e85dfc3b5614f7/image1.png" width="400">
</p>

# Features
- Docker
- Nginx
- Flake8 [will be soon]
- Certbot
- Flask


# How to run?

<code> git clone this-repo </code><br />
<code> cd portfolio </code><br />
<code> ./scripts/init-certbot.sh </code><br />
<code> docker-compose build </code><br />
<code> docker-compose up </code>

# Configuration
edit '.env.dist' for yourself, and rename it to '.env'.
Edit './scripts/init-certbot.sh' to add your domain

Project examples locates at /application/templates/
Static files locates at /application/static

Good luck !

# Todo's

- Clear up code with flake 
- Add Flask-Babel's support
- Compress pictures in projects
- Add pytests , tox 
- Add makefile (?)
- Add structure's description


