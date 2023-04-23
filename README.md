# Twitch Channel Status Checker

This Python script checks the status of a list of Twitch channels and writes the result to separate files for live and offline channels.

## How to Use

1. Clone the repository or download via zip.

2. Create a `usernames.txt` file in the same directory as the script.

3. Add the usernames of the Twitch channels you want to check to the `usernames.txt` file, with each username on a separate line.

4. Run the script using Python 3. The status of each channel will be checked and written to separate files named `live.txt` and `offline.txt`, also located in the same directory as the script.

## Authentication

The script uses Twitch API v5 to check the stream status of each channel. To authenticate with the Twitch API, you will need to provide a `Client-ID` and an `Authorization` token. These are set up in the script using placeholders. 

To get your own `Client-ID` and `Authorization` token, follow these steps:

1. Create a Twitch account if you don't have one already.

2. Go to the [Twitch Developer Dashboard](https://dev.twitch.tv/console/apps) and create a new application.

3. Note the `Client-ID` generated for your application.

4. Generate an `Authorization` token for your application using the [Twitch API Authentication Guide](https://dev.twitch.tv/docs/authentication/getting-tokens-oauth#oauth-authorization-code-flow). The token must have the `user:read:email` scope.

5. Replace the placeholders in the script with your `Client-ID` and `Authorization` token.

# Notes

The script creates 10 worker threads to check the status of the channels in parallel, making it more efficient.

If a channel is already in the live.txt or offline.txt files, it will not be added again to avoid duplicates.

Finally, the script will print a message indicating that the process is complete once all channels have been checked.


## Dependencies

This script requires the `requests` and `colorama` modules. You can install them using `pip`:

```bash
pip install requests
pip install colorama
```

## License

This program is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more information.

## Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue on GitHub or submit a pull request.
