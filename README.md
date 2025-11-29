# BrowserStack Automation with AI Agent

This project demonstrates how to use the BrowserStack Cross-Browser Automation Agent to bootstrap test script development.

## Prerequisites

- Python 3
- BrowserStack Account

## Setup

1.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2.  Configure BrowserStack credentials:
    - Open `browserstack.yml` and replace `YOUR_USERNAME` and `YOUR_ACCESS_KEY` with your BrowserStack credentials.
    - Alternatively, set `BROWSERSTACK_USERNAME` and `BROWSERSTACK_ACCESS_KEY` environment variables.

## Running Tests

Run the tests using the BrowserStack SDK:

```bash
browserstack-sdk pytest login_test.py
```

## Scenarios

- **Login Scenario**: The test `login_test.py` uses natural language commands (AI Authoring) to perform a login on `https://ecommercebs.vercel.app/`.

## Platforms

The tests are configured to run on:
- Windows 11 (Chrome)
- macOS Sonoma (Chrome)
- iOS (iPhone 15, Safari)
- Android (Samsung Galaxy S24, Chrome)

## Proof of Execution

After running the tests, you can view the results on the [BrowserStack Automate Dashboard](https://automate.browserstack.com/).
Public build link will be available in the dashboard.
