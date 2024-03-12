# Playwrigth tests on multiple browsers

This repo is a showcase how to run Playwright tests on multiple browsers
inside a nix-shell.

On my Mac, the tests run just fine on all three browser types:

```shell
$ nix-shell
[nix-shell:~/work/playwright_test]$ python test.py
Running test on chromium
Running test on firefox
Running test on webkit
```

However, [they fail on Ubuntu-based GitHub Actions](https://github.com/zupo/playwright_test/actions/runs/8247091113/job/22554514652):

```shell
...
playwright._impl._api_types.Error: Executable doesn't exist at /nix/store/i8s3akd29p16wzrafaqk360323kjxl1x-playwright-browsers-chromium/firefox-1424/firefox/firefox
```