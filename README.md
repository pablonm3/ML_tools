Tools for managing small Machine Learning projects

list of tools:
- Slack Bot

## Installation
`pip install ML-tools`


## Usage

### Post message to Slack
        from ML_tools import SlackNotifier
        SlackNotifier(TOKEN).message("testing baby")


### Post error to Slack
        from ML_tools import SlackNotifier
        try:
            smart = 1/0
        except Exception as e:
            SlackNotifier(TOKEN).error(e)