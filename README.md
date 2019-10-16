# Team Project repo
Heroku Production URI: [https://nyu-mercury.herokuapp.com](https://nyu-mercury.herokuapp.com)

Heroku Dashboard: [https://dashboard.heroku.com/apps/nyu-mercury](https://dashboard.heroku.com/apps/nyu-mercury)
# HOWTO Contribute to this repo

N.B.: `<something>` means you need to change the `something` text within the angle brackets (and do not include the include brackets in your command).
1. Make a feature branch
`git checkout -b <new_branch_name>`
2. Make your changes
3. Use `git add <filename> ...` to add files you changed or more conveniently, `git add -A`.
4. Commit your changes with `git commit -m "<message_of_what_this_commit_does>"`.
5. Push your branch to the origin fork with `git push origin <new_branch_name>` of the branch you made locally.
6. Visit [our repo](https://github.com/gcivil-nyu-org/fall2019-cs-gy-6063-team-moonsurvivors/pulls) to create a Pull Request or use the link that the `git` command printed for you.
7. Add someone on the team as a review or share your URL to the Slack channel.

# HOWTO Run the app locally
Run `python manage.py runserver` from the root of this Git repo

# HOWTO Push to Heroku
## Push develop branch to Heroku
Run `git push heroku develop:master`

## Push a feature branch to Heroku
Do you really need to do this? If so, you can can run `git push heroku <local_branch>:master` if you need to test your local changes on the Heroku app. Just be mindful that it will replace the existing running Heroku deployment, which someone else may be using.

# Things you should only have to do once
## HOWTO prepare to push to Heroku
You should only have to complete this once (to configure your local repo to have the Heroku remote)

1. `heroku login`
2. `heroku git:remote -a nyu-mercury`

Repo now has a remote called "heroku" that can be pushed to using "git push heroku"

## HOWTO configure Django app for deployment
- Add the following lines to settings.py
--    `import django_heroku`
--    `django_heroku.settings(locals())`
- Create a Procfile containing the following line
--    `web: gunicorn <project-name>.wsgi`
- Create a requirements.txt containing the following lines
-- `gunicorn`
-- `django_heroku`