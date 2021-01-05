"""
------------------------------------------------------------------------
MessageBlock Module
------------------------------------------------------------------------
"""

class MessageBlock:
    """Forms the response message based on user input """

    WELCOME_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Welcome to Password Manager! :wave:\n\n"
                "*Commands:*"
            ),
        },
    }
    
    DIVIDER_BLOCK = {"type": "divider"}

    STORE_PASSWORD = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (":floppy_disk: *STORE PASSWORD :floppy_disk::*\n_Store your passwords with the following "
                     "format_:\n \t*`sp`* \n\tEnter *sp * "
                     "to perform this command "
                     ),
        },
    }

    GET_PASSWORD = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (":unlock: *GET PASSWORD :unlock::*\n_Store your passwords with the following "
                     "format_:\n \t*`gp <Insert Account Name>`* \n\tEnter "
                     "*gp* , followed by the *name of the account* \n \tassociated with "
                     "your password to perform this command "
                     ),
        },
    }

    PASS_HEADER = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "_*Storing password...*_ \n\n \t*Password Choices:*"
            ),
        },
    }

    GEN_PASSWORD = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ("*GENERATE SECURE PASSWORD:*\n \t*`gen_pass <Insert Account Name>`* \n\tEnter "
                     "*gen_pass* , followed by the *name of the account* to generate a secure password "
                     ),
        },
    }

    CREATE_PASSWORD = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ("*CREATE YOUR OWN PASSWORD:*\n \t*`create_pass <Insert Account Name> <Insert "
                     "Password>`* \n\tEnter "
                     "*create_pass* , followed by the *name of the account* and *password* to create your \n\town "
                     "password "
                     ),
        },
    }

    def __init__(self, channel):
        self.channel = channel
        self.username = "pythonboardingbot"
        self.icon_emoji = ":robot_face:"
        self.timestamp = ""
        self.reaction_task_completed = False
        self.pin_task_completed = False

    def get_start_message_payload(self):
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                self.WELCOME_BLOCK,
                self.DIVIDER_BLOCK,
                self.STORE_PASSWORD,
                self.DIVIDER_BLOCK,
                self.GET_PASSWORD,
            ],
        }

    def get_choice_message_payload(self):
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                self.PASS_HEADER,
                self.DIVIDER_BLOCK,
                self.GEN_PASSWORD,
                self.DIVIDER_BLOCK,
                self.CREATE_PASSWORD,
            ],
        }

    def get_store_password_payload(self, account, password):
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "*Password Stored! :smile:*"
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": ":ledger: *Account:*\n \t\t\t{}".format(account)
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": ":key: *Password:*\n \t\t\t{}".format(password)
                    }
                },
                {
                    "type": "divider"
                }
            ]
        }

    def get_retrieve_password_payload(self, account, password):
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "*Password Retrieved! :smile:*"
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": ":ledger: *Account:*\n \t\t\t{}".format(account)
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": ":key: *Password:*\n \t\t\t{}".format(password)
                    }
                },
                {
                    "type": "divider"
                }
            ]
        }
