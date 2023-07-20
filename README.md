# SPA-task

## About
SPA-task is single-page application, 
that allows you to write comments.

Click "New message" to write your message or "Add answer" to answer.
You should fill the form to send it. You can use tag buttons to format your text 
and click "Preview" to watch the end formatting.
You can also add jpg, png and gif files to your comment.
You can view the full-size image by clicking on it.

Comments are displayed on pages (25 root comments per one page).
Use the navigation bar below the comments to turn pages.

Also, you can sort the comments using top bar.
Select the parameter for sorting on the top bar and click chekbox,
if you want to display comments in descending order.


## Installation
1. Clone this git repository
2. Install requirements
```bash
pip install -r requirements.txt
```
3. Add your host name in SPA-task/SPA/SPA/settings.py
```py3
ALLOWED_HOSTS = [<your hosts>]
```
4. Set the RECAPTCHA_PUBLIC_KEY and RECAPTCHA_PRIVATE_KEY, obtained from reCAPTCHA in settings.py
5. Edit the SPA-task/Dockerfile by setting your host and port
6. Build the docker image
```bash
docker build . -t <TAG>
```
7. Run the container
```bash
docker run -dp <HOST> -t <TAG>
```

