import requests
 SLACK_WEBHOOK_URL =
 'https://hooks.slack.com/services/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'
 def send_alert(message):
    """Send a message to Slack using a webhook."""
    payload = {'text': message} # The message content
    try:
        response = requests.post(SLACK_WEBHOOK_URL, json=payload)
        if response.status_code == 200:
            print('Message successfully sent to Slack!')
        else:
            print(f'Failed to send message to Slack, status code: {response.status_code}')
    except Exception as e:
        print(f'Error sending message to Slack: {e}')
 # Example usage of sending an alert
 send_alert('Anomaly detected in log data!')
