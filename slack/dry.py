from slacker import Slacker

slack = Slacker('xoxp-2189814853-16355864855-134060798294-abebead05219cf6f4a4427760d800a3f')

# Send a message to #general channel
slack.chat.post_message('#test-fred', 'Testing -testing 123')

# Get users list
#response = slack.users.list()
#users = response.body['members']
