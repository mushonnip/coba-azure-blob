from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'nyobablob' # Must be replaced by your <storage_account_name>
    account_key = 'PEV+ARbR8G+rosYHYyBuN20zHdyioXhDdNTTdtijqfjKgMgVbO0s6W1QiStdXSWxhwCrqLIkD7/n39iHFyX/3Q==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'nyobablob' # Must be replaced by your storage_account_name
    account_key = 'PEV+ARbR8G+rosYHYyBuN20zHdyioXhDdNTTdtijqfjKgMgVbO0s6W1QiStdXSWxhwCrqLIkD7/n39iHFyX/3Q==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None