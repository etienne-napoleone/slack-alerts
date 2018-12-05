<h5 align='center'>SLACK-ALERTS</h5>
<h6 align='center'>
  SIMPLE SLACK ALERTING PYTHON LIBRARY<br/>
  ────
</h6>
<div align='center'>
  <a href='https://travis-ci.org/etienne-napoleone/slack-alerts'>
    <img src='https://travis-ci.org/etienne-napoleone/slack-alerts.svg?branch=develop' alt='Build Status' />
  </a>
  <a href='https://coveralls.io/github/etienne-napoleone/slack-alerts?branch=develop'>
    <img src='https://coveralls.io/repos/github/etienne-napoleone/slack-alerts/badge.svg?branch=develop' alt='Coverage Status' />
  </a>
</div>

&nbsp;

&nbsp;

### Usage

```
import slack_alerts

alerter = slack_alerts.Alerter('https://your-slack.webhook/url')
alerter.critical('something bad happened!!')
```

### Installation

With pip

```bash
pip3 install --user slack_alerts
```

As a dependency

```bash
# with poetry
poetry add slack_alerts

# with virtualenv
virtualenv -p python3 .env
source .env/bin/activate
pip install slack_alerts

# with pipenv
pipenv install slack_alerts
```

### Tests

Run pytest for unit tests

```bash
# you need a valid slack webhook url as there is no api mocking
export SLACK_WEBHOOK_URL='https://...'

poetry run coverage run --source slack_alerts -m pytest -v
poetry run coverage report
```

Run flake8 for code style

```bash
poetry run flake8 .
```

### Built With

* [Poetry](https://github.com/sdispater/poetry) - Python dependency management made great
* [Requests](https://github.com/requests/requests) - The famous and robust http client library

<!--
### Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

### Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

### Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

### Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
-->
