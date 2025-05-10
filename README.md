# Spotify Ad Block for Clash

## Structure

- SpotifyBlocklist.txt

	- All Spotify Ad server list
	- From [SpotifyAdBlock](https://github.com/x0uid/SpotifyAdBlock)

- scripts.py

	- Run as

		```bash
		python scripts.py
		```

	- This scripts will generate a js file `config.js`.

- config.js

	- Directly store the variable that can be used in clash scripts e.g.

		```javascript
		const prependRule = [
			"DOMAIN, ad.spotify.com, REJECT",
		// more rules
		];
		```

## Usage

In Clash Verge, self-defined rules can be add in `Profiles`>`Global Extend Script`

Double click the `Global Extend Script`, you will see javascript scripts like

```javascript
// Define main function (script entry)

function main(config, profileName) {
  return config;
}
```

Replace the scripts e.g.

```javascript
// This varible is copied from the config.js
const prependRule = [
	"DOMAIN, ad.spotify.com, REJECT",
// more rules
];

function main(config, profileName) {
  let oldrules = config["rules"];
  config["rules"] = prependRule.concat(oldrules);
  return config;
}
```

Save the change and then all ad from the spotify can be blocked.

## Reference

- [Clash Verge Docs](https://www.clashverge.dev/guide/rules.html)
- [SpotifyAdBlock](https://github.com/x0uid/SpotifyAdBlock)