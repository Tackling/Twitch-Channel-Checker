---

# Twitch Channel Checker

Twitch Channel Checker is a Python script that checks the stream status of Twitch channels using the Twitch API. It reads a list of Twitch channel usernames from a text file and for each channel, it sends a request to the Twitch API to get the stream status. If the channel is live, the program writes the channel name to a "live.txt" file; if the channel is offline, it writes the channel name to an "offline.txt" file. The program can be useful for Twitch viewers or streamers who want to keep track of which channels are live or offline.

## Usage

To use the Twitch Channel Checker, you will need to obtain a Twitch API client ID and access token. You can obtain these by registering a new Twitch application in the [Twitch developer console](https://dev.twitch.tv/console/apps).

Once you have obtained your client ID and access token, replace the placeholders in the `headers` variable in `checker.py` with your client ID and access token.

Next, create a text file called `usernames.txt` in the same directory as `twitch_channel_checker.py`. List the Twitch channel usernames you want to check, one per line.

Finally, run the `twitch_channel_checker.py` script with Python 3. The program will output messages indicating which channels are live or offline, and will write the channel names to the appropriate files.

## Contributing

If you find any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This program is licensed under the MIT license. See the `LICENSE` file for more information.

