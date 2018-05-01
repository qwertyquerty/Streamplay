# Streamplay
A little program for letting Twitch chat play the games you stream by just typing the keys in chat!


### The Config

```json
{
  "oauth": "",
  "channel": "",
  "keys": {
    "up":0.4,
    "left":0.4,
    "down":0.4,
    "right":0.4,
    "a": 0.2,
    "b": 0.2,
    "x": 0.2,
    "y": 0.2,
    "q": 0.2,
    "e": 0.2,
    "shift": 0.2,
    "enter": 0.2
  }
}
```

Above is what the config file looks like. "What do I put in it?" Here you go:

* `oauth`: This is your oauth token you use to read chat. You can get it here [https://twitchapps.com/tmi/](https://twitchapps.com/tmi/) Make sure no one sees it!
* `channel`: This is your channel name. Enter it the exact way you enter it when you login to Twitch.
* `keys`: This is a dictionary of keys that the chatters are allowed to use. Each number is the time the key is held in seconds.

And there you go! Have fun! If you have any issues, please submit them. Feel free to contribute with pull requests!
