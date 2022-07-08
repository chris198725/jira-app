# jira-app

## Guides

### 1. Create API token

https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/

### 2. Create .env file

Parameters

- SITE_URL (e.g. https://sample.atlassian.net)
- API_VERSION
- ACCOUNT (Email address of your atlassian account)
- TOKEN (Token created in step 1)

### 3. Run scripts

Example

```
python scripts/batch_update_permission_scheme.py
```
