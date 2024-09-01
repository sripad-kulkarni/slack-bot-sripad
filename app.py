import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Initializes your app with your bot token and socket mode handler
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)
# Listens to incoming messages that contain "hello"
# To learn available listener arguments,
# visit https://slack.dev/bolt-python/api-docs/slack_bolt/kwargs_injection/args.html
@app.message()
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    say(f"Hey there <@{message['user']}>! Please open a support ticket at help.heroku.com. Thank you!")

@app.event("app_home_opened")
def update_home_tab(client, event, logger):
  try:
    # views.publish is the method that your app uses to push a view to the Home tab
    client.views_publish(
      # the user that opened your app's app home
      user_id=event["user"],
      # the view object that appears in the app home
      view={
        "type": "home",
        "callback_id": "home_view",

        # body of the view
        "blocks": [
          {
            "type": "section",
            "text": {
              "type": "mrkdwn",
              "text": "Hi <@{app_home_opened['user']}>! *Welcome to your _App's Home tab_* :tada:"
            }
          },
          {
            "type": "divider"
          },
          {
            "type": "section",
            "text": {
              "type": "mrkdwn",
              "text": "This button won't do much for now but you can set up a listener for it using the `actions()` method and passing its unique `action_id`. See an example in the `examples` folder within your Bolt app."
            }
          },
          {
            "type": "actions",
            "elements": [
              {
                "type": "button",
                "text": {
                  "type": "plain_text",
                  "text": "Click me!"
                }
              }
            ]
          }
        ]

        {
    "blocks": [
        {
            "type": "input",
            "block_id": "ticket_id_block",
            "label": {
                "type": "plain_text",
                "text": "Ticket ID"
            },
            "element": {
                "type": "plain_text_input",
                "action_id": "ticket_id",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Enter Ticket ID"
                }
            }
        },
        {
            "type": "input",
            "block_id": "current_shift_block",
            "label": {
                "type": "plain_text",
                "text": "Current Shift"
            },
            "element": {
                "type": "static_select",
                "action_id": "current_shift",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Select current shift"
                },
                "options": [
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "APAC"
                        },
                        "value": "apac"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "IST"
                        },
                        "value": "ist"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "EMEA"
                        },
                        "value": "emea"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "EST"
                        },
                        "value": "est"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "PST"
                        },
                        "value": "pst"
                    }
                ]
            }
        },
        {
            "type": "input",
            "block_id": "handoff_shift_block",
            "label": {
                "type": "plain_text",
                "text": "Handoff Shift"
            },
            "element": {
                "type": "static_select",
                "action_id": "handoff_shift",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Select handoff shift"
                },
                "options": [
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "APAC"
                        },
                        "value": "apac"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "IST"
                        },
                        "value": "ist"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "EMEA"
                        },
                        "value": "emea"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "EST"
                        },
                        "value": "est"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "PST"
                        },
                        "value": "pst"
                    }
                ]
            }
        },
        {
            "type": "input",
            "block_id": "handoff_type_block",
            "label": {
                "type": "plain_text",
                "text": "Handoff Type"
            },
            "element": {
                "type": "static_select",
                "action_id": "handoff_type",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Select handoff type"
                },
                "options": [
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "Full Handoff"
                        },
                        "value": "full_handoff"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "Partial Handoff"
                        },
                        "value": "partial_handoff"
                    }
                ]
            }
        },
        {
            "type": "input",
            "block_id": "handoff_summary_block",
            "label": {
                "type": "plain_text",
                "text": "Handoff Summary"
            },
            "element": {
                "type": "plain_text_input",
                "action_id": "handoff_summary",
                "multiline": true,
                "placeholder": {
                    "type": "plain_text",
                    "text": "Enter summary of the handoff"
                }
            }
        },
        {
            "type": "actions",
            "block_id": "acknowledge_button_block",
            "elements": [
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Acknowledge"
                    },
                    "style": "primary",
                    "action_id": "acknowledge_handoff"
                }
            ]
        }
    ]
}
      }
    )

  except Exception as e:
    logger.error(f"Error publishing home tab: {e}")


# Start your app
if __name__ == "__main__":
    #SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
    app.start(port=int(os.environ.get("PORT", 3000)))